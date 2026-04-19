---
type: meta
title: "Hot Cache"
status: active
created: 2026-04-17
updated: 2026-04-19T00:00:00
tags: [wiki, hot]
---

# Recent Context

## Last Updated
2026-04-19. `.raw/第3章_巴佐赞.md` 已完成 `wiki-ingest-hq-auto` focused lint 收尾：补出 `神话共鸣`、`献祭引擎`、`幽暗潜猎兽出逃`、`可能性之尘` 与 `托罗格之饥饿诅咒` 五个 standalone canonical 节点，并把它们接回 Chapter 3 source / chapter / view / town / dungeon 面；focused re-check 已完成，当前 Chapter 3 ingest surface 未发现新的 critical / warning / suggestion 级问题。

## Key Recent Facts
- 用户明确要求第2章起抛弃旧资料依赖，以 `.raw` 为主，在新的 `wiki/` 中独立生成内容。
- DND ingest 的默认标准现已进一步收紧：不仅要高精度、高细节、高保真，还要避免用旧资料补结构和颗粒度。
- 第4章现在三条派系线各 6 个任务均有 canonical 事件页；后半段任务保留第5章、第6章、第7章承接信息，但不替代后续章节完整 ingest。
- `wiki-ingest-hq-auto` 已收紧：后续 auto ingest 必须实际执行 focused lint、修补、二次 focused lint，不能用手工 Read/Grep 代替。
- 本地 `wiki-ingest-hq-auto` 现已通过项目内 `/wiki-lint` wrapper 正确接到 marketplace wiki-lint 语义，不再因 skill 暴露差异而误判 blocked。
- 附录D现已成为第6章痛苦碎片的规则层；遇到 raw 条文残缺时，canonical 页必须显式保留“当前转写缺口”，而不是补写缺失规则。
- 第1章现已补齐吉高高频 NPC 与 `翡翠之眼` 的 canonical 落位，后续如继续深化 Chapter 1，应优先围绕剩余高频微地点或比赛节点，而不是回退到 legacy 入口。


## Recent Changes
- Created focused lint reports for Chapter 3: `lint-report-2026-04-19-focused-chapter-3`, `lint-report-2026-04-19-focused-chapter-3-recheck`
- Completed Chapter 3 auto flow repair: `神话共鸣`, `献祭引擎`, `幽暗潜猎兽出逃`, `可能性之尘`, `托罗格之饥饿诅咒`
- Repaired Chapter 3 focused findings by refreshing touched-page `updated` dates across the Chapter 3 source / chapter / views / event / location / NPC surface
- Created focused lint reports for Chapter 2: `lint-report-2026-04-19-focused-chapter-2`, `lint-report-2026-04-19-focused-chapter-2-recheck`
- Repaired Chapter 2 focused findings by wiring `波斯特拉克` back into the Chapter 2 source / travel-encounter surface and adding `.raw/第2章_启程出发.md` to `巴佐赞` source provenance
- Created focused lint reports for Chapter 1: `lint-report-2026-04-19-focused-chapter-1`, `lint-report-2026-04-19-focused-chapter-1-recheck`
- Completed Chapter 1 auto flow repair: `翡翠之眼`, `德思·米莉姆`, `科尔布·卡兹长老`, `阿加西·银勺`, `欧莫`, `玛丽尔·棕牙`, `阿丹`
- Repaired Chapter 1 focused findings by removing legacy chapter-entry backjumps and rewiring Chapter 1 source / cast / finale / grotto pages to the new canonical nodes
- Created focused lint reports for Appendix D: `lint-report-2026-04-18-focused-appendix-d`, `lint-report-2026-04-18-focused-appendix-d-recheck`
- Completed Appendix D auto flow: `附录D-痛苦碎片`, `痛苦碎片`, `厌恶碎片`, `依恋碎片`, `消沉碎片`, `欺瞒碎片`, `执迷碎片`, `憎恨碎片`, `哀伤碎片`, `怜悯碎片`, `怨愤碎片`
- Repaired Appendix D focused findings by tightening source-page coverage claims and refreshing Chapter 6 region backlinks to the standalone fragment pages
- Created local compatibility skill: `wiki-lint`
- Created focused lint reports for Appendix C: `lint-report-2026-04-18-focused-appendix-c`, `lint-report-2026-04-18-focused-appendix-c-recheck`
- Verified Appendix C ingest surface stayed clean: `附录C-善行奖章`, `善行奖章`, 七枚功业节奖章页, `功业节`, `第1章`
- Created focused lint reports for Chapter 7: `lint-report-2026-04-18-focused-chapter-7`, `lint-report-2026-04-18-focused-chapter-7-recheck`
- Completed Chapter 7 auto flow: `第7章-绝望之心`, `第7章角色表`, `第7章地点表`, `绝望之心`, `情感治疗`, `受难者阿利克辛`, `无情者阿利克辛`, `一无所有者阿利克辛`, `无罪者阿利克辛`
- Repaired Chapter 7 focused findings by adding `绝望之心祈祷遗址与巢穴动作`, `阿利克辛的三种结局` and refreshing Chapter 7 navigation
- Created focused lint reports for Chapter 5: `lint-report-2026-04-18-focused-chapter-5`, `lint-report-2026-04-18-focused-chapter-5-recheck`
- Repaired Chapter 5 recency/index findings: `wiki/hot`, `wiki/log`, `Call of the Netherdeep/_index`, `overview`
- Completed Chapter 6 auto flow: `第6章-溟渊`, `第6章角色表`, `第6章地点表`, `悔恨洞窟`, `愤怒孔穴`, `渴望深谷`, `痛苦碎片`, `茹蒂斯的诅咒`, `希奥`, `猎手阿利克辛`
- Repaired Chapter 6 focused findings by adding `绝望之壳`, `近神者之矛` and refreshing `_index` / Chapter 6 navigation
- Created focused lint reports for Chapter 6: `lint-report-2026-04-18-focused-chapter-6`, `lint-report-2026-04-18-focused-chapter-6-recheck`

## Active Threads
- 逐步让 `wiki/` 完全成为 DND 的主阅读层与 query 层
- 后续 auto ingest 可直接复用本地 `/wiki-lint` focused 工作流
