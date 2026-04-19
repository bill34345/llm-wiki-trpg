---
type: meta
title: "Lint Report 2026-04-19"
created: 2026-04-19
updated: 2026-04-19
tags: [meta, lint, dnd, chapter-2]
status: developing
---

# Lint Report: 2026-04-19

## Scope
- Mode: focused
- Target: `.raw/dnd/call-of-the-netherdeep/chapters/第2章_启程出发.md` current ingest surface
- Pages scanned: 23

## Summary
- Issues found: 2
- Critical: 0
- Warnings: 1
- Suggestions: 1

## Critical
- None.

## Warnings
- [[wiki/entities/locations/dnd/call-of-the-netherdeep/巴佐赞]]: this page is part of the Chapter 2 ingest surface and is presented in the Chapter 2 source/chapter/view layers as the chapter terminus, but its frontmatter `source_refs` still only cites `.raw/dnd/call-of-the-netherdeep/preface/前言_AnsweringTheCall.md` and `.raw/dnd/call-of-the-netherdeep/chapters/第3章_巴佐赞.md`. This leaves the page's provenance stale relative to the current Chapter 2 ingest surface. Suggest: add `.raw/dnd/call-of-the-netherdeep/chapters/第2章_启程出发.md` to `source_refs`, and make sure the page text clearly preserves its Chapter 2 gate/endpoint role.

## Warnings
- None.

## Suggestions
- [[wiki/sources/dnd/call-of-the-netherdeep/第2章-启程出发]] and [[wiki/entities/events/dnd/call-of-the-netherdeep/乔哈斯旅途遭遇]]: the Chapter 2 road-bandit node is still referenced only as plain text (`六把刀`, `波斯特拉克`) inside the ingest surface, even though [[wiki/entities/npcs/dnd/call-of-the-netherdeep/波斯特拉克]] already exists as the standalone canonical page. Suggest: wire the source/event mentions to the canonical NPC page so the Chapter 2 travel-threat layer no longer leaves this reusable human-threat node implicit.
