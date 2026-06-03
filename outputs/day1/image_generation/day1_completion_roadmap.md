# Day1 Image Generation Completion Roadmap

## Current Status

| Page | Status | Review / Prompt | Notes |
| --- | --- | --- | --- |
| Page 1 Mission Board | direction approved / needs final review | `outputs/day1/image_generation/reviews/day1_page_01_review.md` | User said: 「むっちゃいい感じ。この方向ですすめてほしい」. Candidate image file is not in repo. |
| Page 2 Case File - Work | candidate direction approved / needs final review | `outputs/day1/image_generation/reviews/day1_page_02_review.md` | User said: 「よい！」. Candidate image file is not in repo. |
| Page 3 Evidence Board - Money | prompt packet ready / candidate pending | `outputs/day1/image_generation/prompt_packets/day1_page_03_prompt_packet_for_gpt.md` | Generate manually in ChatGPT / GPT image generation, one candidate at a time. |
| Page 4 Card Table - Value | prompt ready | `outputs/day1/prompts/day1_page_04_image_generation_prompt_final.md` | Candidate generation pending. |
| Page 5 Business Detective Case File | prompt ready | `outputs/day1/prompts/day1_page_05_image_generation_prompt_final.md` | Candidate generation pending. |
| Page 6 Final Mission Sheet | prompt ready | `outputs/day1/prompts/day1_page_06_image_generation_prompt_final.md` | Candidate generation pending. |

## Important Boundary

No page is final yet.

Page 1 and Page 2 are direction-approved by the user, but actual candidate image files are not present in the repository. A human must place the image files or generate new candidates before final visual review.

## Day1 16:9 Final Completion Steps

1. Place Page 1 and Page 2 candidate image files in `assets/generated/day1/page_01/candidates/` and `assets/generated/day1/page_02/candidates/`, or use `outputs/day1/image_generation/candidates/` as the temporary alternative.
2. Visually review Page 1 and Page 2 using `docs/image_generation_visual_review_checklist.md`.
3. Generate Page 3 candidate from `outputs/day1/image_generation/prompt_packets/day1_page_03_prompt_packet_for_gpt.md`.
4. Visually review Page 3.
5. If needed, create correction prompt and regenerate Page 3.
6. Repeat candidate generation and visual review for Page 4.
7. Repeat candidate generation and visual review for Page 5.
8. Repeat candidate generation and visual review for Page 6.
9. Decide overlay text plan for all 6 pages.
10. Move only reviewed and approved images to final naming/location.
11. Create Day1 16:9 contact sheet from final images.
12. Review contact sheet for consistency, flow, text overlay needs, and safety.

## Conditions To Move To 4:5

Do not start 4:5 until:

- all six Day1 16:9 images have final review records
- all six have final / approved status
- overlay text scope is decided
- no candidate image is being used as final
- no page has unresolved prop, hand, gaze, text, or safety issue

## Conditions To Reflect Into Script / Cards / Worksheet

Do not reflect into facilitator script, cards, or worksheet until:

- Day1 16:9 final 6 images are approved
- key wording and overlay text are stable
- Page 1 to Page 6 flow is accepted by human review
- the visual language for Mission Board, Case File, Evidence Board, Card Table, and Final Mission Sheet is stable

## Page 3 Candidate Generation Decision

Page 3 candidate was not generated in this run.

Reason:

- The current standard workflow is manual GPT image handoff.
- Codex prepares prompt packets and review rules.
- The user generates images in ChatGPT / GPT image generation and returns them as candidates.
- OpenAI API automation is optional future support and is not required for this workflow.

Next action:

- Human reviews the Page 3 prompt packet.
- Human pastes the final prompt into ChatGPT / GPT image generation.
- Human generates one Page 3 candidate.
- Candidate is saved as candidate, not final.
- Candidate is visually reviewed before any final adoption.

## Manual GPT Handoff Update

Day1 image generation now uses prompt packets for manual handoff.

Prompt packet index:

`outputs/day1/image_generation/prompt_packets/README.md`

User handoff template:

`outputs/day1/image_generation/user_handoff_template.md`

Current order:

1. If Page 1 / Page 2 direction images already exist outside the repo, place them as candidates.
2. If they are not available, regenerate Page 1 and Page 2 from the prompt packets.
3. Generate Page 3, Page 4, Page 5, and Page 6 one at a time.
4. Save every first output as `candidate`, never `final`.
5. Return each candidate to Codex with the handoff template.
6. Review, revise, and only then consider final adoption.

Codex does not run image generation in this workflow. The user pastes prompt packets into ChatGPT / GPT image generation.
