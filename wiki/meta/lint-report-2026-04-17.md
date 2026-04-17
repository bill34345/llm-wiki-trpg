---
type: meta
title: "Lint Report 2026-04-17"
created: 2026-04-17
updated: 2026-04-17
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-04-17

## Summary
- Pages scanned: ~100 (Call-of-the-Netherdeep campaign + Exandria world)
- Issues found: 20
- Auto-fixed: 7 (from first round)
- Needs review: 13

## Orphan Pages

### Missing inbound links from other pages:
- [[守望者特拉斯特]]: referenced in [[记忆哨兵]] but no other page links to it. Consider linking from [[安卡瑞尔]]/locations or [[凯尔-莫罗]].
- [[守望者拜伦]]: same — referenced in [[记忆哨兵]] but isolated. Consider linking from [[记忆哨兵#拜伦]] section or [[安卡瑞尔]].
- [[立梅尔·威斯特]]: has dedicated page `立梅尔-威斯特.md` but wikilink `[[立梅尔·威斯特]]` in [[记忆哨兵]] may not resolve (hyphen vs space mismatch). **Fix: normalize wikilink to `[[立梅尔-威斯特]]`.**

### Standalone pages (intentionally isolated — for DM reference):
- [[蔚蓝宫]]: only linked from Sources/第4章-希望明珠 and 安卡瑞尔. Acceptable.
- [[月蚀魔象]]: only linked from Sources/第4章. Acceptable (creature reference).

## Dead Links

- `[[欧德之手]]` in [[洛林-奥菲达斯]] → file is `欧德之手.md` (exists). **Link resolves.**
- `[[萨兹拉克·符文行者]]` in [[希拉]] → file is `萨兹拉克-符文行者.md` (exists). **Link resolves.**
- `[[依沃·扎拉雷]]` in [[洛林-奥菲达斯]] → file is `依沃-扎拉雷.md` (exists). **Link resolves.**

**No dead links found in main content.** All referenced NPC/faction files exist.

## Missing Pages

~~三头犬密会~~ - **FIXED** ✓
- **隐秘巨蛇希泽尔**: deity referenced in [[洛林-奥菲达斯]] — no page. Low priority (patron deity of a cult).
- **芭丝/柯芙莱·琴弦**: Twin sister bandits at 黑市前哨站 (Lyrean Linen). Not created yet. Part of 黑市前哨站 location.
- **埃奇奥**: Parrot companion of 瑞罗萨. Low priority.

## Cross-Reference Gaps

| Mention | Page | Missing Link |
|---------|------|--------------|
| 荒野母亲神庙 | [[希拉]] | Not linked to [[安卡瑞尔]] location |
| 印记区 S7 | [[希拉]] | No link to [[安卡瑞尔]] |
| 卷轴凹室 S5 | [[洛林-奥菲达斯]] | No link to [[安卡瑞尔]] |
| 初蚀 | [[希拉]] | Should link to 红梦秘会 or [[弗瑞尔]] |
| 欧德之手 | [[洛林-奥菲达斯]] | Already links correctly |

## Thin Pages (Need Expansion)

| Page | Current State | Issue |
|------|--------------|-------|
| [[德思-米利姆]] | ~30 lines | Very brief — only alias info. Source has more detail? |
| [[阿加西-银勺]] | ~30 lines | Brief NPC from Ch1 |
| [[玛丽尔-棕牙]] | ~30 lines | Brief NPC from Ch1 |
| [[比特]] / [[扎格]] | ~20 lines each | Very brief洼路收割赛主持 |
| [[鹰眼]] | ~20 lines | Brief maze judge |

## Frontmatter Gaps

- [[德思-米利姆]]: missing `type: npc` — only has `aliases`.
- [[弗瑞尔]]: **has** `type: npc` ✓
- [[希拉]]: **has** `type: NPC` ✓
- [[洛林-奥菲达斯]]: **has** `type: NPC` ✓

## Stale Claims

No contradictions detected in this pass. Key pages ([[安卡瑞尔]], [[红梦秘会]], [[全视联盟]], [[钴魂书院]]) all consistently reference Chapter 4 source.

## Thin Source Summary Pages

| Page | Issue |
|------|-------|
| [[第4章-希望明珠]] | 600+ lines — too long. Should be split into: 派系任务详情, 安卡瑞尔探索, NPC互动 — or keep as-is (acceptable as DM reference). |
| [[第5章-溺亡之城]] | Only lists: 涂鸦, 因赛特·阿奎尔, 加莱奥卡达, 凯尔·莫罗. Missing full M1-M17 region breakdown. |
| [[第6章-溟渊]] | Only lists: 三个区域, 九块痛苦碎片. Missing N1-N26 detail. |

## Recommendations

### Priority 1 (Fix Now)
1. Normalize `[[立梅尔·威斯特]]` → `[[立梅尔-威斯特]]` in [[记忆哨兵]]
2. Add `type: npc` to [[德思-米利姆]]
3. Create stub for **三头犬密会** in [[洛林-奥菲达ς]] (or mark as "see 荒洲" reference)

### Priority 2 (Expand on Next Ingest)
4. Expand 德思-米利姆, 阿加西-银勺 if source has more detail
5. Split 第4章-希望明珠 into sub-pages if it grows beyond 800 lines

### Priority 3 (Low — DM Acceptable)
6. Add cross-links from [[希拉]] to [[安卡瑞尔]] locations
7. Expand Chapter 5/6 source summaries with region details (currently very thin)
