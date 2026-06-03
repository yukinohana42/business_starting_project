# Image Generation Handoff README

## Purpose

このREADMEは、ユーザーがChatGPT / GPT画像生成でcandidate画像を作り、Codexへ戻すための全体案内です。

Codexは画像生成を実行しません。Codexはprompt packet、レビュー基準、保存先、candidate/final/rejected管理、後載せ文字設計、修正promptを担当します。

## Role Split

| Role | Does | Does Not Do |
| --- | --- | --- |
| Codex | prompt packet作成、保存先指定、review Markdown、修正prompt、後載せ文字設計 | GPT画像生成の代行、画像API実行、見ていない画像のレビュー |
| GPT画像生成 | ユーザーが貼ったpromptからcandidate画像を作る | final判定、教材安全性判断、正確な日本語組版 |
| ユーザー | promptを貼る、candidate画像をrepoへ置く、第一印象を返す、人間承認する | レビュー前にfinal扱いする |

## Prompt Packet Folders

Day1 10 image prompts:

`outputs/day1/image_generation/prompt_packets/day1_10_image_prompts_for_gpt/`

Parent image prompts:

`outputs/parents/image_generation/prompt_packets/`

## Save Paths

Day1 candidate:

```text
assets/generated/day1/page_XX/candidates/day1_page_XX_candidate_YYYYMMDD_01.png
```

Parent candidate:

```text
assets/generated/parents/page_XX/candidates/parent_page_XX_candidate_YYYYMMDD_01.png
```

Alternative candidate path:

```text
outputs/<session>/image_generation/candidates/
```

Final path after review only:

```text
assets/generated/<session>/page_XX/final/
```

Rejected path:

```text
assets/generated/<session>/page_XX/rejected/
```

Review Markdown:

```text
outputs/<session>/image_generation/reviews/
```

## User Next Steps

1. Open the relevant prompt packet.
2. Paste only the "GPT画像生成に貼る最終プロンプト" section into ChatGPT / GPT画像生成.
3. Generate one image at a time.
4. Save the output as `candidate`.
5. Return the report template to Codex.
6. Wait for review or correction prompt before final adoption.

Do not batch-generate all pages. Do not put first outputs into `final`.

## Return To Codex Template

```text
Image candidateをレビューしてください。

page_id:
prompt_packet_used:
candidate_filename:
candidate_path:
human_candidate_decision: keep / revise / reject / unsure
first_impression:
good_points:
concerns:
meaningless_depictions:
text_issues:
hand_prop_gaze_issues:
parent_role_issues:
safety_check:
next_action_requested_for_codex:
```

## Finalization Rule

final化できるのは、以下を満たした画像だけです。

- candidate画像がrepoに保存されている。
- Codexまたは人間が視覚レビューしている。
- 必要なら修正promptで再生成している。
- 採用理由がMarkdownに記録されている。
- 後載せする日本語本文の方針が決まっている。
- 人間が承認している。

Codexが画像を見られない場合は、見たふりをせず `human visual review required` と記録します。
