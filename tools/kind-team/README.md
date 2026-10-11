# Tools for building kind team roles

These are for people who build roles. They aren't part of the plugin, so they don't install with it.

| File | What it's for |
|---|---|
| `new_role.py` | Starts a role from the skeleton, with the shared contract text copied in exactly |
| `role-skeleton/` | The empty role: standard sections, placeholders, an evals file with the standard scenarios |
| `check_roles.py` | Checks every role against the shared rules. Fast, runs offline, needs PyYAML |
| `run_role_tests.py` | Runs a role's trigger prompts and scenarios in a throw-away Claude Code setup, with and without the role |
| `ROLLOUT.md` | The three levels (Bone, Ready, Proven), the steps, and where each role stands |
| `PULL_REQUEST_ROLE.md` | A pull request description to copy for a new role |

## The loop for a new role

```bash
cd /path/to/ToolShed
python3 tools/kind-team/new_role.py kind-example "Example"
# fill in the {{placeholders}}, checking as you go:
python3 tools/kind-team/check_roles.py --draft kind-example
python3 tools/kind-team/check_roles.py kind-example
claude plugin validate plugins/kind-team --strict
python3 tools/kind-team/run_role_tests.py kind-example --reps 3 --baseline --blind
```

## Good to know

- `run_role_tests.py` uses a temporary Claude Code setup and never touches your own. It needs a login that works in a fresh setup, such as `ANTHROPIC_API_KEY` set in your terminal.
- During test runs the roles can only answer. Shell, file-writing and web tools are switched off.
- The checker and the harness never read your private projects. Keep real project material out of every evals file.
