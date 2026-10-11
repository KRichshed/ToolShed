#!/usr/bin/env python3
"""Run a kind team role's tests in an isolated Claude Code setup.

Usage:
  python3 tools/kind-team/run_role_tests.py kind-qa-tester
  python3 tools/kind-team/run_role_tests.py kind-qa-tester --reps 3 --baseline --blind
  python3 tools/kind-team/run_role_tests.py kind-qa-tester --only main-review,just-tell-me --no-triggers

What it does, in a temporary folder (never your real Claude settings):
  1. Installs the plugin from this repository into a throw-away Claude Code config.
  2. Runs the role's trigger prompts and scenarios from evals/evals.json, several times each.
  3. With --baseline, runs the scenarios again with no plugin installed.
  4. With --blind, writes the with-skill and without-skill replies as shuffled A and B files for a grader, plus a key.
  5. Writes summary.md and prints it.

Needs: the claude command, and a way to log in that works with a fresh config folder
(set ANTHROPIC_API_KEY, or run `CLAUDE_CONFIG_DIR=<workdir>/cfg-with claude` once to log in).
File-writing, shell and web tools are switched off for the test runs, so roles can only answer.
Never put real keys, personal details or private project files in an evals file.
"""
import argparse, json, os, random, re, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SKILLS = REPO / "plugins" / "kind-team" / "skills"
DENY = ["--disallowedTools", "Bash", "Write", "Edit", "NotebookEdit", "WebSearch", "WebFetch", "Agent"]
SYNC_VARS = ("CLAUDE_CODE_SYNC_SKILLS", "CLAUDE_ADDITIONAL_DIRECTORIES", "CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD")


def base_env(cfg):
    env = {k: v for k, v in os.environ.items() if k not in SYNC_VARS}
    env["CLAUDE_CONFIG_DIR"] = str(cfg)
    return env


def sh(cmd, env, cwd):
    return subprocess.run(cmd, env=env, cwd=cwd, capture_output=True, text=True, timeout=600)


def install_plugin(cfg, cwd):
    env = base_env(cfg)
    r = sh(["claude", "plugin", "marketplace", "add", str(REPO)], env, cwd)
    r2 = sh(["claude", "plugin", "install", "kind-team@toolshed"], env, cwd)
    ok = "uccessfully installed" in (r2.stdout + r2.stderr)
    if not ok:
        sys.exit("Could not install the plugin into the test setup.\n" + r.stdout + r.stderr + r2.stdout + r2.stderr)
    listed = sh(["claude", "plugin", "list"], env, cwd).stdout
    if "kind-team@toolshed" not in listed:
        sys.exit("The plugin did not show up in the test setup, so a 'not loaded' result would mean nothing.")


def run_one(job):
    prompt, out, cfg, cwd, turns = job
    r = sh(["claude", "-p", prompt, "--output-format", "stream-json", "--verbose", "--max-turns", str(turns), *DENY], base_env(cfg), cwd)
    tools, final = [], ""
    for line in r.stdout.splitlines():
        if not line.startswith("{"):
            continue
        try:
            m = json.loads(line)
        except json.JSONDecodeError:
            continue
        if m.get("type") == "assistant":
            for c in m["message"]["content"]:
                if c.get("type") == "tool_use":
                    tools.append(c["name"] + (":" + c["input"].get("skill", "") if c["name"] == "Skill" else ""))
        if m.get("type") == "result":
            final = m.get("result") or ""
    Path(out).write_text(json.dumps({"prompt": prompt, "tools": tools, "reply": final}, indent=1))


def loaded(tools, role):
    return any(t.startswith("Skill:") and role in t for t in tools)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("role")
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--only", help="comma-separated scenario ids")
    ap.add_argument("--no-triggers", action="store_true")
    ap.add_argument("--baseline", action="store_true")
    ap.add_argument("--blind", action="store_true")
    ap.add_argument("--workdir")
    ap.add_argument("--workers", type=int, default=8)
    a = ap.parse_args()

    evals_path = SKILLS / a.role / "evals/evals.json"
    if not evals_path.is_file():
        sys.exit(f"No evals file at {evals_path}")
    try:
        ev = json.loads(evals_path.read_text())
    except json.JSONDecodeError as exc:
        sys.exit(f"evals.json is not valid JSON, nothing was run: {exc}")
    work = Path(a.workdir or tempfile.mkdtemp(prefix=f"kt-{a.role}-"))
    for d in ("cfg-with", "cfg-without", "cwd", "out-with", "out-without"):
        (work / d).mkdir(parents=True, exist_ok=True)
    print(f"Working in {work}")
    install_plugin(work / "cfg-with", work / "cwd")

    scen = [s for s in ev["scenarios"] if not a.only or s["id"] in a.only.split(",")]
    jobs = []
    for s in scen:
        for r in range(1, a.reps + 1):
            jobs.append((s["prompt"], work / f"out-with/scenario-{s['id']}-r{r}.json", work / "cfg-with", work / "cwd", 8))
            if a.baseline:
                plain = re.sub(rf"Use the {re.escape(a.role)} skill\.\s*", "", s["prompt"])
                jobs.append((plain, work / f"out-without/scenario-{s['id']}-r{r}.json", work / "cfg-without", work / "cwd", 8))
    if not a.no_triggers:
        for kind in ("should_trigger", "should_not_trigger"):
            for i, p in enumerate(ev["triggers"][kind]):
                for r in range(1, a.reps + 1):
                    jobs.append((p, work / f"out-with/trigger-{kind}-{i}-r{r}.json", work / "cfg-with", work / "cwd", 3))
    print(f"Running {len(jobs)} prompts ({a.workers} at a time). This takes a few minutes.")
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(run_one, jobs))

    lines = [f"# Test summary: {a.role}", "", f"{a.reps} runs per prompt. Plugin installed from {REPO}.", ""]
    code = 0
    if not a.no_triggers:
        lines += ["## Triggers", "", "| Kind | Prompt | Loaded this role | Other roles loaded |", "|---|---|---|---|"]
        tot = {"should_trigger": [0, 0], "should_not_trigger": [0, 0]}
        for kind in ("should_trigger", "should_not_trigger"):
            for i, p in enumerate(ev["triggers"][kind]):
                runs = [json.loads((work / f"out-with/trigger-{kind}-{i}-r{r}.json").read_text()) for r in range(1, a.reps + 1)]
                hit = sum(loaded(x["tools"], a.role) for x in runs)
                other = sorted({t.split(":")[-1] for x in runs for t in x["tools"] if t.startswith("Skill:") and a.role not in t})
                tot[kind][0] += hit; tot[kind][1] += len(runs)
                lines.append(f"| {kind.replace('_', ' ')} | {p[:60]} | {hit} of {len(runs)} | {', '.join(other) or '-'} |")
        lines += ["", f"**Should-trigger: {tot['should_trigger'][0]} of {tot['should_trigger'][1]} runs loaded the role. "
                  f"Should-not: {tot['should_not_trigger'][0]} of {tot['should_not_trigger'][1]} did.**", ""]
    lines += ["## Scenarios", "", "| Scenario | Role loaded | Words (with) | Words (without) |", "|---|---|---|---|"]
    for s in scen:
        w = [json.loads((work / f"out-with/scenario-{s['id']}-r{r}.json").read_text()) for r in range(1, a.reps + 1)]
        wo = [json.loads((work / f"out-without/scenario-{s['id']}-r{r}.json").read_text()) for r in range(1, a.reps + 1)] if a.baseline else []
        n = lambda xs: ", ".join(str(len(x["reply"].split())) for x in xs) or "-"
        lines.append(f"| {s['id']} | {sum(loaded(x['tools'], a.role) for x in w)} of {len(w)} | {n(w)} | {n(wo)} |")
        empties = [x for x in w if not x["reply"].strip()]
        if empties:
            lines.append(f"|  | WARNING: {len(empties)} empty replies. Check the setup before trusting this. | | |")
            code = 1
    lines += ["", "Grading is a separate step. Read the replies in out-with/, or use --blind and give the A and B files to a grader who doesn't know which is which."]
    if a.blind:
        if not a.baseline:
            sys.exit("--blind needs --baseline")
        random.seed(7); key = {}
        (work / "blind").mkdir(exist_ok=True)
        for s in scen:
            pair = [(work / f"out-with/scenario-{s['id']}-r1.json", "skill"), (work / f"out-without/scenario-{s['id']}-r1.json", "baseline")]
            random.shuffle(pair)
            for lab, (f, kind) in zip("AB", pair):
                (work / f"blind/{s['id']}-{lab}.md").write_text(json.loads(f.read_text())["reply"])
                key[f"{s['id']}-{lab}"] = kind
        (work / "blind-key.json").write_text(json.dumps(key, indent=1))
        lines.append(f"\nBlind files: {work / 'blind'}. Key (don't show the grader): {work / 'blind-key.json'}.")
    summary = "\n".join(lines) + "\n"
    (work / "summary.md").write_text(summary)
    print("\n" + summary)
    sys.exit(code)


if __name__ == "__main__":
    main()
