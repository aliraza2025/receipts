#!/usr/bin/env python3
"""Validate every skills/*/SKILL.md: frontmatter, naming, size, and house style."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_LINES = 500


def frontmatter(text: str) -> dict:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def check(skill_dir: Path) -> list[str]:
    errors = []
    path = skill_dir / "SKILL.md"
    if not path.exists():
        return [f"{skill_dir.name}: missing SKILL.md"]
    text = path.read_text(encoding="utf-8")
    meta = frontmatter(text)
    name = meta.get("name", "")
    description = meta.get("description", "")
    if not name:
        errors.append(f"{skill_dir.name}: missing name")
    elif name != skill_dir.name:
        errors.append(f"{skill_dir.name}: name '{name}' does not match folder")
    elif len(name) > 64 or not NAME_RE.match(name):
        errors.append(f"{skill_dir.name}: name must be lowercase words joined by hyphens, max 64 chars")
    if not description:
        errors.append(f"{skill_dir.name}: missing description")
    elif len(description) > 1024:
        errors.append(f"{skill_dir.name}: description over 1024 chars")
    elif "use when" not in description.lower():
        errors.append(f"{skill_dir.name}: description should say when to use it ('Use when ...')")
    if len(text.splitlines()) > MAX_LINES:
        errors.append(f"{skill_dir.name}: SKILL.md over {MAX_LINES} lines")
    for file in skill_dir.rglob("*"):
        if file.is_file() and file.suffix in {".md", ".py", ".sh", ".txt"}:
            if "\u2014" in file.read_text(encoding="utf-8"):
                errors.append(f"{file.relative_to(ROOT)}: contains an em dash")
    return errors


def main() -> int:
    skills = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
    errors = [e for s in skills for e in check(s)]
    if "\u2014" in (ROOT / "README.md").read_text(encoding="utf-8"):
        errors.append("README.md: contains an em dash")
    for e in errors:
        print(f"FAIL {e}")
    print(f"{len(skills)} skills checked, {len(errors)} problems")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
