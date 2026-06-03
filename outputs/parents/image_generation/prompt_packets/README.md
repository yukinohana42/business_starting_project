# Parent Image Prompt Packets For GPT

## Purpose

親説明用資料の画像・図解candidateを、ユーザーがChatGPT / GPT画像生成へ1枚ずつ貼って作るためのprompt packet一覧です。

Codexは画像生成を実行しません。Codexはprompt packet、レビュー基準、保存先、candidate/final管理、後載せ文字設計、修正promptを担当します。

## Packet List

| Order | Purpose | Packet |
| --- | --- | --- |
| 1 | Cover / Facilitator Guide | `parent_01_cover_facilitator_guide_prompt_for_gpt.md` |
| 2 | Why this workshop | `parent_02_why_this_workshop_prompt_for_gpt.md` |
| 3 | Parent role | `parent_03_parent_role_facilitator_not_teacher_prompt_for_gpt.md` |
| 4 | OK / NG response sheet | `parent_04_ok_ng_response_sheet_prompt_for_gpt.md` |
| 5 | Question card | `parent_05_question_card_prompt_for_gpt.md` |
| 6 | Safety boundary card | `parent_06_safety_boundary_card_prompt_for_gpt.md` |
| 7 | Session flow map | `parent_07_session_flow_map_prompt_for_gpt.md` |
| 8 | Reward / badge explanation | `parent_08_reward_badge_explanation_prompt_for_gpt.md` |
| 9 | After session reflection | `parent_09_after_session_reflection_prompt_for_gpt.md` |
| 10 | Parent visual anchor | `parent_10_parent_material_visual_anchor_prompt_for_gpt.md` |

## Recommended Order

1. まず `outputs/parents/parent_explanation_material_plan.md` を人間確認する。
2. 必要なら `parent_10_parent_material_visual_anchor_prompt_for_gpt.md` で親向け共通トーンを確認する。
3. Page1からPage9を1枚ずつcandidate生成する。
4. 各candidateをレビューし、必要なら修正promptを作る。

親向け資料では文字の正確さが重要です。本文、OK/NG声かけ、表、チェックリストは後載せ前提にしてください。

## Design Rule

- 子供向けよりゲームUIを弱める。
- 温かいが落ち着いた見た目にする。
- 親を先生、採点者、ゲームマスターにしない。
- 親は問いを出す伴走者として描く。
- 起業押し付け、お金煽り、将来不安、競争、採点を避ける。

## Candidate Rule

- 画像はcandidateとして保存する。
- final化は視覚レビューと人間承認後のみ。
- 一括生成しない。
- 固定情報源に画像本体をコピーしない。

## Return To Codex

```text
Parent image candidateをレビューしてください。

page_id:
prompt_packet_used:
candidate_filename:
candidate_path:
human_candidate_decision: keep / revise / reject / unsure
first_impression:
good_points:
concerns:
text_issues:
parent_role_issues:
safety_check:
next_action_requested_for_codex:
```

Codexが画像を確認できない場合は、見たふりをせず `human visual review required` と記録する。
