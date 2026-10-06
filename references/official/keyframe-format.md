# Official H3 Keyframe Alignment Format

Source: MiniMax-AI/MiniMax-H3 / skills/h3-prompt-writing / references/base-en.txt.

These are structural instructions, not permission to invent story content.

## T2VA

No image-alignment instruction. Begin directly with the three core fields.

## I2VA

The first line is:

For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

Then one blank line, then the three core fields.

Picture 1 is the actual first frame at 0.00 seconds.

## FL2VA

The first line is:

How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot N) aligns with the S.SS-second mark of the target video.

Then one blank line, then the three core fields.

Picture 1 is the opening endpoint and Picture 2 is the ending endpoint. The description must provide a continuous path between them.

## L2VA

The first line is:

How the reference pictures align with the target video — <Picture 1> (from [Shot N]) aligns with the S.SS-second mark of the target video.

Then one blank line, then the three core fields.

N is the actual final shot index and S.SS is the effective target duration formatted to exactly two decimal places.

## Shared core fields

integrated_multimodal_description:
overall_soundscape:
non_diegetic_music:

integrated_multimodal_description contains the visual timeline, shots, actions, dialogue/singing, speakers, and synchronized diegetic events.

overall_soundscape summarizes ambient and physical sounds across the full video. Dialogue and singing are not repeated here.

non_diegetic_music describes audience-only background music. Use N/A when no non-diegetic music is present.

## Strict compilation note

Do not invent a duration merely to make I2VA/FL2VA/L2VA look complete. If the user's workflow or platform supplies an effective duration, use that actual value. Otherwise request or obtain the required duration rather than silently fabricating one.
