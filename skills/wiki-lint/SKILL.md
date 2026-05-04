---
name: wiki-lint
description: Compatibility wrapper for wiki lint in this project. Supports the upstream claude-obsidian full-vault health check plus the project-local focused lint mode required by `wiki-ingest-hq-auto`.
allowed-tools: Read Write Edit Glob Grep
---

# wiki-lint

This project-local skill is the stable `/wiki-lint` entrypoint for this vault in Codex, Claude, and other Agent Skills compatible tools. It preserves the upstream `claude-obsidian` lint surface while adding the focused lint mode required by the local HQ ingest workflow.

## Modes

### 1. Full wiki lint
Use this when the user asks to lint the whole vault, run a health check, find orphan pages, or perform the original upstream `claude-obsidian` wiki-lint behavior.

### 2. Focused wiki lint
Use this when the user asks to lint a specific source ingest, folder, chapter, entity cluster, or repair surface. This is the default mode for `wiki-ingest-hq-auto`.

For focused lint, keep the scope limited to the actual ingest surface:
- the source page in `wiki/sources/`
- pages created by the ingest
- pages materially updated by the ingest
- directly connected chapter/view/navigation pages touched in the same pass
- recency layers such as `wiki/hot.md`, `wiki/log.md`, `_index.md`, or `overview.md` only if this pass edited them

Do not silently widen a focused lint into a whole-vault audit unless the user explicitly asks for that.

## Checks

Work through these checks in order:
1. dead links
2. missing required frontmatter fields
3. empty sections
4. orphan pages
5. missing standalone pages for concepts or entities repeatedly referenced in scope
6. missing cross-references
7. stale or contradicted claims
8. stale index entries, if index-like pages are in scope

For full-vault lint, also preserve the upstream `claude-obsidian` expectations around:
- stale claims that should be checked against newer sources
- naming consistency
- style-guide violations
- missing dashboards or overview maintenance artifacts when the user explicitly asks for a broader health check

For focused lint, evaluate links and backlinks against the real vault, but report only issues that affect the focused scope.

## Report

Create a lint report under `wiki/meta/`.
- Full vault lint: `wiki/meta/lint-report-YYYY-MM-DD.md`
- Focused lint: `wiki/meta/lint-report-YYYY-MM-DD-focused-<slug>.md`

Use this structure:

```markdown
---
type: meta
title: "Lint Report YYYY-MM-DD"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [meta, lint]
status: developing
---

# Lint Report: YYYY-MM-DD

## Scope
- Mode: full | focused
- Target: <vault | source | folder | chapter cluster>
- Pages scanned: N

## Summary
- Issues found: N
- Critical: N
- Warnings: N
- Suggestions: N

## Critical
- [[Page]]: problem. Suggest: fix.

## Warnings
- [[Page]]: problem. Suggest: fix.

## Suggestions
- [[Page or concept]]: problem. Suggest: fix.
```

List each issue with the affected page, the exact problem, and a suggested fix.

If the user asked for the broader upstream maintenance sweep, the report may additionally call out optional follow-up artifacts such as:
- `wiki/meta/dashboard.md`
- `wiki/meta/overview.canvas`

## Guardrails

Do not auto-fix anything inside this skill. Report only.

If invoked from `wiki-ingest-hq-auto`, the repair pass happens after this report and must stay within the same focused scope before running a second focused lint.

If invoked directly by the user as a standalone lint request, show the report first, then ask whether to repair the safe issues automatically or leave them for manual review.
