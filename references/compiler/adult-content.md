# Adult-Content Semantic Handling

## Purpose

This layer governs adult/NSFW prompt compilation without changing the selected MiniMax H3 mode.

It is a semantic-preservation layer, not a scene-template catalog.

## Core rule

When the user explicitly supplies adult sexual content, preserve the requested semantic intent during compilation unless a higher-priority structural constraint requires a change.

Do not:
- silently sanitize or erase user-supplied adult semantics;
- replace an explicit requested action with a different action;
- invent additional sexual acts, participants, props, positions, emotions, or escalation;
- import sexual content from unrelated references;
- treat historical adult prompts as permission to add content.

## Scope lock

For adult-content requests, classify each supplied element as:
- SUBJECT
- RELATIONSHIP
- ACTION
- STATE
- LOCATION
- PROP
- DIALOGUE
- TIMING
- CAMERA
- REFERENCE ROLE

Only elements explicitly present or structurally required may enter the payload.

NSFW status does not authorize completion of unspecified details.

## Reference isolation

A reference assigned to identity/appearance supplies identity/appearance only.

A reference assigned to environment supplies environment only.

A reference assigned to motion supplies motion/camera information only to the extent explicitly authorized.

A voice reference supplies timbre/delivery, not dialogue or sexual content.

Do not infer adult actions from a reference merely because the reference visually suggests them.

## Temporal isolation

For multi-phase adult scenes:
- complete prerequisite state/action before dependent state/action;
- keep later-phase actions out of earlier phases;
- use an explicit Transition when the state change matters;
- preserve the requested final state;
- never add intermediate sexual actions merely to fill unused duration.

## Action continuity

Represent requested actions as an observable chain:

INITIAL STATE → TRIGGER → PHYSICAL ACTION → INTERMEDIATE STATE → FINAL STATE

Do not insert an unrequested action between dependent steps.

## Camera separation

Sexual action does not imply:
- POV;
- camera movement;
- zoom;
- tracking;
- close-up;
- reframing;
- voyeuristic framing.

Camera behavior must come from the user's request, an explicitly assigned camera reference, or an applicable approved production rule.

## Dialogue and audio

Preserve user-supplied dialogue exactly when requested.

If an audio reference is assigned only for voice characteristics, do not copy dialogue, wording, sexual sounds, or narrative content from it.

Keep:
- dialogue/vocal performance;
- diegetic soundscape;
- non-diegetic music

as separate concerns.

## Output principle

NSFW handling must compile into the selected H3 schema.

NSFW is not a seventh Ref2VA section and does not override official H3 field names or ordering.
