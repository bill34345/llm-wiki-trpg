---
type: meta
title: "Wiki Log"
status: active
created: 2026-04-17
updated: 2026-04-17
tags: [wiki, log]
---

# Wiki Log

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
- 目标：先建立可读的章节/视图/任务层，再逐步吸收旧内容
