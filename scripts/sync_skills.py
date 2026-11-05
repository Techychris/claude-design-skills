#!/usr/bin/env python3
"""Mirror your own claude.ai skills into this repo and refresh the README index.

Reads the synced-skills manifest that Claude sessions keep on disk, picks the
skills you uploaded (skillId starts with "skill_"; Anthropic built-ins don't),
copies each into a top-level folder of the same name, and rewrites the table
between the SKILLS-INDEX markers in README.md.

Usage:
  python3 scripts/sync_skills.py                # auto-find the synced dir
  python3 scripts/sync_skills.py --src DIR      # explicit synced dir
  python3 scripts/sync_skills.py --dry-run      # show what would change

Folders for skills that are no longer in your account are reported, not
deleted. Remove them yourself if you want them gone from the repo.
"""
import argparse, filecmp, glob, json, os, shutil, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
START, END = "<!-- SKILLS-INDEX:START -->", "<!-- SKILLS-INDEX:END -->"
KEEP = {".git", ".github", "scripts", "tests", "README.md", "LICENSE", "NOTICE"}


def find_src():
    hits = glob.glob(os.path.expanduser("~/.claude/skills/synced/*/manifest.json"))
    if len(hits) != 1:
        sys.exit(f"Expected one synced manifest, found {len(hits)}. Pass --src.")
    return os.path.dirname(hits[0])


def tree_equal(a, b):
    if not os.path.isdir(b):
        return False
    c = filecmp.dircmp(a, b)
    if c.left_only or c.right_only or c.funny_files:
        return False
    _, mismatch, errors = filecmp.cmpfiles(a, b, c.common_files, shallow=False)
    return not mismatch and not errors and all(
        tree_equal(os.path.join(a, d), os.path.join(b, d)) for d in c.common_dirs)


def short(desc, n=160):
    desc = " ".join(desc.split()).replace("|", "\\|")
    return desc if len(desc) <= n else desc[: n - 1].rsplit(" ", 1)[0] + "…"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    src = args.src or find_src()
    manifest = json.load(open(os.path.join(src, "manifest.json")))
    mine = sorted((s for s in manifest["skills"] if s["skillId"].startswith("skill_")),
                  key=lambda s: s["name"])

    changed = []
    for s in mine:
        a, b = os.path.join(src, s["name"]), os.path.join(REPO, s["name"])
        if not os.path.isfile(os.path.join(a, "SKILL.md")):
            print(f"skip {s['name']}: no SKILL.md in {a}")
            continue
        if tree_equal(a, b):
            continue
        changed.append(s["name"])
        if not args.dry_run:
            shutil.rmtree(b, ignore_errors=True)
            shutil.copytree(a, b)

    names = {s["name"] for s in mine}
    stale = sorted(d for d in os.listdir(REPO)
                   if os.path.isdir(os.path.join(REPO, d)) and d not in KEEP | names
                   and not d.startswith("."))

    rows = "\n".join(f"| [`{s['name']}`]({s['name']}/SKILL.md) | {short(s['description'])} |"
                     for s in mine)
    table = f"{START}\n| Skill | Use it for |\n| --- | --- |\n{rows}\n{END}"
    readme_path = os.path.join(REPO, "README.md")
    readme = open(readme_path).read()
    if START in readme and END in readme:
        new = readme[: readme.index(START)] + table + readme[readme.index(END) + len(END):]
    else:
        new = readme.rstrip() + "\n\n## Skills\n\n" + table + "\n"
    readme_changed = new != readme
    if readme_changed and not args.dry_run:
        open(readme_path, "w").write(new)

    print(f"{len(mine)} skills in account; {len(changed)} updated: {', '.join(changed) or 'none'}")
    print(f"README index {'updated' if readme_changed else 'unchanged'}")
    if stale:
        print(f"Not in account any more (left in place): {', '.join(stale)}")


if __name__ == "__main__":
    main()
