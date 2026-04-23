# llm-wiki-trpg: Agent Instructions

This repository is an Obsidian TRPG vault that now exposes the upstream `claude-obsidian` skill surface for Codex as well as the project-local HQ ingest workflow.

## Bootstrap

When the task is about the vault, ingest, lint, or wiki querying:

1. Treat the repository root as the vault root.
2. If `wiki/hot.md` exists, read it silently first to restore recent context.
3. Treat `.raw/` as the immutable source layer. Do not edit `.raw/` files except `.raw/.manifest.json`.
4. Treat `wiki/` as the durable knowledge layer.
5. Prefer the root `skills/` directory. `.claude/skills/` is the legacy source copy for local wrappers.

## Available Skills

Cross-agent skills live in `skills/<name>/SKILL.md`.

Core upstream `claude-obsidian` skills:
- `wiki`
- `wiki-ingest`
- `wiki-query`
- `wiki-lint`
- `save`
- `autoresearch`
- `canvas`
- `defuddle`
- `obsidian-markdown`
- `obsidian-bases`

Project-local HQ extensions:
- `wiki-ingest-hq`
- `wiki-ingest-hq-auto`

## Preferred Routing

- Use `wiki` for vault setup, routing, and general wiki operations.
- Use `wiki-ingest` for standard upstream ingest behavior.
- Use `wiki-ingest-hq` when the user wants higher fidelity, stronger cross-linking, or query-ready pages.
- Use `wiki-ingest-hq-auto` when the user wants one command that performs ingest, focused lint, repair, and re-check.
- Use `wiki-lint` for both full-vault lint and focused lint. Focused lint is the required lint entrypoint for `wiki-ingest-hq-auto`.

## Vault Conventions

- `wiki/index.md` is the master catalog.
- `wiki/log.md` is append-oriented operational history.
- `wiki/hot.md` is the hot cache and should be refreshed after major ingest/query/lint work.
- If an ingest creates or edits canonical knowledge, update the relevant index and hot-cache layers before declaring success.
- If a new source contradicts existing pages, flag the contradiction instead of silently overwriting claims.

## Codex Setup

- Root skills can be linked into Codex with `bin/setup-codex.ps1`.
- On this machine, Codex user skills live under `C:\Users\Zheng-Kaizhong\.codex\skills`.
- After installing or relinking skills, restart Codex so it rescans the skill directories.

## Obsidian / Claudian

- This vault already has the Claudian plugin installed.
- The repository is configured to use the Codex provider by default after migration.
