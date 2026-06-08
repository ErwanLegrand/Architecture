#!/usr/bin/env python3
"""Regenerate the per-type index tables from definition frontmatter.

Each concept type has a top-level index file — principles.md, patterns.md,
primitives.md, threats.md, references.md — whose table is generated from the
YAML frontmatter of the files under the matching folder: `title`, `brief`,
`order` (sort key), and the file path. The hand-written prose around the
`<!-- gen:<type>:start -->` / `<!-- gen:<type>:end -->` markers is preserved.
Edit a definition's frontmatter, then run this script.

Reference nodes are pointers to concepts defined in another knowledge base;
they have no `order` and are sorted by title.

Usage:
  python3 tools/gen-index.py            # rewrite the index files in place
  python3 tools/gen-index.py --check    # exit 1 if any index file is stale
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

# type -> (folder, column label, index file). Folder names are space-free.
TYPES = {
    "principle": ("principles", "Principle", "principles.md"),
    "pattern": ("patterns", "Pattern", "patterns.md"),
    "primitive": ("primitives", "Primitive", "primitives.md"),
    "threat": ("threats", "Threat", "threats.md"),
    "reference": ("references", "Reference", "references.md"),
}


def load(kind, folder):
    out = []
    # references are external pointers and carry no `order`.
    required = ("title", "brief") if kind == "reference" else ("title", "brief", "order")
    for path in glob.glob(os.path.join(REPO, folder, "*.md")):
        text = open(path, encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not m:
            sys.exit(f"{path}: missing frontmatter")
        fm = yaml.safe_load(m.group(1))
        for key in required:
            if key not in fm:
                sys.exit(f"{path}: frontmatter missing '{key}'")
        stem = os.path.splitext(os.path.basename(path))[0]
        out.append(fm | {"stem": stem})
    # concepts sort by declared order; references (orderless) sort by title.
    return sorted(out, key=lambda d: (d.get("order", 1_000_000), d["title"]))


def display_name(title):
    # strip a trailing axis annotation, e.g. "Core agents (trust-position axis)"
    return re.sub(r"\s*\([^)]*\)\s*$", "", title)


def domains(d):
    vals = d.get("domains") or []
    if isinstance(vals, str):
        vals = [vals]
    return ", ".join(vals)


def table(kind):
    folder, label, _ = TYPES[kind]
    rows = [f"| {label} | Domain | Brief | Full Definition |", "| --- | --- | --- | --- |"]
    for d in load(kind, folder):
        link = f"/{folder}/{d['stem']}.md"
        rows.append(
            f"| **{display_name(d['title'])}** | {domains(d)} | {d['brief']} | [→]({link}) |"
        )
    return "\n".join(rows)


def render(kind, current):
    block = table(kind)
    pat = re.compile(
        rf"(<!-- gen:{kind}:start.*?-->\n).*?(\n<!-- gen:{kind}:end -->)",
        re.DOTALL,
    )
    if not pat.search(current):
        sys.exit(f"{TYPES[kind][2]}: missing gen markers for '{kind}'")
    return pat.sub(lambda m: m.group(1) + block + m.group(2), current)


def main():
    check = "--check" in sys.argv[1:]
    stale = []
    for kind, (_, _, fname) in TYPES.items():
        path = os.path.join(REPO, fname)
        if not os.path.exists(path):
            sys.exit(f"{fname}: missing index file (expected gen markers for '{kind}')")
        current = open(path, encoding="utf-8").read()
        new = render(kind, current)
        if new == current:
            continue
        if check:
            stale.append(fname)
        else:
            open(path, "w", encoding="utf-8").write(new)
            print(f"{fname} regenerated.")
    if check:
        if stale:
            sys.exit(
                "index files out of date with frontmatter: "
                + ", ".join(stale)
                + "\nRun: python3 tools/gen-index.py  (then stage the index files)"
            )
        print("index files are up to date.")
    else:
        print("done.")


if __name__ == "__main__":
    main()
