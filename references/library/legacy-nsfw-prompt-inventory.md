# Legacy NSFW Prompt Collection Inventory

This index records the legacy prompt collections audited during migration.

## Historical prompt families

### Production / reference pose collection
Legacy source:
`PROJECT/ACTIVE-SKILL/h3-prompt-skill-current/references/poses/`

Observed families:
- POV-specific adult scene prompts
- first-person variants
- third-person variants
- cut / shot-transition variants
- position/body-state variants
- unverified samples

Migration:
- structural patterns → `references/library/nsfw-pattern-library.md`
- literal explicit prompt text → historical source only, not active Skill rule

### GROK prompt experiments
Legacy source:
`PROJECT/SKILL_OPTIMIZATION-技能优化/PW-OPT-001-优化skill--参考别人的github技能skill/GROK/`

Observed:
- multiple prompt experiment drafts;
- comparison/optimization variants;
- continuous-shot experiments.

Migration:
- experiment methodology and failure lessons → compiler/QA layers;
- explicit prompt payloads → not copied as active rules.

### Workspace prompt-writing records
Legacy source:
`PROJECT/WORKSPACE-工作区/PROMPT_WRITING-提示词编写/`

Observed:
- original task briefs;
- drafts;
- reviews;
- optimization conversations.

Migration:
- useful reasoning patterns → production reasoning / failure repair;
- historical prompt text remains historical evidence.

### V3 baseline pose library
Legacy source:
`baseline/H3NSFW提示词技能skill第三版-V1-5-patch-optimize/references/poses/`

Observed:
- established adult pose families;
- first-person and third-person organization;
- cut/transition variants;
- unverified samples.

Migration:
- body-state representation;
- POV separation;
- continuity;
- phase isolation;
- reference-role rules.

## Why the literal prompt catalog is not the active Skill

Historical prompts can contain:
- scene-specific assumptions;
- unvalidated behavior;
- model-version-specific tricks;
- duplicated or conflicting instructions;
- explicit sexual payloads.

Therefore the successor treats them as **evidence**, not automatic instructions.

The new Skill retrieves a reusable lesson from the legacy corpus and recompiles it under:
1. current user intent;
2. explicit reference roles;
3. official H3 mode/schema;
4. approved Skill rules;
5. approved experience.

This prevents the historical library from becoming an uncontrolled source of semantic additions.

## Migration status

- Legacy NSFW corpus audited: YES
- NSFW pattern layer migrated: YES
- NSFW core compiler behavior integrated: YES
- Literal historical explicit prompts copied into active rules: NO
- Automatic promotion of historical prompts: NO
- Regression protection: YES
