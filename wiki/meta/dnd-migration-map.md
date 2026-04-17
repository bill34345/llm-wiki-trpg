---
type: meta
title: "DND Migration Map"
status: active
created: 2026-04-17
updated: 2026-04-17
tags: [wiki, dnd, migration, meta]
---

# DND Migration Map

## 迁移原则
- 先建立 `wiki/` 下的可读入口与视图层
- 旧 `Dungeons & Dragons/...` 内容暂不搬动
- 后续逐步把稳定内容吸收到 `wiki/entities` / `wiki/sources` / `wiki/domains`

## 目录映射
- `Dungeons & Dragons/campaigns/Call-of-the-Netherdeep/Sources/` → `wiki/sources/dnd/call-of-the-netherdeep/`
- `.../NPCs/` → `wiki/entities/npcs/dnd/call-of-the-netherdeep/`
- `.../Locations/` → `wiki/entities/locations/dnd/call-of-the-netherdeep/`
- `.../Items/` → `wiki/entities/items/dnd/call-of-the-netherdeep/`
- `.../Monsters/` → `wiki/entities/monsters/dnd/call-of-the-netherdeep/`
- `.../Quests/` → `wiki/domains/dnd/call-of-the-netherdeep/quests/`
- `.../Plots/` → `wiki/domains/dnd/call-of-the-netherdeep/arcs/`
- DM 运行内容 → `wiki/domains/dnd/call-of-the-netherdeep/run/`
- 用户改编内容 → `wiki/domains/dnd/call-of-the-netherdeep/adaptation/`

## 当前阶段
- 已完成：架构骨架与入口页
- 下一步：将第4章相关 legacy 内容优先映射到新的 entities / sources / views
