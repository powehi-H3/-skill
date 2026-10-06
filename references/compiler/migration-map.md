# Legacy Migration Map

This project intentionally migrates useful behavior from the previous H3 Skill without importing its old architecture wholesale.

## Migrated

- frozen semantic-baseline thinking → semantic authority + scope locks;
- Extract → Preserve → Normalize → Optimize → Recompile → compiler pipeline;
- State A → Action A → State A1 → Transition → State B → Action B → State B1 → temporal references;
- smallest responsible repair → failure-repair matrix;
- reference role isolation → reference-role lock + reference recipes;
- Subject ≠ Picture → explicit semantic subject labels;
- camera/POV separation → camera grammar;
- blocking before framing → production reasoning;
- payload purity → purity QA;
- functional vs verbal vs polluting repetition → density discipline;
- time-budget reasoning → temporal compilation;
- Prompt Library / Experience Library separation → library architecture;
- user approval gate → Experience Library status/approval rules;
- offline regression → static/golden regression suite;
- frozen-vs-active distinction → project rules vs current compiler behavior.

## Deliberately not migrated into the core

- historical NSFW-specific scene recipes;
- large pose/sample catalogs;
- model-specific anecdotes without validation;
- duplicated control layers and historical version stacks;
- old internal architecture names;
- blanket cinematic defaults;
- automatic promotion of successful outputs into rules.

Those may remain historical material in the old repository. They are not silently promoted into this product.

## Design principle

The new Skill keeps the old project's strongest ideas while removing the mechanisms that caused rule competition and prompt over-expansion.


## NSFW prompt-library migration

The legacy NSFW prompt collections were audited and their reusable engineering patterns were migrated into `references/library/nsfw-pattern-library.md`.

Migrated:
- adult action/state decomposition;
- body-state and spatial-relation representation;
- NSFW POV/camera separation;
- multi-phase state locking;
- reference-role isolation;
- dialogue/audio separation;
- prompt-density discipline;
- Extract → Preserve → Normalize → Optimize → Recompile;
- evidence/validation status separation.

Not copied as active Skill rules:
- literal explicit sexual prompt text;
- unverified explicit samples;
- automatic promotion of historical prompts;
- blanket cinematic defaults.
