# Day1 08 Character Sora Reference Prompt For GPT

## 使う目的

Day1 Page4以降や後続教材の一貫性を高めるため、Soraのreference candidateを作る。

## GPT画像生成に貼り付ける最終プロンプト

```text
Create a 16:9 horizontal character reference sheet for Sora, a fully original Japanese junior high school grade 8 student.

Sora role:
Idea Builder. Sora makes ideas and value changes visible.

Sora personality:
active, constructive, practical, friendly, not flashy.

Visual direction:
same-age junior high school student, not childish, not adult, not teacher-like. Medium dark hair with simple silhouette. Casual green or teal top. Dark pants. Warm, parent-safe, age-appropriate.

Learning props:
cards, sticky notes, rough sketch paper, pen, marker. Props connect naturally to hands or table.

Show several small poses in one clean reference sheet:
- arranging Value Change Cards
- writing on a sticky note
- drawing a rough sketch
- moving an idea card on a table

Text handling:
Do not generate long Japanese text. Use blank labels or very short English placeholders only. Exact labels will be added later.

Safety:
No startup pressure, money hype, ranking, score, trophy, winner/loser, reward-like elements.

Style:
warm hand-drawn educational illustration, clean, parent-safe, Zoom-friendly.

Do not imitate any existing anime, manga, game, mascot, brand, logo, artist, studio, or franchise.

Negative prompt:
existing character resemblance, anime franchise style, game mascot, brand logo, specific artist style, face-only icon, chibi-only style, adult teacher, flashy influencer, superhero, business suit, money celebration, trophy pose, floating sticky notes, duplicated props, broken hands, broken Japanese text.
```

## 生成後チェック

- Soraが中学2年生らしく見えるか。
- Idea Builderとしてカード、付箋、ラフスケッチを使う行動が見えるか。
- 派手すぎないか。
- 顔だけ、立っているだけになっていないか。
- 小物が手や机と自然につながっているか。
- 既存作品や特定絵柄に似ていないか。

## 修正プロンプトテンプレート

```text
Revise the Sora character reference while keeping Sora as a fully original grade 8 Idea Builder.

Keep: active constructive student, green or teal casual top, cards, sticky notes, rough sketch, pen, action poses.
Fix: [specific issue]
Remove: existing character resemblance, face-only icon, adult teacher look, flashy influencer look, money celebration, floating or duplicated props, broken hands, broken Japanese.
Text: keep labels minimal and leave clean blank areas.
```

## 候補保存先

```text
assets/generated/day1/references/candidates/day1_character_sora_reference_candidate_YYYYMMDD_01.png
```

代替:

```text
outputs/day1/image_generation/candidates/day1_character_sora_reference_candidate_YYYYMMDD_01.png
```

## Codexへ戻すテンプレート

```text
page_id: day1_character_sora_reference
prompt_packet_used: outputs/day1/image_generation/prompt_packets/day1_10_image_prompts_for_gpt/day1_08_character_sora_reference_prompt_for_gpt.md
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
