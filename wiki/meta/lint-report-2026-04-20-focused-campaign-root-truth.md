---
type: meta
title: "Lint Report 2026-04-20"
created: 2026-04-20
updated: 2026-04-20
tags: [meta, lint, dnd, call-of-the-netherdeep, campaign-truth]
status: developing
---

# Lint Report: 2026-04-20

## Scope
- Mode: focused
- Target: `.raw/ingested/dnd/call-of-the-netherdeep/truth/1_真相.md` campaign-canon root ingest surface
- Pages scanned: 14

## Summary
- Issues found: 2
- Critical: 0
- Warnings: 1
- Suggestions: 1

## Critical
- None.

## Warnings
- [[wiki/concepts/lore/dnd/call-of-the-netherdeep/茹蒂斯迷信]], [[wiki/concepts/lore/dnd/call-of-the-netherdeep/月蚀矿]], [[wiki/entities/locations/dnd/call-of-the-netherdeep/溟渊]], [[wiki/entities/items/dnd/call-of-the-netherdeep/三祷之坠]], [[wiki/entities/npcs/dnd/call-of-the-netherdeep/阿利克辛]]: the new campaign-truth ingest surface links outward to official canon pages, but the official pages do not yet link back to the corresponding campaign run truth pages. This leaves the official ↔ campaign relationship only partially bidirectional inside the real module surface. Suggest: add explicit backlinks or contradiction-entry callouts from each official page to its campaign counterpart so readers can traverse both layers in either direction.

## Suggestions
- [[wiki/domains/dnd/call-of-the-netherdeep/run/truth/茹迪斯之子与擢升者]], [[wiki/domains/dnd/call-of-the-netherdeep/run/truth/月蚀矿与螺旋之核]], [[wiki/domains/dnd/call-of-the-netherdeep/run/truth/提仕坦与言语之力]], [[wiki/domains/dnd/call-of-the-netherdeep/run/truth/艾欧与拉克桑信标]], [[wiki/domains/dnd/call-of-the-netherdeep/run/truth/平行时空]], [[wiki/domains/dnd/call-of-the-netherdeep/run/truth/梦境理论与欧曼提斯]]: several campaign-specific entities are now repeatedly referenced across the root truth surface without standalone campaign pages yet, especially `霍莉`, `凯瑟琳`, `杰德`, `摩达·尼特`, `托雷克`, and `塞琳娜`. The current root pages remain queryable, but these names are becoming reusable knowledge nodes rather than one-off mentions. Suggest: backfill standalone campaign pages for the highest-frequency characters in later ingest passes and wire them back into the run truth surface.
