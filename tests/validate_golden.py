#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
p = (ROOT / "tests/golden/basic-office.expected.txt").read_text(encoding="utf-8")

required = [
    "subject_definitions:",
    "summary:",
    "retention_analysis:",
    "detailed_description:",
    "overall_soundscape:",
    "non_diegetic_music:",
    "Picture 1",
    "boss",
    "boss's office",
    "office desk",
    "conversation",
]

for marker in required:
    if marker not in p:
        raise SystemExit("GOLDEN_MISSING: " + marker)

forbidden = [
    "standing",
    "sitting",
    "computer",
    "documents",
    "window",
    "push-in",
    "camera movement",
    "lighting design",
    "15-second",
    "10-second",
]

hits = [x for x in forbidden if x.lower() in p.lower()]
if hits:
    raise SystemExit("GOLDEN_UNAUTHORIZED_SEMANTICS: " + ", ".join(hits))

order = [
    "subject_definitions:",
    "summary:",
    "retention_analysis:",
    "detailed_description:",
    "overall_soundscape:",
    "non_diegetic_music:",
]
positions = [p.index(x) for x in order]
if positions != sorted(positions):
    raise SystemExit("GOLDEN_SCHEMA_ORDER_FAIL")

print("GOLDEN BASIC OFFICE PASS")
print("unauthorized_semantics=0")
print("runtime_execution=False")
