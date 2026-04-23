# llm-wiki-trpg: Vault Compatibility Notes

This vault keeps the `claude-obsidian` operating model:

- `.raw/` is the immutable source layer
- `wiki/` is the durable knowledge layer
- `skills/` is the cross-agent skill surface

## Use This Vault

- Standard scaffold / routing: `skills/wiki/SKILL.md`
- Standard ingest: `skills/wiki-ingest/SKILL.md`
- Standard query: `skills/wiki-query/SKILL.md`
- Standard lint: `skills/wiki-lint/SKILL.md`
- High-fidelity ingest: `skills/wiki-ingest-hq/SKILL.md`
- One-command ingest + focused lint + repair: `skills/wiki-ingest-hq-auto/SKILL.md`

## Current Migration Notes

- Root `skills/` now exposes both upstream `claude-obsidian` skills and the repo-local HQ wrappers.
- For Codex on Windows, use `bin/setup-codex.ps1` to link the skills into the user Codex skill directory.
- If `wiki/hot.md` exists, read it before broad vault exploration.
