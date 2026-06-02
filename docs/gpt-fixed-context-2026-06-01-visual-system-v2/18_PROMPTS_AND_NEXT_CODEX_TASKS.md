# Prompts and Next Codex Tasks

## Prompt Files Updated or Added

Updated prompt files:

- `prompts/day1_infographic_generation_prompt.md`
- `prompts/slide_generation_prompt.md`
- `prompts/parent_slide_generation_prompt.md`
- `prompts/card_generation_prompt.md`
- `prompts/worksheet_generation_prompt.md`
- `prompts/session_improvement_prompt.md`
- `prompts/codex_design_brushup_plan_prompt.md`
- `prompts/codex_day1_material_improvement_prompt.md`
- `prompts/codex_next_tasks.md`
- `prompts/codex_freeze_gpt_context_prompt.md`

Manual handoff prompt packet files:

- `outputs/day1/image_generation/prompt_packets/README.md`
- `outputs/day1/image_generation/prompt_packets/day1_page_01_prompt_packet_for_gpt.md`
- `outputs/day1/image_generation/prompt_packets/day1_page_02_prompt_packet_for_gpt.md`
- `outputs/day1/image_generation/prompt_packets/day1_page_03_prompt_packet_for_gpt.md`
- `outputs/day1/image_generation/prompt_packets/day1_page_04_prompt_packet_for_gpt.md`
- `outputs/day1/image_generation/prompt_packets/day1_page_05_prompt_packet_for_gpt.md`
- `outputs/day1/image_generation/prompt_packets/day1_page_06_prompt_packet_for_gpt.md`
- `outputs/day1/image_generation/user_handoff_template.md`

New prompt files:

- `prompts/global_visual_learning_system_prompt.md`
- `prompts/session_infographic_generation_prompt_v2.md`
- `prompts/session_cards_generation_prompt_v2.md`
- `prompts/session_worksheet_generation_prompt_v2.md`
- `prompts/parent_material_generation_prompt_v2.md`
- `prompts/visual_acceptance_review_prompt_v2.md`

## How to Use the New Prompt System

Before generating slides, cards, worksheets, or parent materials, require the model to read:

- `docs/visual_learning_system_v2.md`
- `docs/global_visual_acceptance_criteria.md`
- `docs/session_visual_design_map_v2.md`
- `docs/parent_material_design_principles_v2.md` when parent-facing
- `docs/visual_mismatch_root_cause_report.md`
- `docs/codex_gpt_image_generation_handoff_workflow.md`

The model must produce a page-by-page or material-by-material acceptance table before implementation.

If the acceptance table cannot show character action, learning action, and functional game element use, production must stop.

For image-first visuals, create a prompt packet instead of asking Codex to generate images. The user pastes the packet into GPT image generation, saves the output as a candidate, and returns the handoff template to Codex for review.

## Recommended Next Codex Task

Review Day1 manual handoff prompt packets first:

- `outputs/day1/image_generation/prompt_packets/README.md`
- `outputs/day1/image_generation/user_handoff_template.md`

Then the user should generate or place candidates one page at a time. The next Codex task should be candidate review or correction prompt creation, not PNG/PDF/PPTX production.

If a future request resumes HTML/CSS, it should explicitly say:

- create new v3 files only
- do not overwrite v1 or v2
- do not generate PNG yet unless requested
- use the v3 storyboard and acceptance criteria
- avoid round character icons as the main character expression
- make game elements functional, not decorative

## Suggested Next Prompt

Use a prompt with this structure:

1. Confirm project root, branch, HEAD, git status, remote URL, fixed context pointer, and current git status doc.
2. Read the current fixed context folder.
3. Read the Day1 v3 design brief and storyboard.
4. Create `outputs/day1/rendered/session_01_infographic_16x9_v3.html`.
5. Create `outputs/day1/rendered/session_01_infographic_16x9_v3.css`.
6. Do not create PNGs yet.
7. Do not create 4:5, PDF, or PPTX.
8. Do not update scripts/cards/worksheets yet.
9. Create a render review Markdown file with page-by-page acceptance checks.

## Review Prompt

After v3 HTML/CSS is created, use:

`prompts/visual_acceptance_review_prompt_v2.md`

The review must decide whether the result is:

- accepted for PNG rendering
- needs small layout correction
- rejected as explanation-slide regression

## Commit Safety

Always stage explicit paths only.

Never use `git add .`.

Never commit `.env`, Cookie, Login Data, Cache, browser profile data, or secrets.
