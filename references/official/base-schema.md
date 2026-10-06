# Base H3 Schema Reference

This project follows the current official MiniMax H3 prompt-writing contract for base modes.

## Modes

- T2VA: build the audiovisual timeline from text.
- I2VA: start from the supplied first frame and develop forward.
- FL2VA: describe the continuous path from first frame to last frame.
- L2VA: infer a plausible preceding state and converge to the supplied last frame.

## Output fields

Use this exact order:

integrated_multimodal_description:
overall_soundscape:
non_diegetic_music:

## Integrated multimodal description

This is the main timeline. Put concrete shot-level visual information here:

- composition
- subjects
- environment
- actions
- camera
- dialogue / vocal performance
- diegetic sounds when tied to a specific timeline event

Use shot timing when the applicable mode requires it.

## Soundscape

Describe environmental and physical sounds that belong to the scene as a whole or are not better represented as a time-local event.

## Non-diegetic music

Describe only music outside the scene world. Use N/A when no music is requested.

## Keyframe modes

I2VA: the opening image establishes the initial state.

FL2VA: the description must create a plausible continuous path between the supplied endpoints.

L2VA: the description must establish a plausible pre-final state and converge to the supplied final frame.

Never contradict a supplied endpoint.

## Timing

If the user specifies a duration, the described timeline must fit it. Do not invent a duration merely because the model supports a range.
