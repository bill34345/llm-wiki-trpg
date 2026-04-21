---
name: wiki-lint
description: Compatibility wrapper for wiki lint in this project. Use when the user asks to lint the wiki, run a focused wiki health check, audit dead links/orphans/frontmatter gaps, or when `wiki-ingest-hq-auto` needs its mandatory focused lint pass.
allowed-tools: Read Write Edit Glob Grep
---

# wiki-lint

This project-local skill is a compatibility wrapper for the marketplace `Codex-obsidian` wiki-lint behavior. Use it whenever this project needs a reliable `/wiki-lint` entrypoint even if marketplace skill names are not exposed directly in the current session.

## Modes

### 1. Full wiki lint
Use this when the user asks to lint the whole vault.

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
5. missing standalone pages for concepts/entities repeatedly referenced in scope
6. missing cross-references
7. stale or contradicted claims
8. stale index entries, if index-like pages are in scope

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

## Guardrails

Do not auto-fix anything inside this skill. Report only.

If invoked from `wiki-ingest-hq-auto`, the repair pass happens after this report and must stay within the same focused scope before running a second focused lint.
