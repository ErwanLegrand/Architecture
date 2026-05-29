# Agent Instructions

Guidance for AI agents and human contributors working in this repository.

## What this repository is

A reference framework for **secure agentic architecture**: the security principles, design patterns, and architectural primitives required to build agentic systems that remain secure under adversarial input and suborned models. The content is documentation only — there is no executable code, no build, no test suite.

Authoritative entry points:

- [README.md](/README.md) — orientation.
- [architecture.md](/architecture.md) — normative index with briefs and links to full definitions.
- [agent-types.md](/agent-types.md) — taxonomy of agent types referenced by the primitives.

## Normative wording

Definitions in this repository are **normative**. They are cited from other components and design discussions and must remain stable.

- Do **not** paraphrase, summarize, or "improve the style" of an existing definition. Preserve wording byte-for-byte unless the change is explicitly requested.
- A definition's text lives in its own file under `security principles/`, `design patterns/`, or `architectural primitives/`. The table in `architecture.md` only carries a brief — never duplicate the full definition there.
- If you change a definition, change it in its file and verify the brief in `architecture.md` still accurately summarizes the new wording.
- Deviations from any principle in real systems require explicit justification; deviations from the wording of a principle in this repo require explicit user approval.

## File organization

```
/security principles/        # one file per principle (kebab-case)
/design patterns/            # one file per pattern
/architectural primitives/   # one file per primitive
architecture.md              # index with briefs and links
agent-types.md               # agent taxonomy
README.md                    # repository overview
AGENTS.md                    # this file
```

Conventions:

- Directory names contain spaces intentionally; in Markdown links encode them as `%20` (e.g. `/security%20principles/foo.md`).
- One concept per file. Filename is kebab-case of the concept name (e.g. `least-privilege-principle.md`).
- Each definition file uses a single H1 matching the concept name. Subsections use H2 or bullet lists.

## Adding a new principle, pattern, or primitive

1. Create a file in the matching subdirectory with kebab-case name and H1 title.
2. Write the full normative definition; keep it focused on this one concept.
3. Add a row to the corresponding table in `architecture.md` with a single-sentence brief and a `[→](...)` link to the new file.
4. If the new concept is referenced by other definitions, update those files to link to it.
5. Verify all Markdown links resolve (spaces → `%20`, kebab-case filenames).

## Style

- Markdown only. No HTML, no embedded diagrams, no images unless explicitly requested.
- Plain prose; no marketing tone. Definitions read as specification text, not as a blog post.
- Use the long-dash `—` (not `--`) consistent with existing files.
- Italics for term introductions (`*suborn*`); bold for enumerated property names in bullet lists (`**Output validation.**`).
- Quote model behavior in the third person: "the model", not "Claude" / "GPT" / "the LLM" (except where "LLM" is unavoidable as in *least LLM principle*).

## Commits

- Commit messages should describe what changed in the documentation, not what was decided about the system.
- Do **not** add `Co-Authored-By` or generator attribution unless the user has asked for it for a specific commit. Project policy disables attribution globally.
- One commit per coherent change (e.g., "add hash-chained-logs definition", "rephrase trusted-path-logging brief"). Avoid bundling unrelated wording fixes with structural moves.

## What this repository is not

- Not a how-to guide. Definitions are normative descriptions, not tutorials.
- Not a code project. Do not add `package.json`, `Cargo.toml`, CI workflows, or test scaffolding.
- Not a place for opinions. If a claim is contested or aspirational, mark it as such or omit it.
