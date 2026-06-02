# Image Asset Naming And Review Policy

## Purpose

画像生成物の保存、命名、レビュー、final化のルールを定義する。

candidate、draft、rejected、finalを混同しないことが最重要。画像生成ファースト制作では、最初に出た画像は採用版ではない。

## Recommended Directories

```text
assets/generated/day1/candidates/
assets/generated/day1/final/
assets/generated/day1/rejected/
outputs/day1/image_generation/reviews/
outputs/day1/image_generation/prompts/
```

Day2以降も同じ構造を使う。

```text
assets/generated/day2/candidates/
assets/generated/day2/final/
assets/generated/day2/rejected/
outputs/day2/image_generation/reviews/
outputs/day2/image_generation/prompts/
```

## Naming Examples

Candidate:

```text
day1_page_01_candidate_2026-06-02_a.png
day1_page_01_candidate_2026-06-02_b.png
```

Final:

```text
day1_page_01_final_2026-06-02.png
```

Rejected:

```text
day1_page_01_rejected_2026-06-02_a.png
```

Review:

```text
day1_page_01_review_2026-06-02.md
```

Prompt:

```text
day1_page_01_prompt_2026-06-02.md
```

## Required Metadata

Every image review Markdown must record:

- page id
- generation date
- prompt path
- candidate filename
- review result
- final / rejected 判定
- 採用理由
- 修正理由
- 後載せ予定文字
- 人間確認者
- 次アクション

## Review Result Values

- `PASS_FINAL`
- `PASS_WITH_MINOR_FIX`
- `REGENERATE_WITH_REVISED_PROMPT`
- `REJECT`
- `DIRECTION_APPROVED_NOT_FINAL`

## Rules

- candidateをfinalと混同しない。
- finalはレビュー済みだけに付ける。
- rejectedも削除せず、必要なら理由をMarkdownに残す。
- draftやcandidateの画像を教材納品物として使わない。
- final採用前に、意味不明な描写、小物の破綻、文字崩れ、安全性を確認する。
- 固定情報源フォルダには画像本体をコピーしない。
- 固定情報源には、画像パスとレビュー要約だけ記録する。
- `.env`, Cookie, Login Data, Cache, API key, secretsを画像生成記録に含めない。

## Finalization Checklist

Finalに移す前に確認:

- 画像そのものを視覚レビューした。
- page typeが見える。
- キャラクターが学習行動をしている。
- ゲーム要素が学習行動と結びついている。
- 価値または学びの変化が見える。
- 小物が意味不明な場所から出ていない。
- 手、指、視線、姿勢が自然。
- 文字崩れを教材本文として使わない。
- 後載せ予定文字が決まっている。
- 人間確認者または確認待ち状態が記録されている。

## Review Markdown Template

```markdown
# Image Asset Review

## Metadata

- page id:
- generation date:
- prompt path:
- candidate filename:
- reviewer:
- human reviewer:
- visual review availability:

## Decision

- review result:
- final / rejected:

## Good Points

## Issues

## Correction Prompt

## Overlay Text Plan

## Adoption Reason

## Rejection / Revision Reason

## Next Action
```

## Fixed Context Handling

固定情報源フォルダに入れてよいもの:

- Markdownの要約。
- final画像のパス。
- review結果のパス。
- 採用理由。

固定情報源フォルダに入れないもの:

- PNG本体。
- HTML/CSS本体。
- PDF/PPTX本体。
- candidate画像。
- rejected画像。
- secrets。
