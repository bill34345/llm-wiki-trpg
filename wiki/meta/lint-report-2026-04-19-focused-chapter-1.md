---
type: meta
title: "Lint Report 2026-04-19"
created: 2026-04-19
updated: 2026-04-19
tags: [meta, lint, dnd, chapter-1]
status: developing
---

# Lint Report: 2026-04-19

## Scope
- Mode: focused
- Target: `.raw/dnd/call-of-the-netherdeep/chapters/第1章_命运之争.md` current ingest surface
- Pages scanned: 16

## Summary
- Issues found: 3
- Critical: 0
- Warnings: 2
- Suggestions: 1

## Critical
- None.

## Warnings
- [[wiki/domains/dnd/call-of-the-netherdeep/views/cast-by-chapter/第1章角色表]]: “吉高关键 NPC”区块仍以纯文本列出德思·米莉姆、科尔布·卡兹长老、阿加西·银勺、欧莫、玛丽尔·棕牙、阿丹；其中多人已在第1章 source、总决赛、奖章页或相关场景中承担稳定可复用职责，但当前 ingest 面没有相应 standalone canonical page，导致第1章人物阅读层在关键本地 NPC 处中断。Suggest: 为这些高频吉高 NPC 建立 standalone 页，并把角色表改为 canonical 链接。
- [[wiki/domains/dnd/call-of-the-netherdeep/chapters/第1章]]: chapter entry 仍保留 `Legacy 内容入口`，把吉高、翡翠石窟与功业节总决赛重新指回旧目录；这与后续章节已切换到 `wiki/` canonical 入口的当前阅读层状态不一致。Suggest: 移除第1章入口中的 legacy 回跳，保持 chapter entry 只指向当前 `wiki/` 层。

## Suggestions
- [[wiki/entities/events/dnd/call-of-the-netherdeep/功业节总决赛]]: `翡翠之眼` 在 source、总决赛页与翡翠石窟页中被反复提及，是第1章表层胜负目标，但当前没有 standalone canonical page。Suggest: 新建 `翡翠之眼` 物品页，并把第1章 source / 总决赛 / 翡翠石窟接回该页。
