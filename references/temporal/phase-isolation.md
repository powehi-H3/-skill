# Phase Isolation

Use explicit phase boundaries when the user requests staged behavior.

A phase contains only its own authorized state and actions.

When a later phase depends on completion of an earlier action:

PHASE A
→ completion condition
→ TRANSITION
→ PHASE B

Do not let Phase B action, state, dialogue, or camera behavior leak into Phase A.

Do not invent a completion condition if the user did not specify a meaningful dependency; use only the minimum language needed to express the requested sequence.
