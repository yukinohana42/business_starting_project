# Codex Prompt: Freeze GPT Context After Initial GitHub Push

Use this prompt when the project has been pushed to GitHub and the fixed GPT context needs to reflect the current repository state.

## Goal

Update only documentation and fixed-context files so the next ChatGPT/Codex session can understand the current GitHub repository, current HEAD, project rules, and next tasks.

## Required Safety Rules

- Confirm project root, branch, HEAD, worktree status, remote URL, and remote main HEAD before editing.
- Do not use `git add .`.
- Do not create or modify generated lesson assets unless explicitly requested.
- Do not commit browser profiles, Cookie files, Login Data, Cache files, Crashpad dumps, `.env`, or secrets.
- Keep `output/parent_infographic_pdf/chrome-profile/` and `output/parent_infographic_pdf/edge-profile/` untracked.
- Preserve `SOURCE_OF_TRUTH.md`.

## Expected Outputs

- Updated fixed context files under `docs/gpt-fixed-context-2026-06-01/`.
- Updated prompt index if new prompts are added.
- A docs-only commit.
- A pushed documentation branch, not an automatic merge to `main`.

## Visual System v2 Note

If the project has added or changed visual learning system rules, include these in the fixed context:

- `docs/visual_mismatch_root_cause_report.md`
- `docs/visual_learning_system_v2.md`
- `docs/global_visual_acceptance_criteria.md`
- `docs/session_visual_design_map_v2.md`
- `docs/parent_material_design_principles_v2.md`

Do not copy PNG, HTML, CSS, browser profiles, cache, Cookie, Login Data, `.env`, or secrets into the fixed context. Record asset paths and status in Markdown only.
