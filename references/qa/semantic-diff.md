# Semantic Diff QA

Before final output compare the final prompt against the current user request.

## Required checks

1. Every explicit entity remains.
2. Every explicit relationship remains.
3. Every explicit reference role remains.
4. Every explicit action remains.
5. Every explicit setting remains.
6. Every explicit sequence constraint remains.
7. No unrequested story fact was introduced.
8. No unrequested camera or lighting was introduced.
9. No unrequested dialogue or sound was introduced.
10. No unrelated field was rewritten during a repair task.

## Minimality principle

When two compilations satisfy the request equally well, prefer the one with fewer unauthorized assumptions.
