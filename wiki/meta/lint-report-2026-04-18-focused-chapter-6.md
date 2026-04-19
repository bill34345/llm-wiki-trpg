---
type: meta
title: "Lint Report 2026-04-18"
created: 2026-04-18
updated: 2026-04-18
tags: [meta, lint, dnd, chapter-6]
status: developing
---

# Lint Report: 2026-04-18

## Scope
- Mode: focused
- Target: `.raw/dnd/call-of-the-netherdeep/chapters/第6章_溟渊.md` current ingest surface
- Pages scanned: 14

## Summary
- Issues found: 3
- Critical: 0
- Warnings: 1
- Suggestions: 2

## Critical
- None.

## Warnings
- [[wiki/domains/dnd/call-of-the-netherdeep/_index]]: `## Start Here` 仍未补入 `第5章入口`、`第6章入口` 与第5/6章视图入口；在本次已编辑导航页范围内属于 stale index entry。 Suggest: add Chapter 5/6 chapter links and Chapter 5/6 cast/location view links so the index reflects current ingest state.

## Suggestions
- [[wiki/entities/locations/dnd/call-of-the-netherdeep/溟渊]] / [[wiki/sources/dnd/call-of-the-netherdeep/第6章-溟渊]] / [[wiki/domains/dnd/call-of-the-netherdeep/views/locations-by-chapter/第6章地点表]]: `绝望之壳` 在 focused scope 中被多次提及，但仍只作为文本节点存在，没有 standalone canonical page。 Suggest: create `wiki/entities/locations/dnd/call-of-the-netherdeep/绝望之壳.md` and wire it into Chapter 6 navigation.
- [[wiki/entities/monsters/dnd/call-of-the-netherdeep/猎手阿利克辛]] / [[wiki/entities/npcs/dnd/call-of-the-netherdeep/希奥]] / [[wiki/entities/locations/dnd/call-of-the-netherdeep/愤怒孔穴]]: `近神者之矛` 在 focused scope 中被重复作为关键触发器引用，但仍无 standalone canonical page。 Suggest: create `wiki/entities/items/dnd/call-of-the-netherdeep/近神者之矛.md` and link it from the Chapter 6 source, location, and monster/NPC pages.
