# Default-skill strengths to preserve

The HQ skill should inherit these strengths from the default `wiki-ingest` skill instead of discarding them.

## Operational strengths to keep
- Delta tracking via `.raw/.manifest.json`
- Separate entry handling for file, URL, image, and batch ingest
- A clear source-summary → canonical-pages → navigation → log workflow
- Bidirectional contradiction handling
- Hot cache and index updates as first-class ingest outputs
- Basic anti-duplication discipline
- Logging every ingest

## Important caution
The default skill is better at workflow completeness than at enforcing page depth. HQ should preserve the workflow skeleton while tightening the content quality bar.
