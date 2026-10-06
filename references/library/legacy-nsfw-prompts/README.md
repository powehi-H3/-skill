# Legacy NSFW Prompt Asset Manifest

These files are **historical prompt assets**, not rewritten summaries.

## Preservation contract

- Source: legacy `powehi-H3/minimax-h3-NSFW-skill`
- Migration: original text copied into the successor repository.
- Historical wording is preserved.
- Version/source separation is preserved.
- Historical samples do not automatically become universal Skill rules.
- Validation status remains attached to the historical asset where available.

## Migrated collections

### Active Skill prompt collection
Destination:
`references/library/legacy-nsfw-prompts/poses/`

Includes:
- 做爱/切镜
- 做爱/第一人称视角
- 做爱/第三人称视角
- 待验证样例

### V3 baseline prompt collection
Destination:
`references/library/legacy-nsfw-prompts/baseline/`

Includes the corresponding V3 baseline prompt collection as a separate historical version.

### GROK experiments
Destination:
`references/library/legacy-nsfw-prompts/grok/`

Includes:
- PROMPT-EXP-A
- PROMPT-EXP-B-连续一镜
- PROMPT-PURE-EXTERNAL

### PW-0001
Destination:
`references/library/legacy-nsfw-prompts/pw-0001/`

Includes:
- original task brief
- original GROK draft
- Gemini review
- any previously preserved task-level prompt assets

## How the new Skill uses this library

The library has two distinct uses:

1. **Historical retrieval**
   - User asks to recover an old prompt, compare versions, or continue an old experiment.
   - Retrieve the original asset.

2. **Engineering retrieval**
   - User asks for a new prompt or optimization.
   - Extract reusable lessons from relevant historical assets.
   - Recompile under current H3 rules and current user intent.
   - Do not silently copy unrelated scene semantics.

This keeps the user's original work intact while preventing historical samples from becoming uncontrolled defaults.
