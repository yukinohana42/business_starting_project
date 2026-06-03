# Day1 06 Page 06 Final Mission Sheet Prompt For GPT

## 使う目的

Day1 Page6「仕事の正体を、自分の言葉で言う」を、Final Mission Sheetとして見せるcandidate画像を作る。

## GPT画像生成に貼り付ける最終プロンプト

```text
Create a 16:9 horizontal warm hand-drawn educational illustration for a Japanese junior high school grade 8 workshop.

This is a calm reflection learning screen, not a grading sheet, reward screen, or business poster.

Use fully original characters only. Do not imitate existing anime, manga, game, mascot, brand, logo, artist, studio, or franchise.

Page type: Final Mission Sheet.

Scene:
A large Final Mission Sheet lies on a table. Yuu or Sora writes into a large blank sentence area. Miho gently offers a Question Card. A few previous Evidence Cards and Discovery Stamps appear subtly as learning records.

Show:
- Final Mission Sheet
- large clean blank area for later Japanese overlay: "仕事とは、＿＿を＿＿に変えること。"
- Question Card from Miho
- Detective Note or previous Evidence Cards
- Reflection Stamp or Discovery Stamp as learning record, not reward
- Quest Map with the summary step emphasized
- clean headline area for later Japanese overlay: "仕事の正体を、自分の言葉で言う"

Character action:
Yuu or Sora writes on the sheet. Miho offers a question, not an answer. The mood is calm, reflective, and not judged.

Text handling:
Do not generate long Japanese text. Do not try to render the exact Japanese sentence inside the image. Leave a large blank area for overlay.

Safety:
No grading. No score. No correct/incorrect marks. No success/failure feeling. No trophy, winner, prize, reward, ranking, startup pressure, or money hype.

Negative prompt:
existing anime, manga, game, mascot, brand, logo, specific artist style, studio style, grading sheet, red score marks, correct/incorrect stamp, trophy, reward, winner, level-up, teacher judging student, parent judge panel, face-only character, floating Question Card, pen not connected to hand, duplicated props, broken hands, impossible fingers, long generated Japanese paragraphs, money hype, startup pressure.
```

## 生成後チェック

- Final Mission Sheetに見えるか。
- 大きな空欄に「仕事とは、＿＿を＿＿に変えること。」を後載せできるか。
- YuuまたはSoraが書く行動をしているか。
- Mihoが正解を教える先生ではなく、問いカードで支えているか。
- 採点、合否、報酬、成功/失敗に見えないか。
- Evidence CardやDiscovery Stampが学びの記録に見えるか。
- 日本語を後載せできる余白があるか。
- 起業押し付け、お金煽り、勝敗、ランキングがないか。
- 既存作品や特定絵柄に似ていないか。

## 修正プロンプトテンプレート

```text
Revise the Day1 Page6 Final Mission Sheet image while keeping the warm discovery-game educational style.

Keep: large Final Mission Sheet, Yuu or Sora writing in a large blank sentence area, Miho offering a Question Card, previous Evidence Cards and Discovery Stamps as learning records, 16:9 layout.
Fix: [specific issue]
Clarify: Final Mission is reflection, not reward. Miho supports with a question, not an answer. Pen connects naturally to hand.
Remove: score, grade, correct/incorrect marks, trophy, reward, level-up, ranking, floating props, broken Japanese, money hype, startup pressure, IP resemblance.
Text: leave a large blank area for exact Japanese overlay.
```

## 候補保存先

```text
assets/generated/day1/page_06/candidates/day1_page_06_candidate_YYYYMMDD_01.png
```

代替:

```text
outputs/day1/image_generation/candidates/day1_page_06_candidate_YYYYMMDD_01.png
```

## Codexへ戻すテンプレート

```text
page_id: day1_page_06
prompt_packet_used: outputs/day1/image_generation/prompt_packets/day1_10_image_prompts_for_gpt/day1_06_page_06_final_mission_sheet_prompt_for_gpt.md
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

## 最終化しないルール

最初の生成画像はcandidateです。視覚レビューと人間承認が終わるまでfinalにしません。

## 日本語テキストの扱い

日本語の見出し、本文、ラベルは画像生成で完成させない。画像には、後から正しい日本語を重ねるための余白と読みやすい配置だけを作る。生成画像に崩れた日本語や不要な英字が出た場合は、候補レビューで修正対象にする。

## 権利とスタイルの禁止事項

既存の漫画、アニメ、ゲーム、ブランド、ロゴ、マスコット、特定作家、特定スタジオのキャラクターや絵柄をまねない。人物、衣装、小物、UIはすべて完全オリジナルとして扱う。
