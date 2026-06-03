# Day1 10 Image Prompts For GPT

## Purpose

Day1「働く・お金・価値」の画像生成prompt packetを1フォルダに集約する。

Codexは画像生成を実行しない。ユーザーがChatGPT / GPT画像生成へpromptを貼り、生成画像をcandidateとしてrepoへ戻す。

## Prompt Packet List

| Order | Role | Packet |
| --- | --- | --- |
| 1 | Page1 Mission Board | `day1_01_page_01_mission_board_prompt_for_gpt.md` |
| 2 | Page2 Case File - Work | `day1_02_page_02_case_file_work_prompt_for_gpt.md` |
| 3 | Page3 Evidence Board - Money | `day1_03_page_03_evidence_board_money_prompt_for_gpt.md` |
| 4 | Page4 Card Table - Value | `day1_04_page_04_card_table_value_prompt_for_gpt.md` |
| 5 | Page5 Business Detective Case File | `day1_05_page_05_business_detective_case_file_prompt_for_gpt.md` |
| 6 | Page6 Final Mission Sheet | `day1_06_page_06_final_mission_sheet_prompt_for_gpt.md` |
| 7 | Yuu reference | `day1_07_character_yuu_reference_prompt_for_gpt.md` |
| 8 | Sora reference | `day1_08_character_sora_reference_prompt_for_gpt.md` |
| 9 | Miho reference | `day1_09_character_miho_reference_prompt_for_gpt.md` |
| 10 | Common UI parts | `day1_10_common_ui_parts_prompt_for_gpt.md` |

## Recommended Order

まず本編Page1からPage6を1枚ずつcandidate生成する。

推奨順:

1. `day1_01_page_01_mission_board_prompt_for_gpt.md`
2. `day1_02_page_02_case_file_work_prompt_for_gpt.md`
3. `day1_03_page_03_evidence_board_money_prompt_for_gpt.md`
4. `day1_04_page_04_card_table_value_prompt_for_gpt.md`
5. `day1_05_page_05_business_detective_case_file_prompt_for_gpt.md`
6. `day1_06_page_06_final_mission_sheet_prompt_for_gpt.md`
7. 必要ならYuu / Sora / Miho reference
8. 必要ならcommon UI parts

キャラクター一貫性を優先する場合は、Yuu、Sora、Miho referenceを先に生成してもよい。

## Candidate Rule

- 画像は必ずcandidateとして保存する。
- 一括生成しない。
- final化は視覚レビューと人間承認後のみ。
- 細かい日本語本文、カード文言、ページ番号、空欄は後載せする。
- 既存作品、既存キャラクター、特定漫画家、特定スタジオ、ブランド、ロゴの模倣は禁止。

## Return To Codex

生成後は次をCodexへ戻す。

```text
Day1 image candidateをレビューしてください。

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
safety_check:
next_action_requested_for_codex:
```

Codexが画像を確認できない場合は、見たふりをせず `human visual review required` と記録する。
