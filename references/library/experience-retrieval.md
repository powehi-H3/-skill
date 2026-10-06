# Experience Retrieval

Experience retrieval is deliberately small.

## Order

1. Parse current user intent.
2. Lock TARGET / CHANGE / PRESERVE / dependencies.
3. Determine H3 mode.
4. Search only the relevant experience category/tags.
5. Keep only APPROVED, non-stale, non-revoked, non-superseded records.
6. Filter by scope and applicability.
7. Prefer the smallest set of high-relevance records.
8. Extract reusable lessons, not historical prompt text.
9. Recompile under current official H3 rules.
10. Run semantic diff and purity QA.

## Conflict

Current user requirements and official H3 rules always outrank experience.

When approved experiences conflict, choose the one whose applicability matches the current task most closely and whose validation evidence is stronger. Do not merge incompatible recipes merely because both are available.

## Context budget

Do not inject the entire library. Retrieval exists to reduce rule competition, not create another encyclopedia.
