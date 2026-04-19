---
type: meta
title: "Lint Report 2026-04-18"
created: 2026-04-18
updated: 2026-04-18
tags: [meta, lint, dnd, chapter-5]
status: developing
---

# Lint Report: 2026-04-18

## Scope
- Mode: focused
- Target: `.raw/ingested/dnd/call-of-the-netherdeep/chapters/第5章_溺亡之城.md` ingest surface
- Pages scanned: 23

## Summary
- Issues found: 5
- Critical: 3
- Warnings: 2
- Suggestions: 0

## Critical
- [[wiki/hot]]: frontmatter missing required fields `status`, `created`, and `tags`. Suggest: add the missing meta fields so recency pages satisfy the same lint contract as the rest of `wiki/`.
- [[wiki/domains/dnd/call-of-the-netherdeep/_index]]: legacy corpus link `[[Dungeons & Dragons/campaigns/Call-of-the-Netherdeep]]` does not resolve to a concrete note. Suggest: point it to the actual legacy note path such as `[[Dungeons & Dragons/campaigns/Call-of-the-Netherdeep/index]]`, or replace it with a canonical `wiki/` destination.
- [[wiki/domains/dnd/call-of-the-netherdeep/overview]]: legacy corpus link `[[Dungeons & Dragons/campaigns/Call-of-the-Netherdeep]]` does not resolve to a concrete note. Suggest: use the actual legacy note path or replace it with a canonical `wiki/` destination.

## Warnings
- [[wiki/hot]]: the top Chapter 5 status still claims focused wiki lint had no executable entrypoint and that `wiki-ingest-hq-auto` remained blocked. That claim is now stale after the local `/wiki-lint` compatibility entrypoint was added and exercised. Suggest: rewrite the hot cache entry after the repair pass / second focused lint so it reflects the real state.
- [[wiki/log]]: the 2026-04-18 Chapter 5 entry records the run as blocked because no real focused lint entrypoint existed. That is now stale project history unless the entry is updated to distinguish “blocked at that time” from the current repaired workflow. Suggest: revise the entry after the Chapter 5 repair pass and second focused lint.

## Suggestions
- None in this focused pass.
