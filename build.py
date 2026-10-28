#!/usr/bin/env python3
"""
Build the two downloadable skills from this repository into dist/:

  dist/e-disclosure-shareholders.zip   Claude skill:  skills/claude/* + scripts/
  dist/e-disclosure-chatgpt.zip        ChatGPT skill: skills/chatgpt/* + scripts/

Each ZIP holds one top-level folder with SKILL.md at its root, as Claude and ChatGPT expect.
The scripts exist only once, in scripts/, and are copied into both archives here.

Usage: python3 build.py
"""

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
SKILLS = {
    "e-disclosure-shareholders": ROOT / "skills" / "claude",
    "e-disclosure-chatgpt": ROOT / "skills" / "chatgpt",
}


def files_under(folder):
    return sorted(p for p in folder.rglob("*")
                  if p.is_file() and "__pycache__" not in p.parts and not p.name.startswith("."))


def build(name, skill_dir):
    if not (skill_dir / "SKILL.md").exists():
        raise SystemExit(f"{skill_dir}/SKILL.md is missing")
    target = DIST / f"{name}.zip"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files_under(skill_dir):
            z.write(f, f"{name}/{f.relative_to(skill_dir).as_posix()}")
        for f in files_under(ROOT / "scripts"):
            z.write(f, f"{name}/scripts/{f.relative_to(ROOT / 'scripts').as_posix()}")
    with zipfile.ZipFile(target) as z:
        print(f"{target.relative_to(ROOT)}: {len(z.namelist())} files, {target.stat().st_size // 1024} KB")


def main():
    DIST.mkdir(exist_ok=True)
    for name, folder in SKILLS.items():
        build(name, folder)


if __name__ == "__main__":
    main()
