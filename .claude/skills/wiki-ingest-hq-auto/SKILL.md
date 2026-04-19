---
name: wiki-ingest-hq-auto
description: High-fidelity wiki ingest wrapper that must actually run focused lint, repair, and re-check. Use whenever the user wants one command to force-ingest or re-ingest a `.raw/` source and then automatically validate and improve the result, especially for DND/module content where shallow first-pass ingest is not acceptable.
---

# wiki-ingest-hq-auto

Use this skill when the user wants the ingest flow to keep going after page creation instead of stopping at the first pass.

This skill is a thin wrapper over `wiki-ingest-hq`. It does not replace the HQ ingest rules. It orchestrates them into one mandatory workflow:

1. Run `wiki-ingest-hq` on the requested source.
2. Run the local `/wiki-lint` skill in **focused mode** on only that source's ingest result.
3. Fix the issues found by that focused lint, prioritizing:
   - missing standalone canonical pages
   - hollow or underspecified key pages
   - missing dependency backfills for new links
   - stale frontmatter `updated` dates on pages actually edited in this pass
   - weak faction / event / chapter wiring that leaves reusable knowledge disconnected
4. Run `/wiki-lint` a second time on the same focused scope to verify the repair pass.
5. Report the final state to the user with five buckets:
   - source ingested
   - key pages created
   - key pages updated
   - focused lint findings and repair actions
   - unresolved thin spots or contradictions, if any remain

## Core rule

Do not stop after the first ingest if the result is still visibly thin, structurally incomplete, or leaves broken knowledge paths that a focused lint would catch.

## Hard lint rule

Focused lint is mandatory, not optional. Do not substitute manual Read/Grep checks for focused wiki lint.

A valid run of this wrapper must include:
- first-pass ingest
- an actual focused wiki lint pass
- a repair pass based on that lint output
- an actual second focused wiki lint pass

If focused wiki lint cannot be run, say the workflow is blocked and do not report the auto ingest as complete.

Manual checks are allowed only as supplemental verification after the real focused lint pass has run. They must not be described as the focused lint result.

## Scope rule

Keep ingest and lint conceptually separate, but operationally chained. The point of this wrapper is not to merge the two skills into one concept; it is to automate the handoff so the user does not need to issue the next command manually.

## Focused lint integration

Use the local skill name `/wiki-lint` as the required lint entrypoint for this workflow. In this project, that local skill should act as a compatibility wrapper over the marketplace `claude-obsidian` wiki lint capability, so this wrapper does not depend on marketplace skill-name exposure in the current session.

When running focused lint for an ingest, do not ask for a whole-vault health check. Instead, constrain the lint to the pages created or materially updated by this ingest, plus obvious directly connected navigation pages such as:
- the source page in `wiki/sources/`
- the chapter/view pages touched by the ingest
- newly created or materially deepened canonical pages
- hot/log/index/overview layers only if this ingest edited them

The focused lint pass may still use the marketplace wiki-lint logic and report structure, but the operational scope must stay limited to the current ingest surface.

If the local `/wiki-lint` compatibility wrapper is unavailable or cannot be invoked, the workflow is blocked. Do not silently fall back to manual Read/Grep checks and do not describe a manual review as lint.

## Example invocations
- `force ingest .raw/ingested/dnd/call-of-the-netherdeep/appendices/附录A_生物.md`
- `re-ingest .raw/ingested/dnd/call-of-the-netherdeep/chapters/第4章_希望明珠.md`
- `force ingest .raw/ingested/dnd/call-of-the-netherdeep/preface/前言_AnsweringTheCall.md`

## Output expectations

When reporting back, explicitly say:
- what the first-pass ingest added
- what the first focused lint found
- what was fixed in the repair pass
- whether the second focused lint came back clean or what still needs manual follow-up
- if focused lint did not actually run, that the workflow is blocked rather than complete
