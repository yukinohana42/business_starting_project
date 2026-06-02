# Current Status and Next Tasks

## Current Branch

`docs/gamified-visual-foundation-v1`

## Current Fixed Context Folder

`docs/gpt-fixed-context-2026-06-01-visual-system-v2/`

## Current Status

Day1 16:9 v2 PNGs and contact sheet were generated earlier, but the visual direction is not accepted as complete.

The key finding is:

- v2 is readable as a Zoom slide set
- v2 has the correct educational tone
- v2 still looks too much like explanation slides with cards and round character icons
- v2 does not sufficiently show character action, discovery-game structure, or functional game elements

Therefore, v2 should not be propagated to scripts, cards, worksheets, 4:5, PDF, or PPTX as the final system.

## 2026-06-02 Manual Handoff Update

The current production direction is manual GPT image handoff, not Codex-run image generation.

Role split:

- Codex creates prompt packets, production plans, review criteria, correction prompts, file paths, candidate/final management, and overlay text plans.
- The user pastes prompt packets into ChatGPT / GPT image generation.
- Generated images return to the repo as candidates.
- Human approval and visual review are required before any final status.

OpenAI API automation is a future optional helper. Lack of an API key must not block prompt packet preparation, manual generation, review, or parent-material planning.

Current handoff docs outside this fixed context:

- `docs/codex_gpt_image_generation_handoff_workflow.md`
- `outputs/day1/image_generation/prompt_packets/README.md`
- `outputs/day1/image_generation/user_handoff_template.md`
- `outputs/parents/parent_explanation_material_plan.md`
- `outputs/parents/parent_explanation_prompt_packet_plan.md`

## Completed in This Visual-System Update

- Added root-cause report for the mismatch between intended direction and v2 PNG result.
- Added Visual Learning System v2.
- Added global visual acceptance criteria.
- Added Day1-Day5 visual design map.
- Added parent material design principles v2.
- Updated design, agent, gamification, character, visual storytelling, reward, manga panel, curriculum, and prompt documents.
- Created Day1 v3 design brief and storyboard.
- Created Day2-Day5 visual design briefs.
- Created parent material visual design brief.
- Created this new fixed context folder.

## Do Not Do Yet

Do not create:

- Codex-run image generation
- GPT image generation on behalf of the user
- Day1 v3 HTML/CSS
- Day1 v3 PNGs
- Day1 v3 contact sheet
- Day2-Day5 HTML/CSS/PNGs
- 4:5 versions
- PDFs
- PPTX files

Do not update Day1 scripts, cards, or worksheets to v2/v3 until the Day1 v3 visual direction is reviewed.

Do not mark any generated image as final until it has been saved as a candidate, reviewed, revised if needed, and approved by a human.

## Next Human Review

Before production resumes, a human should review:

- `outputs/day1/session_01_infographic_v3_design_brief.md`
- `outputs/day1/session_01_infographic_v3_storyboard.md`
- `docs/visual_learning_system_v2.md`
- `docs/global_visual_acceptance_criteria.md`
- `docs/session_visual_design_map_v2.md`

The review should confirm:

- each page is a learning screen, not a normal explanation slide
- each character is visibly doing something
- the game element on each page supports a learning action
- Day1 still avoids entrepreneurship pressure and money hype
- the v3 storyboard is safe to implement in 16:9 HTML/CSS

## Recommended Next Production Order

1. Human reviews `outputs/day1/image_generation/prompt_packets/README.md`.
2. User places existing Page1/Page2 direction images as candidates, or regenerates them from the prompt packets.
3. User generates Page3, Page4, Page5, and Page6 one by one from prompt packets.
4. Codex reviews returned candidates, or records `human visual review required` if the images are not accessible.
5. Codex creates correction prompts where needed.
6. Human approves Day1 16:9 final 6 images.
7. Create final contact sheet and overlay text plan.
8. Only then expand to 4:5.
9. Then reflect the accepted visual structure into facilitator script, cards, and worksheet.
10. Then proceed to parent explanation material production after human review of `outputs/parents/parent_explanation_material_plan.md`.
