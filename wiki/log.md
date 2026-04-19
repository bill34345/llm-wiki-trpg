---
type: meta
title: "Wiki Log"
status: active
created: 2026-04-17
updated: 2026-04-19
tags: [wiki, log]
---

# Wiki Log

## 2026-04-19 | wiki-ingest-hq-auto verified clean focused lint surface | 第3章：巴佐赞
- 对 `.raw/第3章_巴佐赞.md` 的既有 raw-only ingest 面执行真实 focused lint，并生成 `lint-report-2026-04-19-focused-chapter-3`
- first-pass 深化补出 5 个高频 standalone canonical 节点：`神话共鸣`、`献祭引擎`、`幽暗潜猎兽出逃`、`可能性之尘`、`托罗格之饥饿诅咒`；并将其接回第3章 source / chapter / 角色表 / 地点表 / 任务表、`巴佐赞调查`、`探索叛神殿`、`巴佐赞`、`待命室`、`叛神殿`、`永志不忘墙`、`切询` 与 `凯林·泰拉林`
- focused lint 发现 1 项 recency 元数据警告：12 个实际 touched 页的 frontmatter `updated` 仍停留在 `2026-04-18`
- repair pass 将上述 touched 页 `updated` 统一刷新为 `2026-04-19`
- 对同一 Chapter 3 focused scope 执行第二次 focused lint，生成 `lint-report-2026-04-19-focused-chapter-3-recheck`；本次 re-check 未再发现新的 critical / warning / suggestion 级问题

## 2026-04-19 | wiki-ingest-hq-auto verified clean focused lint surface | 第2章：启程出发
- 对 `.raw/第2章_启程出发.md` 的既有 raw-only ingest 面执行真实 focused lint，并生成 `lint-report-2026-04-19-focused-chapter-2`
- focused lint 发现 1 项 provenance 陈旧警告与 1 项 canonical 接线建议：`巴佐赞` 虽已作为第2章终点节点参与 chapter/view/source 阅读层，但 `source_refs` 尚未记入 `.raw/第2章_启程出发.md`；`路边劫匪` 面的 `波斯特拉克/六把刀` 仍停留在纯文本层
- repair pass 将 `波斯特拉克` 接回 `第2章-启程出发` 与 `乔哈斯旅途遭遇`，并为 `巴佐赞` 补记 Chapter 2 source provenance、刷新 touched 页 `updated` 日期
- 对同一 Chapter 2 focused scope 执行第二次 focused lint，生成 `lint-report-2026-04-19-focused-chapter-2-recheck`；本次 re-check 未再发现新的 critical / warning / suggestion 级问题

## 2026-04-19 | wiki-ingest-hq-auto completed after focused lint repair | 第1章：命运之争
- 对 `.raw/第1章_命运之争.md` 的既有 raw-only ingest 面执行真实 focused lint，并生成 `lint-report-2026-04-19-focused-chapter-1`
- focused lint 发现 2 项结构性问题与 1 项补页建议：第1章角色表中的吉高关键 NPC 仍为纯文本且缺 standalone page、第1章入口仍回跳 legacy 页、`翡翠之眼` 虽高频出现但尚无 canonical item page
- repair pass 补建 `翡翠之眼`、`德思·米莉姆`、`科尔布·卡兹长老`、`阿加西·银勺`、`欧莫`、`玛丽尔·棕牙`、`阿丹`，把第1章 source / cast / finale / grotto 接回这些 canonical 页，并移除第1章入口中的 legacy 内容入口
- 对同一 Chapter 1 focused scope 执行第二次 focused lint，生成 `lint-report-2026-04-19-focused-chapter-1-recheck`；本次 re-check 未再发现新的 critical / warning / suggestion 级问题

## 2026-04-18 | wiki-ingest-hq-auto completed after focused lint repair | 附录D：痛苦碎片
- 对 `.raw/附录D_痛苦碎片.md` 完成首轮 raw-only 高保真 ingest，补出 `附录D-痛苦碎片` source 页与九块痛苦碎片的 standalone 规则页，并把 `痛苦碎片` 总页升级为规则总枢纽
- 使用本地 `/wiki-lint` 兼容入口对附录D ingest 面执行真实 focused lint，并生成 `lint-report-2026-04-18-focused-appendix-d`
- focused lint 发现 1 项 source 页覆盖表述过满警告与 1 项第6章地理回链偏弱建议；repair pass 改写“当前 raw 可稳定辨认”口径，并把 `悔恨洞窟`、`愤怒孔穴`、`渴望深谷` 接回对应碎片页
- 对同一 Appendix D focused scope 执行第二次 focused lint，生成 `lint-report-2026-04-18-focused-appendix-d-recheck`；本次 re-check 未再发现新的 critical / warning / suggestion 级问题

## 2026-04-18 | wiki-ingest-hq-auto verified clean focused lint surface | 附录C：善行奖章
- 对 `.raw/附录C_善行奖章.md` 的既有 ingest 面补做本地 `/wiki-lint` focused lint 与 focused re-check，覆盖 `附录C-善行奖章` source、`善行奖章` 总概念页、七枚功业节奖章页，以及 `功业节` / `第1章` 等直接接线页
- 本次 focused lint 结果为 0 issue，并补写 `lint-report-2026-04-18-focused-appendix-c`
- 同一 focused scope 的 second pass re-check 结果同样为 0 issue，并补写 `lint-report-2026-04-18-focused-appendix-c-recheck`

## 2026-04-18 | wiki-ingest-hq-auto completed after focused lint repair | 第7章：绝望之心
- 对 `.raw/第7章_绝望之心.md` 完成首轮 raw-only 高保真 ingest，补出 `第7章-绝望之心` source 页、第7章角色/地点视图、`绝望之心`、`情感治疗`，以及 `受难者阿利克辛`、`无情者阿利克辛`、`一无所有者阿利克辛`、`无罪者阿利克辛` 等终局核心 canonical 页
- 使用本地 `/wiki-lint` 兼容入口对第7章 ingest 面执行真实 focused lint，并生成 `lint-report-2026-04-18-focused-chapter-7`
- focused lint 发现 1 项场地规则表述易误导问题与 2 项高频终局节点缺 standalone page 的建议项；repair pass 去除误导性 `三祷之坠` 链接，补建 `绝望之心祈祷遗址与巢穴动作`、`阿利克辛的三种结局`，并刷新第7章 chapter / location / source 接线
- 对同一 Chapter 7 focused scope 执行第二次 focused lint，生成 `lint-report-2026-04-18-focused-chapter-7-recheck`；本次 re-check 未再发现新的 critical / warning / suggestion 级问题

## 2026-04-18 | wiki-ingest-hq-auto completed after focused lint repair | 第6章：溟渊
- 对 `.raw/第6章_溟渊.md` 完成首轮 raw-only 高保真 ingest，补出 `第6章-溟渊` source 页、第6章角色/地点视图、`悔恨洞窟`、`愤怒孔穴`、`渴望深谷`，以及 `痛苦碎片`、`茹蒂斯的诅咒`、`希奥`、`猎手阿利克辛` 等核心 canonical 页
- 使用本地 `/wiki-lint` 兼容入口对第6章 ingest 面执行真实 focused lint，并生成 `lint-report-2026-04-18-focused-chapter-6`
- focused lint 发现 1 项导航陈旧问题与 2 项高频节点缺 standalone page 的建议项；repair pass 补建 `绝望之壳`、`近神者之矛`，并刷新 domain `_index` 与第6章导航接线
- 对同一 Chapter 6 focused scope 执行第二次 focused lint，生成 `lint-report-2026-04-18-focused-chapter-6-recheck`；本次 re-check 未再发现新的 critical / warning / suggestion 级问题

## 2026-04-18 | wiki-ingest-hq-auto completed after focused lint repair | 第5章：溺亡之城
- 基于既有首轮 raw-only 高保真 ingest 结果，使用本地 `/wiki-lint` 兼容入口对 `.raw/第5章_溺亡之城.md` 的 ingest 面执行真实 focused lint，并生成 `lint-report-2026-04-18-focused-chapter-5`
- focused lint 发现并修补 5 项记录层问题：为 `wiki/hot` 补齐缺失 frontmatter，纠正 domain `_index` 与 `overview` 中无法解析的 legacy corpus 入口，并将 `hot` / `log` 中“第5章 auto blocked”状态改写为已完成 focused lint repair 与 re-check 的当前状态
- 更新 `.raw/.manifest.json`，把第5章条目从 `blocked-before-focused-lint` 改为已完成 focused lint repair / re-check 的状态，并补记 focused lint report 页面
- 对同一 Chapter 5 focused scope 执行第二次 focused lint，生成 `lint-report-2026-04-18-focused-chapter-5-recheck`；本次 re-check 未再发现新的 critical / warning 级问题

## 2026-04-18 | wiki-ingest-hq-auto blocked after first-pass ingest | 第5章：溺亡之城
- 对 `.raw/第5章_溺亡之城.md` 完成首轮 raw-only 高保真 ingest，补出 source、chapter 视图、关键地点、关键 NPC 与第5章机制页
- 新建 source / view 页：`第5章-溺亡之城`、`第5章地点表`、`第5章角色表`
- 新建地点页：`联盟大本营`、`被淹没的酒馆`、`皇家图书馆大厅`、`至高之心神庙`、`海藻丛林`、`别墅`、`瞭望塔`、`溟渊裂隙`
- 新建人物页：`涂鸦`、`科索特`、`奥拉拉`、`哈达莱`、`贝尔崔斯`
- 新建机制页：`魔法屏障与基石`、`污染情绪`
- 更新 `第5章`、`凯尔-莫罗`、`全视联盟`、`红梦秘会`、`传送泥板`、`因赛特-阿奎尔`、`加莱奥卡达`、`阿利克辛` 与 `底栖魔鱼阿利克辛`
- 当时尝试继续执行 auto 所要求的 focused wiki lint，但在该时点尚未接通可调用的本地 focused lint 入口；此 blocked 状态已由上方完成条目接续修复

## 2026-04-18 | focused repair | 第4章后半段任务链
- 对 `.raw/第4章_希望明珠.md` 做小范围 focused repair，不重做整章，只补第4章后半段/跨章任务链
- 新建后半段与跨章任务事件页：`双面间谍`、`侦查裂隙`、`拿下溟渊`、`通往溟渊之钥`、`屠杀底栖魔鱼`、`月蚀矿垄断`、`大象骚乱`、`结交联盟`、`敌人之敌`、`摧毁溟渊`
- 补齐早期未拆的任务事件页：`我们中的幽灵`、`泽希尔的教徒`，使第4章三条派系线 18 个任务均有 canonical 事件页
- 更新 `第4章任务表`、`第4章` chapter entry、`quests/chapter-4` 与三条派系 arc，改为完整任务链导航
- 将关键任务链反向接入 `凯尔-莫罗`、`溟渊`、`初蚀`、`荒野母亲神庙`、`阿利克辛`、`加莱奥卡达`、`因赛特-阿奎尔`、`希拉`、`萨兹拉克-符文行者`、`洛林-奥菲达斯` 与 `月蚀武器`

## 2026-04-18 | focused lint repair | 第4章：希望明珠
- 对 `.raw/第4章_希望明珠.md` 的既有 wiki ingest 结果执行真实 focused lint，并修补主要 findings
- 新建任务事件页：`运送雕像`、`搜索生命穹顶`、`普罗里克斯的代理人`、`当运气流尽`、`房间里的大象`、`半熟计划`
- 新建高频 NPC 页：`瑞罗萨`、`乔尔-拉希德`、`卡利亚莱-克鲁根`、`老克鲁克`、`洛林-奥菲达斯`、`阿拉德琳`、`萨兹拉克-符文行者`、`希拉`、`内多西-阿奈`、`阿沙恩`、`立梅尔-威斯特`、`因赛特-阿奎尔`、`加莱奥卡达`
- 深化 `生命穹顶`、`幸运奔流`、`水晶城堡`、`骨园` 与 `异能塑像`，补入触发、DC、敌人、奖励与后果等运行信息
- 将 `quests/chapter-4` 与三条派系 arc 从 legacy 任务入口改为 wiki canonical 入口

## 2026-04-18 | wiki-ingest-hq-auto | 第4章：希望明珠
- 对 `.raw/第4章_希望明珠.md` 执行首轮 force ingest，建立 source / chapter / view / 地点 / 派系层；后续 focused lint 发现任务细节与 NPC standalone 页不足，已由上方 repair 条目补强
- 新建 source 页：`第4章-希望明珠`
- 新建 chapter 视图层：`第4章任务表`
- 新建地点页：`水晶城堡`、`特勒斯学堂`、`导师神庙`、`生命穹顶`、`凯尔-莫罗的无底洞`、`骨园`、`幸运奔流`
- 新建次要派系页：`欧德之手`、`刀疤会`、`记忆哨兵`、`面纱帮`
- 重写 `第4章` 入口、`安卡瑞尔`、`初蚀`、`荒野母亲神庙`、三大主派系页与四名核心 NPC 页
- 更新 domain `_index`、overview、hot cache 与 manifest

## 2026-04-18 | wiki-ingest-hq-auto | 附录C：善行奖章
- 对 `.raw/附录C_善行奖章.md` 执行自动 force ingest → focused lint → 修补 → 复检
- 新建 source 页：`附录C-善行奖章`
- 新建 canonical 概念页：`善行奖章`
- 深化七枚功业节奖章页，把“如何获得”“外观细节”“附录C 作为玩家卡片层的意义”接回 canonical 层
- 更新 `功业节`、第1章入口、domain `_index`、overview、hot cache 与 manifest

## 2026-04-18 | wiki-ingest-hq test | 附录A：生物
- 对 `.raw/附录A_生物.md` 执行 `wiki-ingest-hq` 真实 force ingest，把旧 manifest 占位转成 `wiki/` 层知识页
- 新建 source 页：`附录A-生物`
- 新建 canonical 结构页：`对手阶段`
- 新建怪物页：`底栖魔鱼阿利克辛`、`腐化巨鲨`、`死拥水母`、`幽暗潜猎兽`、`天背龟`、`野跃兽`、`剑魂`、`噬光鮟鱇`、`蛇口蛮蟹`、`血鳍蛇鳗`、`哀恸鱼集群`
- 更新 `对手小队` 与五名对手成员页，把 1/2/3 阶成长、月蚀装备与腐化代价接入角色层
- 更新 `钴魂书院`、`全视联盟`、`红梦秘会`，补出附录A提供的组织执行层模板含义
- 更新 DND overview、domain `_index`、第2/5/6/7章入口、hot cache 与 manifest

## 2026-04-18 | wiki-ingest-hq test | 附录B：魔法物品
- 对 `.raw/附录B_魔法物品.md` 执行 `wiki-ingest-hq` 首轮真实 force ingest，验证 HQ skill 不再只停留在 source 登记层
- 新建 source 页：`附录B-魔法物品`
- 新建 canonical 概念/机制页：`诀别遗物`、`月蚀物品`、`月蚀腐化`
- 新建主要物品页：`呼吸罩`、`传讯耳坠`、`传送泥板`、`赤红狂怒戒指`、`月蚀护甲`、`月蚀盾牌`、`月蚀武器`
- 新建功业节奖章页：`肌肉奖章`、`海螺奖章`、`龟背奖章`、`迷宫奖章`、`肉馅饼奖章`、`湿地奖章`、`智慧奖章`
- 深化 `三祷之坠` 的三阶段能力，使其可直接回答附录B中的具体规则问题
- 更新 DND overview、第4/5/6章入口与 hot cache，并完成新页链接自检

## 2026-04-18 | DND chapter 2 force-ingest (raw-only high-fidelity rewrite)
- 按用户新要求，不再依赖旧 `Dungeons & Dragons/...` 资料承载第2章结构与细节，改为仅以 `.raw/第2章_启程出发.md` 为主重写
- 重写 `wiki/sources/dnd/call-of-the-netherdeep/第2章-启程出发.md`、`前往巴佐赞.md`、`翠环之路休息站.md`，提升深度、颗粒度与 query 直接可答性
- 新增第2章细颗粒 canonical 页：`再遇对手`、`夜盗三祷之坠`、`乔哈斯旅途遭遇`、`棘刺荒野`
- 重写第2章 chapter/view 层，移除 chapter 入口中的 legacy 依赖，让 `wiki/` 自己承担可读导航
- 更新 DND 默认 ingest 记忆：未来章节 ingest 以 raw-only 独立生成 `wiki/` 内容为准

## 2026-04-18 | DND chapter 1 force-ingest (high-fidelity landing)
- 将 `.raw/第1章_命运之争.md` 落位到 `wiki/sources/dnd/call-of-the-netherdeep/第1章-命运之争.md`
- 新建第1章 canonical 页：`功业节`、`功业节总决赛`、`翡翠石窟`
- 新建对手五名成员实体页：艾优、德莫特、加萨利亚德、埃尔文、玛吉
- 新建第1章角色表与地点表，补齐 chapter-level 可读导航
- 更新 `对手小队`、`第1章` 入口与 domain `_index`，把前言 → 第1章链路接通

## 2026-04-17 | DND preface force-ingest (focused improvements)
- 基于定向 lint 结果，深化 `近神者` 与 `茹蒂斯迷信` 页，减少前言链路中的薄概念页
- 新增 `水下冒险规则` 机制页，将前言里的水下运行信息提升为可 query 的 canonical page
- 新增 `对手小队` 事件页，把前言中的长期镜像队伍机制从 source 摘要下沉为实体层知识
- 新增 `模组总时间线` 视图页，为前言中的远古层 / 现代层 / 冒险层建立总导航
- 更新前言 source 页、DND domain 入口与第1章入口，接入新的 canonical 页

## 2026-04-17 | DND preface force-ingest (high-fidelity rewrite)
- 将 `.raw/前言_AnsweringTheCall.md` 对应的 source 页从骨架摘要升级为高保真 canonical source
- 深化月蚀矿、阿利克辛、三祷之坠、吉高、巴佐赞、凯尔-莫罗、溟渊、灾祸之战、艾桑维亚、乔哈斯等页，使其可直接支撑 query
- 保留重要机制、外观、后果、阶段、叙事作用和 source-backed 细节，而不再只停留在概念锚点
- 校正一处月蚀矿相关链接，避免指向不存在的新页

## 2026-04-17 | DND preface force-ingest
- 将 `.raw/前言_AnsweringTheCall.md` 落位到 `wiki/sources/dnd/call-of-the-netherdeep/前言-Answering-the-Call.md`
- 提炼模组级核心概念页：近神者、灾祸之战、月蚀矿、茹蒂斯迷信
- 提炼模组级核心实体页：阿利克辛、三祷之坠、吉高、巴佐赞、凯尔-莫罗、溟渊、全视联盟、红梦秘会
- 更新 `wiki/domains/dnd/call-of-the-netherdeep/arcs/主线-近神者.md` 与第1/5/6/7章入口，使前言成为 module-wide query 入口
- 保持旧 `Dungeons & Dragons/...` 内容不动，继续作为 legacy corpus

## 2026-04-17 | DND chapter 4 entity landing (phase 1)
- 在 `wiki/entities` 下为第4章创建第一批实体页：安卡瑞尔、初蚀、荒野母亲神庙、异能塑像、弗瑞尔、依沃-扎拉雷、阿拉克里托斯、詹姆斯-克里昂
- 将 `wiki/domains/dnd/call-of-the-netherdeep/chapters/第4章.md` 指向新的实体入口
- 将第4章角色表、地点表改为混合模式：已落位实体走 `wiki/entities`，剩余内容暂时继续指向 legacy 页
- 保持旧 `Dungeons & Dragons/...` 内容不动，继续作为 canonical legacy corpus

## 2026-04-17 | DND wiki scaffold (phase 1)
- 建立 `/wiki` 作为 D&D 新知识层入口
- 新建 `wiki/sources/dnd/call-of-the-netherdeep/`
- 新建 `wiki/entities/*/dnd/call-of-the-netherdeep/`
- 新建 `wiki/domains/dnd/call-of-the-netherdeep/` 下的 chapters / arcs / quests / views / adaptation / run
- 保留旧 `Dungeons & Dragons/...` 内容不动，作为 legacy corpus
- 目标：先建立可读的章节/视图层，再逐步吸收旧内容
