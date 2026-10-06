# Temporal State and Action Transitions

Use state transitions when the request contains sequential actions or phases.

Preferred conceptual model:

STATE A
→ ACTION
→ COMPLETION
→ STATE B
→ NEXT ACTION

Do not write dependent actions as though they occur simultaneously when order matters.

For Phase A / Transition / Phase B:

- Phase A contains only Phase A state/action.
- Transition expresses the actual state change.
- Phase B begins only after the transition is complete.

This is a knowledge rule, not permission to invent a transition the user did not request.
