#!/usr/bin/env python3
"""Start a new kind team role from the skeleton.

Usage: python3 tools/kind-team/new_role.py kind-qa-tester "QA tester"

Creates plugins/kind-team/skills/<name>/ with the shared contract text copied in
exactly, and placeholders in {{double braces}} for you to fill. Then run:
  python3 tools/kind-team/check_roles.py --draft <name>     while you write
  python3 tools/kind-team/check_roles.py <name>             when every placeholder is gone
"""
import re, shutil, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SKILLS = REPO / "plugins" / "kind-team" / "skills"
SKELETON = Path(__file__).resolve().parent / "role-skeleton"
REFERENCE = SKILLS / "kind-product-manager"
START, END = "## How you work with people", "## What this role protects"


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    name, title = sys.argv[1], sys.argv[2]
    if not re.fullmatch(r"kind-[a-z0-9]+(-[a-z0-9]+)*", name):
        sys.exit("The role name must be lowercase, hyphenated, and start with kind-, for example kind-qa-tester")
    dest = SKILLS / name
    if dest.exists():
        sys.exit(f"{dest} already exists. Nothing was changed.")
    ref = (REFERENCE / "SKILL.md").read_text()
    core = ref[ref.index(START):ref.index(END)]
    shutil.copytree(SKELETON, dest)
    for f in [p for p in dest.rglob("*") if p.is_file()]:
        t = f.read_text()
        t = t.replace("{{CONTRACT_CORE}}\n", core).replace("{{ROLE}}", name).replace("{{TITLE_LOWER}}", title.lower()).replace("{{TITLE}}", title)
        f.write_text(t)
    shutil.copyfile(REFERENCE / "references/kind-contract.md", dest / "references/kind-contract.md")
    print(f"Created {dest.relative_to(REPO)}")
    print("Next: fill every {{placeholder}}, then run check_roles.py --draft, then the test harness.")


if __name__ == "__main__":
    main()
