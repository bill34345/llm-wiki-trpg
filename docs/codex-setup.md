# Codex Setup

## Goal

Make this vault usable in Codex with:

- the upstream `claude-obsidian` skill surface
- the project-local HQ ingest workflow
- Claudian defaulting to the Codex provider

## What Is Installed

Root `skills/` now contains:

- upstream `claude-obsidian` skills: `wiki`, `wiki-ingest`, `wiki-query`, `wiki-lint`, `save`, `autoresearch`, `canvas`, `defuddle`, `obsidian-markdown`, `obsidian-bases`
- local wrappers: `wiki-ingest-hq`, `wiki-ingest-hq-auto`

## Windows Install

Run this from the repository root in PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File .\bin\setup-codex.ps1
```

What it does:

- creates directory junctions from each root skill into `C:\Users\Zheng-Kaizhong\.codex\skills`
- skips an existing target if it is a normal directory or a link pointing elsewhere
- can relink existing junctions with `-ForceRelink`

Example:

```powershell
powershell -ExecutionPolicy Bypass -File .\bin\setup-codex.ps1 -ForceRelink
```

## After Install

1. Restart Codex so it rescans the user skill directory.
2. Reopen this repository in Codex.
3. Codex should now be able to use the root `skills/` set.

## Claudian

The local Claudian settings are switched to the Codex provider by default. If you still want Claude for a session, you can change the provider inside Claudian settings.

## Notes

- `bin/setup-multi-agent.sh` remains useful for Unix-like environments because the repository now has a root `skills/` directory again.
- `.claude/skills/` is kept as the legacy source copy for the local HQ wrappers. Root `skills/` is the cross-agent runtime surface.
