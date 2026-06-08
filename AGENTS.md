# Agent Instructions

Guidance for AI agents and human contributors working in this repository.

## What this repository is

A reference framework for **agentic architecture**: the principles, patterns, primitives, and threats required to build agentic systems that are secure, reliable, and performant — including remaining secure under adversarial input and suborned models. Each concept declares the domain(s) it serves (`security`, `reliability`, `performance`) in its frontmatter; one concept may serve more than one. The content is documentation only — there is no executable code, no build, no test suite.

Authoritative entry points:

- [README.md](/README.md) — orientation.
- [architecture.md](/architecture.md) — the top-level map, linking the per-type index files. The agent taxonomy (the scope, computational-nature, and trust-position axes) lives in [primitives.md](/primitives.md), which links the per-primitive files under `primitives/`.

## Normative wording

Definitions in this repository are **normative**. They are cited from other components and design discussions and must remain stable.

- Do **not** paraphrase, summarize, or "improve the style" of an existing definition. Preserve wording byte-for-byte unless the change is explicitly requested.
- A definition's text lives in its own file under `principles/`, `patterns/`, `primitives/`, or `threats/`. The generated index table carries only a one-sentence brief — never duplicate the full definition there.
- The brief lives in the file's `brief` frontmatter field; the per-type index tables are generated from it. Never hand-edit those tables. If you change a definition, update `brief` in its file and regenerate (see "The index files are generated").
- Deviations from any principle in real systems require explicit justification; deviations from the wording of a principle in this repo require explicit user approval.

## File organization

```
/principles/                 # one file per principle (kebab-case)
/patterns/                   # one file per pattern
/primitives/                 # one file per primitive
/threats/                    # one file per threat / failure mode
/references/                 # pointer nodes to concepts defined in another KB
principles.md … references.md  # generated per-type index tables (one per concept type)
architecture.md              # top-level map linking the per-type index files
tools/gen-index.py           # regenerates the per-type index tables from frontmatter
.githooks/pre-commit         # blocks commits when an index file is stale or links break
.obsidian/                   # Obsidian vault config; Breadcrumbs pre-configured for the relation graph
README.md                    # repository overview
AGENTS.md                    # this file
```

Conventions:

- Folder and file names are lowercase and space-free; Markdown links use plain paths (e.g. `/patterns/foo.md`). No `%20` encoding is needed.
- One concept per file. Filename is kebab-case of the concept name (e.g. `least-privilege-principle.md`).
- Each definition file uses a single H1 matching the concept name. Subsections use H2 or bullet lists.

## Frontmatter and relations

Each definition file begins with YAML frontmatter carrying its metadata and its outgoing relations. Relations are machine-readable edges for graph/vector ingestion and for Obsidian relation plugins (Breadcrumbs, Graph Link Types). They live **only** in frontmatter; the prose body is unaffected and keeps its inline Markdown links.

```yaml
---
id: write-ahead-audit              # canonical node key; equals the filename stem
title: Write-ahead audit           # equals the H1, verbatim
type: principle | pattern | primitive | threat | reference   # equals the containing folder
domains: [security]                # one or more of: security, reliability, performance — list a domain ONLY where the body already makes that claim
status: draft | stable
brief: "One-sentence summary; source of the index row."
order: 5                           # position within its type group in the index
# outgoing relations: one top-level key per relation verb, wikilink-list values
implements: ["[[no-agency-without-auditability-principle]]"]
---
```

Rules:

- `brief` and `order` drive the generated per-type index tables (see "The index files are generated"). `brief` is the single source of the index row; `order` is the integer position within the type group.
- One top-level key per relation verb; the value is a YAML list of `[[wikilinks]]`, even for a single target. Each `[[target]]` is another file's `id` (its kebab filename stem); basenames are unique across the concept folders (`references/` included), so the bare stem resolves.
- Author the **forward** direction only. Inverse edges (`implemented_by`, `constrained_by`, …) are computed — by Breadcrumbs in Obsidian and by the ingestion loader — never written by hand. Single source of truth; no materialized back-references.
- A relation must reflect a claim the prose already makes. To add an edge the prose does not yet support, extend the prose (one sentence, in the definition's voice — see "Normative wording") rather than asserting an ungrounded edge.

Controlled verb vocabulary (forward forms only; use nothing else):

- **structural** — `implements`, `instantiates`, `extends`, `specializes`, `abstracts`, `decomposes_into`, `composes_with`
- **causal** — `enables`, `enhances`, `reduces`, `amplifies`, `stabilizes`, `simplifies`
- **constraint** — `requires`, `depends_on`, `constrains`, `limits`, `isolates`, `protects`, `mitigates`, `enforces`
- **trade-off** — `conflicts_with`, `trades_off_with`, `competes_with`, `weakens`
- **semantic** — `defines`, `describes`, `models`, `alias_of`, `related_to`
- **forbidden** — `affects`, `uses`, `helps`, "is related to" (too vague to be an edge)

Threats are the failure modes the other concepts defend against. The mitigation edge is authored **forward** as `mitigates` on the mitigating principle, pattern, or primitive (e.g. a pattern file lists `mitigates: ["[[confused-deputy-problem]]"]`); the threat file carries only the implied `mitigated_by` inverse, never written by hand. A more specific threat relates to a more general one with `specializes` (e.g. prompt-injection `specializes` confused-deputy-problem).

### Reference nodes (cross-knowledge-base seams)

Some concepts this framework depends on are defined in a *separate* knowledge base — cryptographic primitives, for instance, belong to cryptography engineering, which is kept as its own KB so this one can leave crypto implicit. Rather than import their content, the repository carries a thin **reference node** under `/references/` so that in-vault edges to them resolve and the graph does not dangle at the seam.

A reference node uses `type: reference` and carries `id`, `title`, `domains`, `status`, `brief`, and an `external_ref` field naming the owning KB and node id (e.g. `external_ref: "cryptography-engineering:merkle-tree"`). It is exempt from `order` (the generated `references.md` index sorts pointers by title) but otherwise appears in the index like any other type. It links out by name in prose only — never via a repo-absolute `/…` link — and carries no outgoing relation wikilinks: edges are authored **forward from the in-scope concept toward the reference** (e.g. `model-attestation` lists `requires: ["[[cryptographic-hash]]"]`), grounded in that concept's prose at the altitude of the capability it depends on, with the construction left to the external KB.

### Visualizing the graph in Obsidian (Breadcrumbs)

Relations are authored forward-only; the inverse edges are produced by the [Breadcrumbs](https://github.com/SkepticMystic/breadcrumbs) plugin's *implied relations*, so they never appear in any file. **Breadcrumbs is installed and pre-configured** in `.obsidian/plugins/breadcrumbs/` — open this repo as a vault and the graph works; no setup needed.

The committed config (`.obsidian/plugins/breadcrumbs/data.json`) registers every vocabulary verb and its inverse as an *edge field*, groups them by direction (forward verbs and their inverses in opposite `ups`/`downs` groups, symmetric verbs in `sames`), and adds one *transitive implied-relation* rule per pair (`chain: [forward] → close_field: inverse, close_reversed: true`). That rule is what makes e.g. `stochastic-agents` show `constrained_by ← local-mediation` without that edge being written anywhere. The Matrix and Tree side views display all groups.

If you change the vocabulary, mirror it in `data.json`: add the field to `edge_fields`, to the right `edge_field_groups` entry, and add a `transitive` rule for the pair (symmetric verbs also go in `self_is_sibling`). *(Optional)* Install **Dataview** + **Graph Link Types** to label edges in the native graph view.

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
| `mitigates` | `mitigated_by` | down |
| `enforces` | `enforced_by` | down |
| `weakens` | `weakened_by` | down |
| `defines` / `describes` / `models` | `defined_by` / `described_by` / `modeled_by` | up |
| `composes_with` | `composes_with` (self) | same |
| `conflicts_with` / `trades_off_with` / `competes_with` | self | same |
| `alias_of` / `related_to` | self | same |

## Adding a new principle, pattern, primitive, or threat

1. Create a file in the matching subdirectory with kebab-case name and H1 title.
2. Write the full normative definition; keep it focused on this one concept.
3. Add frontmatter: `id` (= filename stem), `title` (= H1, verbatim), `type` (= folder), `domains`, `status`, `brief` (one sentence), `order` (position in the type group). See "Frontmatter and relations".
4. Encode outgoing relations in frontmatter using the controlled vocabulary — one wikilink-list per verb, forward direction only, each grounded in the prose.
5. Regenerate the index: `python3 tools/gen-index.py`. The per-type index tables are generated from frontmatter — never hand-edit them; edit `brief`/`order` and regenerate.
6. If the new concept is referenced by other definitions, update those files to link to it.
7. Verify links and frontmatter (the pre-commit hook runs all of this; you can also run it by hand). Each prints only on failure; run from the repo root.

   The index is current with frontmatter:

   ```bash
   python3 tools/gen-index.py --check
   ```


   Body Markdown links resolve (paths are space-free):

   ```bash
   grep -rhoE '\]\(/[^)]+\)' --include='*.md' . \
     | sed -E 's/^\]\(\/(.*)\)$/\1/; s/%20/ /g' \
     | while IFS= read -r p; do [ -e "$p" ] || echo "BROKEN: $p"; done
   ```

   Every frontmatter `[[wikilink]]` relation target resolves to an existing file:

   ```bash
   grep -rhoE '\[\[[^]]+\]\]' --include='*.md' \
     "principles" "patterns" "primitives" "threats" "references" \
     | sed -E 's/\[\[(.*)\]\]/\1/' | sort -u \
     | while IFS= read -r id; do find . -name "$id.md" | grep -q . || echo "UNRESOLVED: [[$id]]"; done
   ```

   No forbidden verb is used as a relation key:

   ```bash
   grep -rnE '^(affects|uses|helps):' --include='*.md' . && echo "^ FORBIDDEN VERB" || true
   ```

## The index files are generated

The five per-type index files — `principles.md`, `patterns.md`, `primitives.md`, `threats.md`, `references.md` — are generated from definition frontmatter by `tools/gen-index.py`; in each, the table rows live between `<!-- gen:<type>:start -->` / `<!-- gen:<type>:end -->` markers. The prose around the tables is hand-written and preserved. Each row's name comes from `title` (a trailing ` (… axis)` annotation is stripped), its summary from `brief`, its position from `order` (references, which have no `order`, sort by title), and its link from the file path.

- Edit a brief or add/remove a concept → change frontmatter, then run `python3 tools/gen-index.py`.
- Never edit text between the `gen:` markers by hand; it is overwritten on the next run.
- `python3 tools/gen-index.py --check` exits non-zero if any index file is stale relative to frontmatter.

### Pre-commit hook

`.githooks/pre-commit` blocks a commit when an index file is stale (frontmatter changed but not regenerated), when a body link is broken, when a relation wikilink is unresolved, or when a forbidden verb is used. Activate it once per clone:

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
