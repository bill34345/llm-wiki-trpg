# Query-readiness review

Before declaring an ingest complete, test whether the resulting wiki pages can answer the questions a future user will ask.

## Minimum review questions
For each key page, ask:
- Does this page explain what the subject is?
- Does it explain how the subject appears, behaves, or is encountered, if that matters?
- Does it explain triggers, conditions, stages, or gatekeeping, if applicable?
- Does it explain effects, consequences, or outcomes?
- Does it explain key relationships to people, places, factions, events, or objects?
- Does it explain why this page matters in the broader module or knowledge graph?

## Failure signals
The page is still too thin if:
- it only defines the subject at a high level
- it cannot answer concrete follow-up questions without returning to `.raw/`
- it says something is important without explaining the mechanism or consequence
- it compresses a multi-step event into one vague paragraph

## What to do when a page fails
- Add source-backed operational detail.
- Move reusable information out of the source summary into the canonical page.
- Split summary-level material into standalone pages if the knowledge is reusable.
