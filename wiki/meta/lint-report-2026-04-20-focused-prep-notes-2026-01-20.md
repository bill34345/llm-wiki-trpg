---
type: meta
title: "Lint Report 2026-04-20"
created: 2026-04-20
updated: 2026-04-20
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-04-20

## Scope
- Mode: focused
- Target: prep-notes ingest surface for `.raw/ingested/dnd/call-of-the-netherdeep/prep-notes/2026.01.20备团.md`
- Pages scanned: 15

## Summary
- Issues found: 2
- Critical: 0
- Warnings: 2
- Suggestions: 0

## Critical
- None.

## Warnings
- [[wiki/entities/npcs/dnd/call-of-the-netherdeep/佩莉吉]]: page was materially deepened in this ingest pass, but frontmatter `updated` still remains `2026-04-19`. Suggest: refresh `updated` to `2026-04-20` so recency metadata matches the actual prep-note repair surface.
- [[wiki/entities/npcs/dnd/call-of-the-netherdeep/佩莉吉]]: page currently contains two separate `## 关联` sections, leaving stale duplicated navigation at the tail. Suggest: merge into a single `## 关联` section and keep the expanded cross-links added by this ingest.

## Suggestions
- None.
