# Failure → Repair Matrix

Use this only after a failure is observed or when the user explicitly asks for diagnosis/repair.

| Failure | First repair target | Principle |
|---|---|---|
| Identity drift | Reference / subject layer | strengthen identity anchors without adding unrelated style |
| Spatial relation flip | Blocking / continuity | re-lock only the required spatial relation |
| Posture collapse | Action/state layer | describe the observable stable state |
| Frozen or overly rigid motion | Action / motion wording | distinguish intended stillness from intended motion |
| Action timing error | Temporal layer | complete prerequisite action before dependent action |
| Missing transition | State transition | add only the minimum observable bridge |
| Camera teleport / unwanted movement | Camera layer | replace competing camera instructions with one clear decision |
| Unwanted dialogue | Dialogue layer | isolate authorized speech and speaker IDs |
| Voice mismatch | Audio/reference layer | preserve timbre/delivery role without copying source content |
| Environment drift | Environment/reference layer | strengthen the authorized environment anchor |
| Reference contamination | Reference role layer | narrow each reference to its assigned responsibility |

## Repair discipline

1. Identify the failed observable behavior.
2. Locate the smallest responsible layer.
3. Patch only TARGET + proven dependencies.
4. Recompile the full applicable H3 payload.
5. Re-run semantic QA.

Do not rewrite the whole Skill for a local failure.
