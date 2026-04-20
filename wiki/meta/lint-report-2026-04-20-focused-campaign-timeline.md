---
type: meta
title: "Lint Report 2026-04-20 Focused Campaign Timeline"
created: 2026-04-20
updated: 2026-04-20
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-04-20 Focused Campaign Timeline

## Scope
- Mode: focused
- Target: campaign-canon timeline ingest surface for `.raw/ingested/dnd/call-of-the-netherdeep/truth/2_时间线.md` after `run/` restructuring
- Pages scanned: 19

Scanned pages:
- [[wiki/sources/dnd/call-of-the-netherdeep/时间线与剧情流]]
- [[wiki/domains/dnd/call-of-the-netherdeep/run/timeline/战役时间线总览]]
- [[wiki/domains/dnd/call-of-the-netherdeep/run/characters/格莱姆]]
- [[wiki/domains/dnd/call-of-the-netherdeep/run/characters/瑟西]]
- [[wiki/domains/dnd/call-of-the-netherdeep/run/characters/格拉多斯-02]]
- [[wiki/domains/dnd/call-of-the-netherdeep/run/characters/史蒂夫]]
- [[wiki/domains/dnd/call-of-the-netherdeep/run/characters/无心]]
- [[wiki/domains/dnd/call-of-the-netherdeep/run/characters/阿塔甘]]
- [[wiki/domains/dnd/call-of-the-netherdeep/run/characters/克罗登]]
- [[wiki/domains/dnd/call-of-the-netherdeep/run/characters/特雷恩·铁眉]]
- [[wiki/domains/dnd/call-of-the-netherdeep/run/characters/V]]
- [[wiki/domains/dnd/call-of-the-netherdeep/run/truth/战役真相总览]]
- [[wiki/domains/dnd/call-of-the-netherdeep/run/state/campaign-state]]
- [[wiki/domains/dnd/call-of-the-netherdeep/run/state/三祷之坠-战役状态]]
- [[wiki/domains/dnd/call-of-the-netherdeep/run/_index]]
- [[wiki/domains/dnd/call-of-the-netherdeep/_index]]
- [[wiki/hot]]
- [[wiki/log]]
- `.raw/.manifest.json`

## Summary
- Issues found: 7
- Critical: 0
- Warnings: 3
- Suggestions: 4

## Critical
- None.

## Warnings
- [[wiki/domains/dnd/call-of-the-netherdeep/run/timeline/战役时间线总览]]: the timeline source is much denser than the current hub, and several high-frequency transition arcs remain compressed into one-line bullets. The biggest query gaps are the Ankh'Harel investigation chain, Bowl of Judgment crisis, flower-shop collapse, Feywild sequence, and final Tishtan assault. Suggest: split the long chronology into several linked event-arc pages under `run/timeline/` so future queries can answer “what happened in this arc” without returning to raw.
- [[wiki/domains/dnd/call-of-the-netherdeep/run/timeline/战役时间线总览]]: recurring campaign-only NPCs from the raw timeline are still unlinked plain text despite repeated or structurally important appearances, especially `威尔比`, `达莉亚`, `希尔瓦娜`, `桑德尔`, `艾拉拉`, `艾尔敦`, and `莉莉娅·格拉汉姆`. Suggest: create `run/characters/` pages or explicitly fold them into existing pages with aliases/backlinks if they are not meant to stand alone.
- [[wiki/domains/dnd/call-of-the-netherdeep/run/state/三祷之坠-战役状态]]: the artifact state page captures the major transfers, but it still compresses the enemy-side retrieval phase after `杰德`'s death into a short paragraph. The raw timeline has enough detail around `威尔比`, `达莉亚`, and the “坠饰不在队伍手中” realization to support a clearer state transition. Suggest: expand the “第二次脱手” section or create a linked event page for the post-Jade pursuit of the pendant.

## Suggestions
- [[审判之碗事件]]: the raw timeline contains a full campaign-specific arc around `希尔瓦娜`, `深红圣约`, the Red Dream attack, `达莉亚`, the arena lockdown, and the party drinking Alyxian's blood, but the wiki surface currently only summarizes it. Suggest: add a `run/timeline/审判之碗事件.md` page and link it from [[wiki/domains/dnd/call-of-the-netherdeep/run/timeline/战役时间线总览]] and [[wiki/sources/dnd/call-of-the-netherdeep/时间线与剧情流]].
- [[花屋与地下势力]]: `花屋` appears as a major Ankh'Harel information hub and later collapse point, with `无心`, the twin assassins, kidnapping commissions, and long-term party cooperation attached to it. Suggest: add a `run/timeline/花屋与地下势力.md` or `run/truth/花屋与地下势力.md` page depending on whether it should be treated as event flow or faction/location truth.
- [[枯木镇与假九头蛇]]: the timeline source repeatedly uses 枯木镇 / 假九头蛇 as the point where Story A and Story B become player-facing, but the focused surface keeps this mostly inside 格莱姆/瑟西 and one timeline bullet. Suggest: create a dedicated `run/timeline/枯木镇与假九头蛇.md` page linking 格莱姆, 瑟西, 霍莉, 桑德尔, 欧曼提斯, and 平行时空.
- [[舒马斯秘库与提仕坦突入]]: the final assault has multiple reusable objects and revelations (`沙漏之书`, `舒马斯秘库`, `伊阿修特`, `阈限之石`, `言语之力`, `螺旋之核同调室`, `遗世间`) that are currently only lightly summarized. Suggest: create a `run/timeline/提仕坦突入与至日决战.md` page, and decide whether the key items should be standalone `run/state/` or official/campaign item pages.

## Notes
- No missing required frontmatter fields were found in the focused scope.
- No dead Obsidian links were found in the focused scope.
- The `run/` restructuring itself is consistent: scoped links now point to `run/truth/`, `run/timeline/`, `run/characters/`, or `run/state/`, and `.raw/.manifest.json` uses the new paths.
- This report is intentionally report-only and does not apply fixes.
