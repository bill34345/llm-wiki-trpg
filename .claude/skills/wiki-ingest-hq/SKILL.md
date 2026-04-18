---
name: wiki-ingest-hq
description: High-fidelity ingest into an Obsidian LLM wiki. Use whenever the user asks to ingest, force ingest, re-ingest, process a source, improve ingest quality, or build query-ready wiki pages from `.raw/` files, URLs, images, or batches—especially when the user wants higher detail, stronger cross-linking, or better human+AI usability than the default wiki-ingest flow.
---

# wiki-ingest-hq

Use this skill when the user wants ingest quality to be the priority.

This skill keeps the original LLM wiki model:
- `.raw/` = immutable source layer
- `wiki/` = durable knowledge layer
- ingest = update the knowledge graph, not just summarize a source

This skill is stricter than a generic ingest flow. It inherits the default wiki-ingest operational loop, but adds hard quality gates so pages become query-ready for both humans and AI.

## Core operating rule

Do not treat page creation as success. A page is only complete when it can directly answer the important questions a future reader will ask without falling back to `.raw/` for all substance.

## When to read bundled references

- Read `references/default-skill-strengths.md` before editing the workflow, so you preserve the good parts inherited from the default skill.
- Read `references/hard-rules.md` for the mandatory HQ quality gates.
- Read `references/workflow.md` every time you perform ingest.
- Read `references/query-readiness.md` before deciding an ingest is complete.
- Read `references/domain-adapters/dnd.md` whenever the source is DND or tabletop-module content.

## Workflow

1. Identify the source type: file, URL, image, or batch.
2. Apply delta tracking unless the user explicitly says force ingest or re-ingest.
3. Read the source completely. Do not skim.
4. Build a source-backed map of entities, events, locations, items, factions, concepts, and likely user queries.
5. Create or update the source summary in `wiki/sources/`.
6. Create or update canonical knowledge pages in `wiki/`.
7. Backfill missing dependency pages created by new links.
8. Update navigation and recency layers: `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`, relevant `_index.md` pages, and `wiki/overview.md` if needed.
9. Run the query-readiness review before declaring success.
10. If the new source contradicts existing pages, add bidirectional contradiction callouts instead of silently overwriting claims.
11. Update `.raw/.manifest.json` with the ingest result unless this was impossible for a concrete reason.

## Quality gates

You must enforce all of the following:

- Do not leave key pages as skeletons.
- Do not leave key entities linked but nonexistent.
- Do not compress operationally important scenes into vague chapter summaries.
- Do not keep crucial details only in the source summary if they belong on canonical pages.
- Do not sacrifice important source detail just to keep pages short.
- Do not silently overwrite contradictions.

## DND / module-specific note

For DND content, chapter summaries are not enough. Important NPCs, locations, items, monsters, factions, and events need standalone pages when they carry reusable knowledge. Important scenes must preserve triggers, structure, consequences, and relationships strongly enough for DM-style querying.

## Output expectations

When reporting back to the user after ingest, include:
- what source was ingested
- key pages created
- key pages updated
- any important dependency backfills
- any unresolved contradictions or thin spots that still need follow-up

## Test prompts

See `evals/evals.json` for starter prompts that can be used to evaluate whether this skill is actually producing higher-fidelity ingest than a generic flow.
