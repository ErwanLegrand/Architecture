#!/usr/bin/env python3
"""Regenerate the index tables in architecture.md from definition frontmatter.

The three tables in architecture.md (principles / patterns / primitives) are
generated, not hand-edited. Each table's rows come from the YAML frontmatter of
the files under the matching folder: `title`, `brief`, `order` (sort key), and
the file path. Edit a definition's frontmatter, then run this script.

Usage:
  python3 tools/gen-index.py            # rewrite architecture.md in place
  python3 tools/gen-index.py --check    # exit 1 if architecture.md is stale
"""
import os
import re
import sys
import glob

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(REPO, "architecture.md")

# type -> (folder, column label). Folder names contain literal spaces on disk;
# links encode them as %20.
TYPES = {
    "principle": ("security principles", "Principle"),
    "pattern": ("design patterns", "Pattern"),
    "primitive": ("architectural primitives", "Primitive"),
}


def load(folder):
    out = []
    for path in glob.glob(os.path.join(REPO, folder, "*.md")):
        text = open(path, encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not m:
            sys.exit(f"{path}: missing frontmatter")
        fm = yaml.safe_load(m.group(1))
        for key in ("title", "brief", "order"):
            if key not in fm:
                sys.exit(f"{path}: frontmatter missing '{key}'")
        stem = os.path.splitext(os.path.basename(path))[0]
        out.append(fm | {"stem": stem})
    return sorted(out, key=lambda d: d["order"])


def display_name(title):
    # strip a trailing axis annotation, e.g. "Core agents (trust-position axis)"
    return re.sub(r"\s*\([^)]*\)\s*$", "", title)


def table(kind):
    folder, label = TYPES[kind]
    rows = [f"| {label} | Brief | Full Definition |", "| --- | --- | --- |"]
    for d in load(folder):
        link = f"/{folder.replace(' ', '%20')}/{d['stem']}.md"
        rows.append(f"| **{display_name(d['title'])}** | {d['brief']} | [→]({link}) |")
    return "\n".join(rows)


def render(current):
    out = current
    for kind in TYPES:
        block = table(kind)
        pat = re.compile(
            rf"(<!-- gen:{kind}:start.*?-->\n).*?(\n<!-- gen:{kind}:end -->)",
            re.DOTALL,
        )
        if not pat.search(out):
            sys.exit(f"architecture.md: missing gen markers for '{kind}'")
        out = pat.sub(lambda m: m.group(1) + block + m.group(2), out)
    return out


def main():
    check = "--check" in sys.argv[1:]
    current = open(INDEX, encoding="utf-8").read()
    new = render(current)
    if check:
        if new != current:
            sys.exit(
                "architecture.md is out of date with frontmatter.\n"
                "Run: python3 tools/gen-index.py  (then stage architecture.md)"
            )
        print("architecture.md is up to date.")
        return
    if new != current:
        open(INDEX, "w", encoding="utf-8").write(new)
        print("architecture.md regenerated.")
    else:
        print("architecture.md already up to date.")


if __name__ == "__main__":
    main()
