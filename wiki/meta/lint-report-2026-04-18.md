## Summary
- Pages scanned: 19 scoped Chapter 3 pages + 5 immediate dependencies
- Issues found: 7 (1 critical, 3 medium, 3 minor)
- Audit type: focused post-repair validation for Call of the Netherdeep Chapter 3 ingest

## Critical (must fix)
1. Affected page: [[wiki/entities/events/dnd/call-of-the-netherdeep/探索叛神殿]]
   - Problem: The page compresses the dungeon too aggressively into thematic summary. It preserves why the dungeon matters, but not enough operational room/encounter detail for DM-ready use at the Chapter 3 graph level.
   - Suggested fix: Expand with a concise room/segment breakdown for the major traversal gates, named hazards, and what changes when the party has [[wiki/entities/items/dnd/call-of-the-netherdeep/三祷之坠]].

## Warnings (should fix)
1. Affected page: [[wiki/domains/dnd/call-of-the-netherdeep/views/quests-by-chapter/第3章任务表]]
   - Problem: Query-ready as a navigation stub, but too skeletal compared with the repaired entity set; it underserves DM lookup.
   - Suggested fix: Add one-line operational purpose for each event/location row.

2. Affected page: [[wiki/entities/items/dnd/call-of-the-netherdeep/鹰眼镜片]]
   - Problem: Valid and linked, but very thin and reads more like a loot note than a stable item entity.
   - Suggested fix: Add item function, why it was in the vrock corpse, and whether it matters beyond this scene.

3. Affected page group: Chapter 3 pages using plain-text mentions of core dependencies
   - Problem: Several pages mention 三祷之坠 / 阿利克辛 / 安卡瑞尔 / 全视联盟 / 红梦秘会 in prose without always linking the first mention.
   - Suggested fix: Normalize first-mention wikilinking per page for better graph traversal.

## Suggestions (worth considering)
1. Affected pages: [[wiki/entities/npcs/dnd/call-of-the-netherdeep/德瑞斯-德蒙纳]], [[wiki/entities/npcs/dnd/call-of-the-netherdeep/普丽玛-德蒙纳]], [[wiki/entities/npcs/dnd/call-of-the-netherdeep/雷纳德-阿勒顿]], [[wiki/entities/npcs/dnd/call-of-the-netherdeep/塞巴斯蒂安-阿勒顿]]
   - Problem: These are no longer unjustified, but they remain scene-support NPCs with modest standalone payload.
   - Suggested fix: Keep them if the design goal is high-fidelity DM support; otherwise later consider folding some details into location pages if maintenance burden grows.

2. Affected page: [[wiki/entities/locations/dnd/call-of-the-netherdeep/安卡瑞尔]]
   - Problem: Immediate dependency is consistent, but it still mixes new-style wiki links with one legacy-path link to 凯尔-莫罗.
   - Suggested fix: Normalize that legacy link to the current wiki entity path when convenient.

3. Affected page set: scoped Chapter 3 graph overall
   - Problem: The graph is strong on narrative significance, but a few pages still prioritize interpretation over table-facing procedure.
   - Suggested fix: Continue the repair standard used in 火葬场 / 关口军营 / 艾梵德拉祈祷地 for remaining high-pressure traversal content.
