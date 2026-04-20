---
type: meta
title: "Hot Cache"
status: active
created: 2026-04-17
updated: 2026-04-21T00:00:00
tags: [wiki, hot]
---

# Recent Context

## Last Updated
2026-04-21. 已完成 `.raw/ingested/dnd/call-of-the-netherdeep/prep-notes/再次进入凯尔·莫罗（备团笔记）.md` 的 HQ 备团 ingest：新建 source 页 `再次进入凯尔·莫罗：柯瑞隆神庙与三祷之坠解封`、run 事件弧 `再次进入凯尔·莫罗与三祷之坠解封` 与地点页 `柯瑞隆神庙`，并深化 `三祷之坠-战役状态`、`霍莉`、`杰德`、`底栖魔鱼阿利克辛`、`campaign-state`、`战役时间线总览` 与 `run/_index`；这份 source 现作为凯尔·莫罗再入、三祷之坠回收与柯瑞隆神庙场景战的 DM 查询入口。

## Key Recent Facts
- 用户明确要求第2章起抛弃旧资料依赖，以 `.raw` 为主，在新的 `wiki/` 中独立生成内容。
- DND ingest 的默认标准现已进一步收紧：不仅要高精度、高细节、高保真，还要避免用旧资料补结构和颗粒度。
- 第4章现在三条派系线各 6 个任务均有 canonical 事件页；后半段任务保留第5章、第6章、第7章承接信息，但不替代后续章节完整 ingest。
- `wiki-ingest-hq-auto` 已收紧：后续 auto ingest 必须实际执行 focused lint、修补、二次 focused lint，不能用手工 Read/Grep 代替。
- 本地 `wiki-ingest-hq-auto` 现已通过项目内 `/wiki-lint` wrapper 正确接到 marketplace wiki-lint 语义，不再因 skill 暴露差异而误判 blocked。
- 附录D现已成为第6章痛苦碎片的规则层；遇到 raw 条文残缺时，canonical 页必须显式保留“当前转写缺口”，而不是补写缺失规则。
- Final pre-archive parity audit found remaining DM-usable details in legacy `安卡瑞尔`, `第4章-希望明珠`, and `翡翠石窟`; those details have now been folded into canonical `wiki/` pages before archive.
- Old Netherdeep legacy campaign directory has been archived at `Dungeons & Dragons/campaigns/_archive/Call-of-the-Netherdeep-legacy-2026-04-19/`; current navigation should use `wiki/domains/dnd/call-of-the-netherdeep/_index` and `wiki/sources/`.
- `run/` 层现有结构入口为 `wiki/domains/dnd/call-of-the-netherdeep/run/_index.md`；后续 run-layer ingest 默认按 `truth/`、`timeline/`、`characters/`、`state/` 分级落位，避免再写回 `run/` 根目录。
- Campaign timeline focused lint repair has expanded dense run arcs into standalone `run/timeline/` pages: `审判之碗事件`, `花屋与地下势力`, `枯木镇与假九头蛇`, `提仕坦突入与至日决战`; recurring campaign NPCs now have `run/characters/` pages for `威尔比`, `达莉亚`, `希尔瓦娜`, `桑德尔`, `艾拉拉`, `艾尔敦`, and `莉莉娅·格拉汉姆`.

## Recent Changes
- Completed HQ ingest for `.raw/ingested/dnd/call-of-the-netherdeep/prep-notes/再次进入凯尔·莫罗（备团笔记）.md`: created `wiki/sources/dnd/call-of-the-netherdeep/再次进入凯尔·莫罗-柯瑞隆神庙与三祷之坠解封.md`, `wiki/domains/dnd/call-of-the-netherdeep/run/timeline/再次进入凯尔·莫罗与三祷之坠解封.md`, and `wiki/entities/locations/dnd/call-of-the-netherdeep/柯瑞隆神庙.md`; deepened `三祷之坠-战役状态`, `霍莉`, `杰德`, `底栖魔鱼阿利克辛`, `campaign-state`, `战役时间线总览`, and `run/_index`; updated `hot`, `log`, and manifest so this prep-note now lands as a reusable campaign-canon source surface for Cael Morrow re-entry, Jewel of Three Prayers recovery, and Corellon Temple encounter design.
- Completed HQ ingest for `.raw/ingested/dnd/call-of-the-netherdeep/prep-notes/2026.01.28.md`: created `wiki/sources/dnd/call-of-the-netherdeep/2026-01-28备团-安卡瑞尔沦陷与无底洞突入.md`, `wiki/domains/dnd/call-of-the-netherdeep/run/timeline/安卡瑞尔沦陷与无底洞突入.md`, `wiki/entities/items/dnd/call-of-the-netherdeep/对调胶囊.md`, and `wiki/entities/monsters/dnd/call-of-the-netherdeep/灾星使徒.md`; deepened `史蒂夫`, `霍莉`, `艾琳·博尔顿`, `campaign-state`, `战役时间线总览`, and `run/_index`; updated `hot`, `log`, and manifest so this prep-note now lands as a reusable campaign-canon source surface for Ank'Harel collapse, Maw insertion, and Cael Morrow re-entry.
- Completed HQ ingest for `.raw/ingested/dnd/call-of-the-netherdeep/prep-notes/2026.01.20备团.md`: created `wiki/sources/dnd/call-of-the-netherdeep/2026-01-20备团-提仕坦至日前夜与角色专属桥段.md`; added canonical/run pages `艾欧复启芯片`, `静滞气泡`, `静滞视界`, and `终局裁决`; deepened `Devexian`, `格拉多斯-02`, `托雷克`, `佩莉吉`, `提仕坦突入与至日决战`, `campaign-state`, and `run/_index`; updated `hot`, `log`, and manifest so this prep-note now lands as a reusable post-solstice campaign-canon source surface.
- Completed HQ ingest for `.raw/ingested/dnd/call-of-the-netherdeep/truth-items-mechanics/6_物品机制.md`: created `wiki/sources/dnd/call-of-the-netherdeep/物品与机制库.md`; added canonical/campaign item and concept pages `拉克桑信标`, `螺旋之核`, `提仕坦方尖碑`, `沙漏之书`, `佩罗之泪`, `林璇的玉佩`, `托雷克之战锤`, `潮汐透镜`, `蝎子王冠`, `因果纺锤`, `言语之力`, `秘迹魔法`, `记忆断层`, and `血魔法`; deepened `月蚀矿`, `月蚀腐化`, `拉克桑`, `阈限之石`, `面纱帮`, `普拉芬尼尔`, `舒马斯秘库`, `德沃萨宝库`, and `提仕坦遗迹`; updated module `_index`, `hot`, `log`, and manifest.
- Completed HQ ingest for `.raw/ingested/dnd/call-of-the-netherdeep/truth-factions-groups/5_组织群体.md`: created `wiki/sources/dnd/call-of-the-netherdeep/组织势力与特殊群体指南.md`; added canonical faction/group pages `深红圣约`, `曙光守卫`, `芬迪尔部族`, `祈愿者皮克精`, `茹迪斯之子`, `擢升者`, `艾欧人造人`, `提仕坦人`, `蛇人`, `艾欧瑞安猎手`, `星之子`, and `假九头蛇`; deepened `红梦秘会`, `全视联盟`, `钴魂书院`, `欧德之手`, `面纱帮`, `克灵王朝`, `对手小队`, `底栖魔鱼阿利克辛`, and `月刷丛林`; updated module `_index`, `hot`, `log`, and manifest.
- Completed HQ ingest for `.raw/ingested/dnd/call-of-the-netherdeep/truth-characters/3_重要角色.md`: created `wiki/sources/dnd/call-of-the-netherdeep/人物志与关系网.md` and new run character pages `哑女希拉`, `S.I.L.A.H.A.`, `Devexian`, `艾琳·博尔顿`, `兰斯洛特`, `莱拉·暮光之影`; deepened existing run character pages `杰德`, `托雷克`, `克罗登`, `摩达·尼特`, `格拉多斯-02`, `莉莉娅·格拉汉姆`, `霍莉`, `艾尔敦`, `塞琳娜`, `史蒂夫`; rewired `run/_index`, `hot`, `log`, and manifest.
- Repaired campaign timeline focused lint findings for `.raw/ingested/dnd/call-of-the-netherdeep/truth/2_时间线.md`: created `审判之碗事件`, `花屋与地下势力`, `枯木镇与假九头蛇`, `提仕坦突入与至日决战`, plus `威尔比`, `达莉亚`, `希尔瓦娜`, `桑德尔`, `艾拉拉`, `艾尔敦`, and `莉莉娅·格拉汉姆`; rewired source/timeline/state/run index backlinks; recheck report `lint-report-2026-04-20-focused-campaign-timeline-recheck` found 0 issues.
- Created campaign-canon root source and run truth surface for `.raw/ingested/dnd/call-of-the-netherdeep/truth/1_真相.md`: `战役真相-世界观底层与核心谜团`, `战役真相总览`, `茹迪斯与远地点天至日真相`, `茹迪斯之子与擢升者`, `月蚀矿与螺旋之核`, `提仕坦与言语之力`, `艾欧与拉克桑信标`, `溟渊真相`, `梦境理论与欧曼提斯`, `平行时空`, `三祷之坠-战役状态`
- Created focused lint reports for Chapter 3: `lint-report-2026-04-19-focused-chapter-3`, `lint-report-2026-04-19-focused-chapter-3-recheck`
- Completed Chapter 3 auto flow repair: `神话共鸣`, `献祭引擎`, `幽暗潜猎兽出逃`, `可能性之尘`, `托罗格之饥饿诅咒`
- Repaired Chapter 3 focused findings by refreshing touched-page `updated` dates across the Chapter 3 source / chapter / views / event / location / NPC surface
- Created focused lint reports for Chapter 2: `lint-report-2026-04-19-focused-chapter-2`, `lint-report-2026-04-19-focused-chapter-2-recheck`
- Repaired Chapter 2 focused findings by wiring `波斯特拉克` back into the Chapter 2 source / travel-encounter surface and adding `.raw/ingested/dnd/call-of-the-netherdeep/chapters/第2章_启程出发.md` to `巴佐赞` source provenance
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
