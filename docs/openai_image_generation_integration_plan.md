# OpenAI Image Generation Integration Plan

## Purpose

このリポジトリで将来的にChatGPT images / OpenAI image generationを使い、教材用key visualを生成・保存・レビューするための設計案。

今回は設計のみ。APIキー、`.env`、生成画像、実行スクリプト本体は追加しない。

Official references to verify before implementation:

- OpenAI image generation guide: `https://platform.openai.com/docs/guides/image-generation`
- OpenAI Images API reference: `https://platform.openai.com/docs/api-reference/images`
- OpenAI Responses API reference: `https://platform.openai.com/docs/api-reference/responses`

## Recommended Directory Structure

```text
prompts/image_generation/
  global/
    visual_anchor_prompt.md
    character_prompt.md
    negative_prompt.md
  day1/
    page_01_mission_board.md
    page_02_case_file_work.md
    page_03_evidence_board_money.md
    page_04_card_table_value.md
    page_05_business_case_file.md
    page_06_final_mission_sheet.md
  day2/
  day3/
  day4/
  day5/
  parents/

assets/generated/
  day1/
    page_01/
      candidates/
      final/
      rejected/
  day2/
  day3/
  day4/
  day5/
  parents/

reviews/image_generation/
  day1/
    review_manifest.json
    contact_sheet_review.md
  day2/
  day3/
  day4/
  day5/
  parents/

scripts/
  image-generation/
    generate_page_visual.ts
    generate_day1_visuals.ts
    build_contact_sheet.ts
    review_manifest_schema.json
```

For the current repository stage, prompts can live in `outputs/day1/prompts/`. Once automation begins, move reusable prompts into `prompts/image_generation/`.

## What To Save For Reproducibility

Each generation must save a manifest record.

```json
{
  "page_id": "day1_page_01",
  "session": "day1",
  "asset_role": "key_visual",
  "page_type": "Mission Board",
  "aspect_ratio": "16:9",
  "target_size": "1920x1080",
  "prompt_path": "prompts/image_generation/day1/page_01_mission_board.md",
  "anchor_prompt_path": "prompts/image_generation/global/visual_anchor_prompt.md",
  "character_prompt_path": "prompts/image_generation/global/character_prompt.md",
  "negative_prompt_path": "prompts/image_generation/global/negative_prompt.md",
  "generation_date": "YYYY-MM-DD",
  "tool": "openai",
  "model": "verify-before-use",
  "final_output": "assets/generated/day1/page_01/final/day1_page_01_v001.png",
  "candidate_outputs": [],
  "review_status": "pending_human_review",
  "review_memo": "",
  "human_reviewer": ""
}
```

## Script Design

### `generate_page_visual.ts`

Purpose:

- Generate one page visual from prompt files.
- Save candidates.
- Append manifest records.

Inputs:

- `--page-id`
- `--prompt`
- `--anchor`
- `--character`
- `--negative`
- `--aspect-ratio`
- `--out-dir`
- `--manifest`

Output:

- candidate images
- manifest update

Rule:

- Do not overwrite selected assets.
- Do not write secrets to manifest.

### `generate_day1_visuals.ts`

Purpose:

- Batch wrapper for Day1 only after human approval.
- Calls `generate_page_visual.ts` page by page.

Rule:

- Default mode should be dry-run.
- Require `--confirm` for actual generation.
- Allow `--page 1` for pilot generation.

### `build_contact_sheet.ts`

Purpose:

- Create a contact sheet from selected or candidate outputs.
- Useful for human review.

### `review_manifest.json`

Purpose:

- Store generation metadata and review status.
- Do not store API keys or private user data.

## API Strategy

Use the current official OpenAI documentation at implementation time.

Recommended split:

- Use image generation endpoint or image generation tool for key visual creation.
- Use image editing flow only when revising an accepted composition.
- Use layout code or HTML/CSS for exact Japanese text, blanks, page numbers, cards, and export.

Do not depend on image generation for exact long Japanese text. It is better to generate clean visual surfaces and overlay text later.

## Environment And Secrets

Do not commit:

- `.env`
- API keys
- generated browser profiles
- cookies
- login data
- cache

Recommended local environment variable:

- `OPENAI_API_KEY`

If adding scripts later, document setup in a README but keep secrets out of git.

## Naming Convention

Generated asset:

```text
assets/generated/day1/page_01/candidates/day1_page_01_v001_candidate_01.png
assets/generated/day1/page_01/final/day1_page_01_v001.png
```

Prompt:

```text
prompts/image_generation/day1/page_01_mission_board_v001.md
```

Review:

```text
reviews/image_generation/day1/day1_page_01_review_v001.md
```

## Review Flow

1. Create prompt.
2. Run dry-run manifest check.
3. Generate one pilot page.
4. Human reviews the page.
5. If defects are found, create a correction prompt and regenerate or edit.
6. Re-review the revised candidate.
7. Move only approved assets to `final`.
8. If accepted, generate remaining pages one by one.
9. Build contact sheet.
10. Review against global acceptance criteria.
11. Overlay exact Japanese text and UI.
12. Export 16:9.
13. Only after approval, adapt to 4:5 and A4.

## Common Failure Prevention

| Failure | Rule |
| --- | --- |
| Too much text | Prompt must say exact Japanese text is added later |
| Character inconsistency | Use anchor and character prompt every time |
| Page becomes poster | Require page type and learner action |
| Game element becomes decoration | Define the learning action for each game element |
| Confusing props | Require prop-to-action review before final |
| First image treated as final | Store initial outputs as candidates only |
| Money hype | Negative prompt bans cash piles and luxury imagery |
| Existing IP resemblance | Negative prompt bans IP/style imitation; human review checks it |
| Parent becomes judge | Parent prompts must say facilitator, not judge |
| Childish style | Prompt says grade 8, not preschool, not chibi-only |

## What Image Generation Should Do

Use image generation for:

- character scenes
- hand actions
- props and environment
- warm visual tone
- Before/After emotional state
- Mission Board, Case File, Card Table, Experiment Lab, Pitch Stage key visuals

Use post-edit/layout for:

- exact Japanese copy
- long body text
- blanks
- worksheet fields
- page numbers
- cards requiring exact wording
- final export formats

## Pilot Recommendation

Before full automation, run only one pilot:

- Day1 Page 1 Mission Board
- 16:9
- use anchor + character + page prompt
- generate 2-4 candidates
- choose 1 selected image
- overlay exact Japanese copy manually or with a small layout script
- review before continuing

## Manual Handoff Mode Is Current Default

現在の標準運用はAPI自動生成ではなく manual handoff mode です。Codexはprompt packet、レビュー、保存先、修正prompt、candidate/final管理を担当し、ユーザーがChatGPT / GPT画像生成にpromptを貼ってcandidate画像を作ります。

API自動化は将来の補助機能です。APIがないことを理由に、プロンプト整備、手動生成、レビュー、教材設計を止めません。

Manual handoff prompt packets live under:

```text
outputs/day1/image_generation/prompt_packets/
```

The same structure should be used for Day2-Day5 and parent-facing materials when they enter image production.
