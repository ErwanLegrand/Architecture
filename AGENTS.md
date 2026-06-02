# Agent Instructions

Guidance for AI agents and human contributors working in this repository.

## What this repository is

A reference framework for **secure agentic architecture**: the security principles, design patterns, and architectural primitives required to build agentic systems that remain secure under adversarial input and suborned models. The content is documentation only — there is no executable code, no build, no test suite.

Authoritative entry points:

- [README.md](/README.md) — orientation.
- [architecture.md](/architecture.md) — normative index with briefs and links to full definitions. Its "Architectural Primitives" section carries the agent taxonomy (the two-axis classification) and links to the per-primitive files under `architectural primitives/`.

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
README.md                    # repository overview
AGENTS.md                    # this file
```

Conventions:

- Directory names contain spaces intentionally; in Markdown links encode them as `%20` (e.g. `/security%20principles/foo.md`).
- One concept per file. Filename is kebab-case of the concept name (e.g. `least-privilege-principle.md`).
- Each definition file uses a single H1 matching the concept name. Subsections use H2 or bullet lists.

## Frontmatter and relations

Each definition file begins with YAML frontmatter carrying its metadata and its outgoing relations. Relations are machine-readable edges for graph/vector ingestion and for Obsidian relation plugins (Breadcrumbs, Graph Link Types). They live **only** in frontmatter; the prose body is unaffected and keeps its inline `%20` Markdown links.

```yaml
---
id: write-ahead-audit              # canonical node key; equals the filename stem
title: Write-ahead audit           # equals the H1, verbatim
type: principle | pattern | primitive   # equals the containing folder
domains: [security]                # add reliability/performance ONLY where the body already makes that claim
status: draft | stable
# outgoing relations: one top-level key per relation verb, wikilink-list values
implements: ["[[no-agency-without-auditability-principle]]"]
---
```

Rules:

- One top-level key per relation verb; the value is a YAML list of `[[wikilinks]]`, even for a single target. Each `[[target]]` is another file's `id` (its kebab filename stem); basenames are unique across the three folders, so the bare stem resolves.
- Author the **forward** direction only. Inverse edges (`implemented_by`, `constrained_by`, …) are computed — by Breadcrumbs in Obsidian and by the ingestion loader — never written by hand. Single source of truth; no materialized back-references.
- A relation must reflect a claim the prose already makes. To add an edge the prose does not yet support, extend the prose (one sentence, in the definition's voice — see "Normative wording") rather than asserting an ungrounded edge.

Controlled verb vocabulary (forward forms only; use nothing else):

- **structural** — `implements`, `instantiates`, `extends`, `specializes`, `abstracts`, `decomposes_into`, `composes_with`
- **causal** — `enables`, `enhances`, `reduces`, `amplifies`, `stabilizes`, `simplifies`
- **constraint** — `requires`, `depends_on`, `constrains`, `limits`, `isolates`, `protects`, `enforces`
- **trade-off** — `conflicts_with`, `trades_off_with`, `competes_with`, `weakens`
- **semantic** — `defines`, `describes`, `models`, `alias_of`, `related_to`
- **forbidden** — `affects`, `uses`, `helps`, "is related to" (too vague to be an edge)

## Adding a new principle, pattern, or primitive

1. Create a file in the matching subdirectory with kebab-case name and H1 title.
2. Write the full normative definition; keep it focused on this one concept.
3. Add frontmatter: `id` (= filename stem), `title` (= H1, verbatim), `type` (= folder), `domains`, `status`. See "Frontmatter and relations".
4. Encode outgoing relations in frontmatter using the controlled vocabulary — one wikilink-list per verb, forward direction only, each grounded in the prose.
5. Add a row to the corresponding table in `architecture.md` with a single-sentence brief and a `[→](...)` link to the new file.
6. If the new concept is referenced by other definitions, update those files to link to it.
7. Verify links and frontmatter. Run these from the repo root; each prints only on failure.

   Body Markdown links resolve (targets use `%20` for spaces; filesystem paths use literal spaces — decode before testing):

   ```bash
   grep -rhoE '\]\(/[^)]+\)' --include='*.md' . \
     | sed -E 's/^\]\(\/(.*)\)$/\1/; s/%20/ /g' \
     | while IFS= read -r p; do [ -e "$p" ] || echo "BROKEN: $p"; done
   ```

   Every frontmatter `[[wikilink]]` relation target resolves to an existing file:

   ```bash
   grep -rhoE '\[\[[^]]+\]\]' --include='*.md' \
     "security principles" "design patterns" "architectural primitives" \
     | sed -E 's/\[\[(.*)\]\]/\1/' | sort -u \
     | while IFS= read -r id; do find . -name "$id.md" | grep -q . || echo "UNRESOLVED: [[$id]]"; done
   ```

   No forbidden verb is used as a relation key:

   ```bash
   grep -rnE '^(affects|uses|helps):' --include='*.md' . && echo "^ FORBIDDEN VERB" || true
   ```

## Style

- Markdown only. No HTML, no embedded diagrams, no images unless explicitly requested.
- Plain prose; no marketing tone. Definitions read as specification text, not as a blog post.
- Use the long-dash `—` (not `--`) consistent with existing files.
- Italics for term introductions (`*suborn*`); bold for enumerated property names in bullet lists (`**Output validation.**`).
- Quote model behavior in the third person: "the model", not "Claude" / "GPT". Prefer the general "model" over "LLM"; use "LLM" / "VLM" / "language model" only when a statement is specific to that model class (e.g. contrasting instruction-following models with classifiers or embedding models).

## Commits

- Commit messages should describe what changed in the documentation, not what was decided about the system.
- Do **not** add `Co-Authored-By` or generator attribution unless the user has asked for it for a specific commit. Project policy disables attribution globally.
- One commit per coherent change (e.g., "add hash-chained-logs definition", "rephrase trusted-path-logging brief"). Avoid bundling unrelated wording fixes with structural moves.

## What this repository is not

- Not a how-to guide. Definitions are normative descriptions, not tutorials.
- Not a code project. Do not add `package.json`, `Cargo.toml`, CI workflows, or test scaffolding.
- Not a place for opinions. If a claim is contested or aspirational, mark it as such or omit it.
