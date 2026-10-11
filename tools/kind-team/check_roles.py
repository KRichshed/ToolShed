#!/usr/bin/env python3
"""Check kind team roles against the shared rules. Needs Python 3 and PyYAML.

Usage:
  python3 tools/kind-team/check_roles.py                 # every role
  python3 tools/kind-team/check_roles.py kind-qa-tester  # one role
  python3 tools/kind-team/check_roles.py --draft NAME    # allow {{placeholders}} while a role is being written

Exit code 0 means no errors. Warnings never fail the run.
"""
import json, re, sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is needed: pip install pyyaml")

REPO = Path(__file__).resolve().parents[2]
SKILLS = REPO / "plugins" / "kind-team" / "skills"
REFERENCE_ROLE = "kind-product-manager"   # the role the shared text is copied from
STANDARD_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
REQUIRED_FILES = ["SKILL.md", "references/kind-contract.md", "assets/learning-log-entry.md", "evals/evals.json"]
CORE_START, CORE_END = "## How you work with people", "## What this role protects"
SECRET_PATTERNS = [r"sk_(live|test)_[A-Za-z0-9]{10,}", r"AKIA[0-9A-Z]{16}", r"ghp_[A-Za-z0-9]{20,}", r"-----BEGIN [A-Z ]*PRIVATE KEY"]
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
OK_EMAILS = {"noreply@anthropic.com", "noreply@github.com"}


def core(text):
    s, e = text.find(CORE_START), text.find(CORE_END)
    return text[s:e] if s != -1 and e != -1 else None


def check_role(name, draft, ref_core, ref_contract):
    errors, warnings = [], []
    root = SKILLS / name
    if not root.is_dir():
        return [f"no folder at {root}"], []
    for f in REQUIRED_FILES:
        if not (root / f).is_file():
            errors.append(f"missing file: {f}")
    skill = root / "SKILL.md"
    if not skill.is_file():
        return errors, warnings
    text = skill.read_text()
    if not (root / "references/role-primer.md").is_file():
        warnings.append("no references/role-primer.md. Fine only if the role cites no standards, prices or laws")
    # frontmatter
    parts = text.split("---")
    if not text.startswith("---") or len(parts) < 3:
        return errors + ["SKILL.md has no frontmatter block starting on line 1"], warnings
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as exc:
        return errors + [f"frontmatter is not valid YAML (a stray colon in the description is the usual cause): {str(exc).splitlines()[0]}"], warnings
    extra = set(fm) - STANDARD_FIELDS
    if extra:
        errors.append(f"frontmatter fields outside the six standard ones: {sorted(extra)}")
    if fm.get("name") != name:
        errors.append(f"name {fm.get('name')!r} does not match the folder {name!r}")
    if not re.fullmatch(r"kind-[a-z0-9]+(-[a-z0-9]+)*", name):
        errors.append("role names are lowercase, hyphenated, and start with kind-")
    desc = str(fm.get("description", ""))
    if not desc.strip():
        errors.append("description is empty")
    if len(desc) > 1024:
        errors.append(f"description is {len(desc)} characters, the limit is 1024")
    if text.count("\n") > 500:
        errors.append(f"SKILL.md is {text.count(chr(10))} lines, keep it under 500")
    # shared text
    c = core(text)
    if c is None:
        errors.append("the contract core section is missing")
    elif ref_core is not None and c != ref_core and name != REFERENCE_ROLE:
        errors.append(f"the contract core differs from {REFERENCE_ROLE}'s. Copy it across, don't edit it in one role")
    contract = root / "references/kind-contract.md"
    if contract.is_file() and ref_contract is not None and contract.read_text() != ref_contract and name != REFERENCE_ROLE:
        errors.append(f"references/kind-contract.md differs from {REFERENCE_ROLE}'s")
    # placeholders
    for f in [p for p in root.rglob("*") if p.is_file()]:
        body = f.read_text(errors="ignore")
        if "{{" in body or re.search(r"\bTODO\b", body):
            (warnings if draft else errors).append(f"unfinished placeholder in {f.relative_to(root)}")
        for pat in SECRET_PATTERNS:
            if re.search(pat, body):
                errors.append(f"looks like a real secret in {f.relative_to(root)} (pattern {pat})")
        for m in EMAIL.findall(body):
            if m.lower() not in OK_EMAILS and not m.lower().endswith("@example.com"):
                errors.append(f"email address in {f.relative_to(root)}: {m}")
    # evals
    ev_path = root / "evals/evals.json"
    if ev_path.is_file():
        try:
            ev = json.loads(ev_path.read_text())
        except json.JSONDecodeError as exc:
            errors.append(f"evals.json is not valid JSON: {exc}")
            ev = None
        if ev:
            if ev.get("skill") != name:
                errors.append(f"evals.json 'skill' is {ev.get('skill')!r}, expected {name!r}")
            sc = ev.get("scenarios", [])
            if len(sc) < 3:
                errors.append("evals.json needs at least 3 scenarios")
            ids = [s.get("id") for s in sc]
            if len(ids) != len(set(ids)):
                errors.append("scenario ids must be unique")
            for s in sc:
                if not s.get("prompt") or not s.get("expect"):
                    errors.append(f"scenario {s.get('id')!r} needs a prompt and an expect list")
            tr = ev.get("triggers", {})
            if len(tr.get("should_trigger", [])) < 5 or len(tr.get("should_not_trigger", [])) < 5:
                errors.append("evals.json needs at least 5 should_trigger and 5 should_not_trigger prompts")
            if not ev.get("teaching_checks"):
                errors.append("evals.json needs teaching_checks")
            if not any("hand-off-pack-missing" in str(i) for i in ids):
                warnings.append("no scenario tests a hand-off pack with a missing part")
    return errors, warnings


def main(argv):
    draft = "--draft" in argv
    names = [a for a in argv if not a.startswith("--")] or sorted(p.name for p in SKILLS.iterdir() if p.is_dir())
    ref = SKILLS / REFERENCE_ROLE
    ref_core = core((ref / "SKILL.md").read_text()) if (ref / "SKILL.md").is_file() else None
    ref_contract = (ref / "references/kind-contract.md").read_text() if (ref / "references/kind-contract.md").is_file() else None
    failed = False
    for n in names:
        errs, warns = check_role(n, draft, ref_core, ref_contract)
        status = "FAIL" if errs else ("ok (warnings)" if warns else "ok")
        print(f"{n}: {status}")
        for e in errs: print(f"   error: {e}")
        for w in warns: print(f"   warning: {w}")
        failed = failed or bool(errs)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
