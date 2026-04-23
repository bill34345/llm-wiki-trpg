# Hard rules for wiki-ingest-hq

These are mandatory rules, not optional style advice.

## 1. Preserve the LLM wiki model
- Treat `.raw/` as immutable source documents.
- Treat `wiki/` as the durable knowledge graph.
- Treat ingest as knowledge-base updating, not source filing.

## 2. Source fidelity comes first
- Read the source fully.
- Ground core claims in the source.
- Do not replace detail with vague thematic summary when the source gives usable specifics.

## 3. Page usefulness is the completion standard
A page is incomplete if it cannot answer the most likely future queries about:
- what something is
- how it appears or behaves
- what triggers it
- what effects or consequences it has
- what it is related to
- what role it plays in the larger structure

## 4. No hollow pages
The following are failures unless the user explicitly asked for a shallow pass:
- one-line anchor pages
- pages that only say something is important
- pages that merely point back to a source summary for substance
- event pages that only say what they advance without explaining what happens

## 5. Canonical pages must absorb important detail
Do not leave crucial operational detail trapped in `wiki/sources/` when it belongs on canonical pages such as entity, event, item, location, faction, or concept pages.

## 6. Backfill dependencies in the same ingest
If ingest creates a key link to a page that does not exist yet, create that page during the same ingest pass unless it is clearly nonessential.

## 7. Preserve graph integrity
Update the relevant indexes, views, overview, hot cache, and log so the graph remains navigable by both humans and AI.

## 8. Contradictions must be explicit and bidirectional
When new information conflicts with existing wiki content:
- add a contradiction callout on the existing page pointing to the new source
- add a contradiction callout on the new source summary pointing back to the existing page
- do not silently overwrite the prior claim

## 9. Quality beats brevity
Use efficient context discipline, but do not use token saving as a reason to skip important details from the source.

## 10. Force ingest means full re-evaluation
When the user says force ingest or re-ingest, do not rely on the prior ingest result as authoritative. Re-read and re-evaluate the source at full fidelity.
