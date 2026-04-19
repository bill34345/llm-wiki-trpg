---
type: meta
title: "Lint Report 2026-04-18"
created: 2026-04-18
updated: 2026-04-18
tags: [meta, lint, dnd, chapter-7]
status: developing
---

# Lint Report: 2026-04-18

## Scope
- Mode: focused
- Target: `.raw/ingested/dnd/call-of-the-netherdeep/chapters/第7章_绝望之心.md` current ingest surface
- Pages scanned: 13

## Summary
- Issues found: 3
- Critical: 0
- Warnings: 1
- Suggestions: 2

## Critical
- None.

## Warnings
- [[wiki/sources/dnd/call-of-the-netherdeep/第7章-绝望之心]]: line describing all entrants gaining 1 hour of `[[wiki/entities/items/dnd/call-of-the-netherdeep/三祷之坠|水上行走式]]` effect risks misattributing an arena-wide Chapter 7 location rule to the item `三祷之坠`. Suggest: remove the item link there and describe the effect as an `绝望之心`场地规则, or land a standalone mechanic page for the encounter-wide water-walk rule.

## Suggestions
- [[wiki/entities/locations/dnd/call-of-the-netherdeep/绝望之心]]: H1 雕像、H2-H4 祈祷遗址与对应巢穴动作在 source / location / location-view 中反复出现，但目前没有 standalone canonical landing，导致 DM 查询“祈祷点怎么关巢穴动作”时仍要在多个页面拼接。 Suggest: create a small standalone canonical page for `绝望之心祈祷遗址与巢穴动作` or equivalent and wire it from `第7章-绝望之心`、`绝望之心`、`第7章地点表`.
- [[wiki/domains/dnd/call-of-the-netherdeep/chapters/第7章]]: worst / neutral / best ending consequences are spread across the Chapter 7 source, chapter page, `绝望之心`, `一无所有者阿利克辛`, and `无罪者阿利克辛`, but there is no standalone canonical ending landing. Suggest: create a focused end-state page such as `阿利克辛的三种结局` and back-link it from the Chapter 7 source, chapter page, `绝望之心`, and final-form pages.
