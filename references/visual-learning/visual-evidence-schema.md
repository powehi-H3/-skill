# Visual Evidence Schema

The Visual Evidence record stores what was observed before an H3 Experience is proposed.

## Record

evidence_id:
source:
  asset_type: IMAGE | VIDEO | AUDIO | MULTIMODAL
  asset_id:
  source_uri:
  source_timestamp:
  frame_or_region:

learning_scope:
  target:
  source_assets:
  range:
  exclusions:
  purpose:

observation:
  direct:
  invariant:
  changed:
  negative_evidence:

inference:
  structural:
  confidence:

hypothesis:
  h3_representation:
  confidence:

validation:
  status: UNTESTED | EXPERIMENTAL | VALIDATED
  method:
  attempts:
  successes:
  failures:

model_context:
  observer_model:
  h3_model:
  skill_version:

traceability:
  source_prompt:
  source_project:
  related_experiences:

## Rules

1. learning_scope is mandatory.
2. observation must be distinguishable from inference.
3. hypothesis must not be presented as an observed fact.
4. Excluded elements must not be promoted into the hypothesis.
5. Validation requires an H3 experiment or equivalent approved evidence.
6. User approval is required before an evidence-derived Experience becomes an active rule.
