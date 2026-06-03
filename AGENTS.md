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
- A definition's text lives in its own file under `security principles/`, `design patterns/`, or `architectural primitives/`. The `architecture.md` table carries only a one-sentence brief — never duplicate the full definition there.
- The brief lives in the file's `brief` frontmatter field; the `architecture.md` tables are generated from it. Never hand-edit those tables. If you change a definition, update `brief` in its file and regenerate (see "The architecture.md index is generated").
- Deviations from any principle in real systems require explicit justification; deviations from the wording of a principle in this repo require explicit user approval.

## File organization

```
/security principles/        # one file per principle (kebab-case)
/design patterns/            # one file per pattern
/architectural primitives/   # one file per primitive
architecture.md              # index (generated tables) — see tools/gen-index.py
tools/gen-index.py           # regenerates the architecture.md tables from frontmatter
.githooks/pre-commit         # blocks commits when architecture.md is stale or links break
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
brief: "One-sentence summary; source of the architecture.md index row."
order: 5                           # position within its type group in the index
# outgoing relations: one top-level key per relation verb, wikilink-list values
implements: ["[[no-agency-without-auditability-principle]]"]
---
```

Rules:

- `brief` and `order` drive the generated `architecture.md` tables (see "The architecture.md index is generated"). `brief` is the single source of the index row; `order` is the integer position within the type group.
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

### Visualizing the graph in Obsidian (Breadcrumbs)

Relations are authored forward-only; the inverse edges are produced by the [Breadcrumbs](https://github.com/SkepticMystic/breadcrumbs) plugin's *implied relations*, so they never appear in any file. To set this up after opening the repo as an Obsidian vault:

1. Install **Breadcrumbs** (Community Plugins).
2. **Settings → Edge Fields**: create one field per forward verb in the vocabulary above, and one per inverse label in the table below.
3. **Settings → Edge Field Groups**: assign each forward verb and its inverse to *opposite* groups (the suggested `up`/`down` labels below are cosmetic — only the forward↔inverse pairing is load-bearing). Put symmetric relations in a single `same` group.
4. **Settings → Implied Relations**: enable the *opposite-direction* implication so every forward edge auto-implies its inverse. This is what makes e.g. `stochastic-agents` show `constrained_by ← local-mediation` without that edge being written anywhere.
5. *(Optional)* Install **Dataview** + **Graph Link Types** to render the relation verb as a label on each edge in the native graph view.

The forward → inverse pairing (also the table the ingestion loader uses to synthesize inverse edges, so the graph DB matches Breadcrumbs):

| Forward | Inverse | Suggested dir |
|---|---|---|
| `implements` | `implemented_by` | up |
| `instantiates` | `instantiated_by` | up |
| `extends` | `extended_by` | up |
| `specializes` | `generalizes` | up |
| `abstracts` | `abstracted_by` | down |
| `decomposes_into` | `component_of` | down |
| `enables` | `enabled_by` | up |
| `enhances` | `enhanced_by` | up |
| `reduces` | `reduced_by` | down |
| `amplifies` / `stabilizes` / `simplifies` | `amplified_by` / `stabilized_by` / `simplified_by` | up |
| `requires` | `required_by` | up |
| `depends_on` | `depended_on_by` | up |
| `constrains` | `constrained_by` | down |
| `limits` / `isolates` | `limited_by` / `isolated_by` | down |
| `protects` | `protected_by` | down |
| `enforces` | `enforced_by` | down |
| `weakens` | `weakened_by` | down |
| `defines` / `describes` / `models` | `defined_by` / `described_by` / `modeled_by` | up |
| `composes_with` | `composes_with` (self) | same |
| `conflicts_with` / `trades_off_with` / `competes_with` | self | same |
| `alias_of` / `related_to` | self | same |

## Adding a new principle, pattern, or primitive

1. Create a file in the matching subdirectory with kebab-case name and H1 title.
2. Write the full normative definition; keep it focused on this one concept.
3. Add frontmatter: `id` (= filename stem), `title` (= H1, verbatim), `type` (= folder), `domains`, `status`, `brief` (one sentence), `order` (position in the type group). See "Frontmatter and relations".
4. Encode outgoing relations in frontmatter using the controlled vocabulary — one wikilink-list per verb, forward direction only, each grounded in the prose.
5. Regenerate the index: `python3 tools/gen-index.py`. The `architecture.md` tables are generated from frontmatter — never hand-edit them; edit `brief`/`order` and regenerate.
6. If the new concept is referenced by other definitions, update those files to link to it.
7. Verify links and frontmatter (the pre-commit hook runs all of this; you can also run it by hand). Each prints only on failure; run from the repo root.

   The index is current with frontmatter:

   ```bash
   python3 tools/gen-index.py --check
   ```


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

## The architecture.md index is generated

The three tables in `architecture.md` are generated from definition frontmatter by `tools/gen-index.py`; the rows live between `<!-- gen:<type>:start -->` / `<!-- gen:<type>:end -->` markers. The prose around the tables is hand-written and preserved. Each row's name comes from `title` (a trailing ` (… axis)` annotation is stripped), its summary from `brief`, its position from `order`, and its link from the file path.

- Edit a brief or add/remove a concept → change frontmatter, then run `python3 tools/gen-index.py`.
- Never edit text between the `gen:` markers by hand; it is overwritten on the next run.
- `python3 tools/gen-index.py --check` exits non-zero if `architecture.md` is stale relative to frontmatter.

### Pre-commit hook

`.githooks/pre-commit` blocks a commit when `architecture.md` is stale (frontmatter changed but not regenerated), when a body link is broken, when a relation wikilink is unresolved, or when a forbidden verb is used. Activate it once per clone:

```bash
git config core.hooksPath .githooks
```

The hook is committed under `.githooks/` (so it is shared and reviewable); `core.hooksPath` points Git at it. To bypass in an emergency, `git commit --no-verify`.

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
- Not a code project. Do not add `package.json`, `Cargo.toml`, CI workflows, or test scaffolding. The only code permitted is documentation-maintenance tooling under `tools/` and `.githooks/` (currently the index generator and the pre-commit hook) — keep it minimal and dependency-light.
- Not a place for opinions. If a claim is contested or aspirational, mark it as such or omit it.
