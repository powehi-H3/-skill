#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

base = (ROOT / "tests/golden/base-t2va.expected.txt").read_text(encoding="utf-8")
i2va = (ROOT / "tests/golden/i2va.expected.txt").read_text(encoding="utf-8")

base_order = ["integrated_multimodal_description:", "overall_soundscape:", "non_diegetic_music:"]
if [base.index(x) for x in base_order] != sorted(base.index(x) for x in base_order):
    raise SystemExit("BASE_T2VA_SCHEMA_ORDER_FAIL")
if any(x in base for x in ["subject_definitions:", "retention_analysis:", "detailed_description:"]):
    raise SystemExit("BASE_T2VA_WRONG_OUTER_SCHEMA")
if not i2va.startswith("For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.\n\n"):
    raise SystemExit("I2VA_ALIGNMENT_HEADER_FAIL")
if i2va.count("integrated_multimodal_description:") != 1 or i2va.count("overall_soundscape:") != 1 or i2va.count("non_diegetic_music:") != 1:
    raise SystemExit("I2VA_CORE_SCHEMA_FAIL")
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
print("GOLDEN BASE T2VA PASS")
print("GOLDEN I2VA ALIGNMENT PASS")
print("unauthorized_semantics=0")
print("runtime_execution=False")
