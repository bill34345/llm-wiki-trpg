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
- Target: truth-locations ingest surface for `.raw/ingested/dnd/call-of-the-netherdeep/truth-locations/4_地点区域.md`
- Pages scanned: 29

## Summary
- Issues found: 2
- Critical: 1
- Warnings: 1
- Suggestions: 0

## Critical
- [[wiki/entities/locations/dnd/call-of-the-netherdeep/艾欧]]: dead link to `[[wiki/domains/dnd/call-of-the-netherdeep/run/characters/S.I.L.A.H.A.]]`. The actual existing page is `[[wiki/domains/dnd/call-of-the-netherdeep/run/characters/S.I.L.A.H.A.]]` with a filename `S.I.L.A.H.A..md`, so the current wikilink does not resolve in this vault. Suggest: repoint the link to the exact existing page target or normalize the target page filename/link pair so the reference resolves consistently.

## Warnings
- [[wiki/entities/locations/dnd/call-of-the-netherdeep/审判之碗]], [[wiki/entities/locations/dnd/call-of-the-netherdeep/花屋]], [[wiki/entities/locations/dnd/call-of-the-netherdeep/枯木镇]], [[wiki/entities/locations/dnd/call-of-the-netherdeep/德沃萨宝库]], [[wiki/entities/locations/dnd/call-of-the-netherdeep/鲁梅丹沙漠]], [[wiki/entities/locations/dnd/call-of-the-netherdeep/沙虫腹中]], [[wiki/entities/locations/dnd/call-of-the-netherdeep/舒马斯秘库]], [[wiki/entities/locations/dnd/call-of-the-netherdeep/提仕坦遗迹]], [[wiki/entities/locations/dnd/call-of-the-netherdeep/鱼人村落]], [[wiki/entities/locations/dnd/call-of-the-netherdeep/普拉芬尼尔]], [[wiki/entities/locations/dnd/call-of-the-netherdeep/月刷丛林]], [[wiki/entities/locations/dnd/call-of-the-netherdeep/暗影沼泽]], [[wiki/entities/locations/dnd/call-of-the-netherdeep/艾欧]]: these newly created location pages currently have no backlinks from pages outside this ingest surface. Inside the focused scope they are wired correctly through the source page, chapter views, and related-location links, but they are still isolated from the wider vault. Suggest: add targeted backlinks from relevant run timeline / truth / character / faction pages that already rely on these places, so these nodes become discoverable outside the ingest bundle.

## Suggestions
- None.
