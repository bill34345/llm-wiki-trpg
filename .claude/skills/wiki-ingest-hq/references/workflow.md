# wiki-ingest-hq workflow

Follow this workflow in order.

## 1. Detect ingest mode
Determine whether the user wants:
- single file ingest
- URL ingest
- image ingest
- batch ingest
- force ingest / re-ingest

## 2. Delta tracking
Before ingesting a file-based source, check `.raw/.manifest.json`.
- If the source hash is unchanged, skip and report that it is already ingested.
- If the user requested force ingest or re-ingest, skip delta checking and continue.
- After ingest, update the manifest with hash, ingest date, pages created, pages updated, and the finalized raw path when applicable.
- Treat `.raw/inbox/` as a queue. A successful file-based ingest from inbox must be finalized by moving the raw source into the correct `.raw/ingested/...` location.
- If ingest is incomplete, blocked, or failed, leave the file in `.raw/inbox/`.
- Never delete the only raw copy automatically.
- Before reporting success, verify that the manifest and the final raw file location agree.

## 3. Read the source completely
Do not skim.

## 4. Build the extraction map
Identify:
- source title and scope
- key entities
- key events and processes
- important concepts
- relationships
- likely future questions a human or AI would ask

## 5. Update `wiki/sources/`
Create or improve the source summary.
The source summary should explain the source and point into the canonical graph, but should not be the only place that stores crucial reusable details.

## 6. Update canonical pages
Create or update the pages that should hold reusable knowledge.
Typical targets include:
- entities
- events
- locations
- items
- monsters
- factions
- concepts
- view pages

## 7. Backfill missing dependencies
If canonical pages introduce important new links, create the missing destination pages in the same pass.

## 8. Update graph navigation
Update as needed:
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
- relevant `_index.md`
- relevant domain/view pages
- `wiki/overview.md` if the larger picture changed

## 9. Handle contradictions
If the source conflicts with existing content, add bidirectional contradiction callouts rather than silently replacing prior claims.

## 10. Query-readiness review
Read `query-readiness.md` and verify the updated pages can answer the likely questions.
If not, continue improving them before reporting success.
