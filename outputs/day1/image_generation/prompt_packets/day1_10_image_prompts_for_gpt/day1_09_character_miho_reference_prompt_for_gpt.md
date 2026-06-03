# Day1 09 Character Miho Reference Prompt For GPT

## 使う目的

Day1 Page6や親向け資料とのつながりを高めるため、Mihoのreference candidateを作る。

## GPT画像生成に貼り付ける最終プロンプト

```text
Create a 16:9 horizontal character reference sheet for Miho, a fully original navigator character for a Japanese junior high school grade 8 workshop.

Miho role:
Navigator. Miho asks short questions and supports reflection.

Miho personality:
friendly, calm, supportive, warm. Miho is not teacher-like, not adult authority, not judge, not examiner, not game master.

Visual direction:
slightly guide-like but not authoritative. Calm outfit. Gentle expression. Parent-safe and age-appropriate for a learning workshop.

Learning props:
Question Card, Reflection Card, Safety Boundary Card. Cards must be held naturally or placed clearly.

Show several small poses in one clean reference sheet:
- offering a Question Card
- listening beside a learner
- pointing gently to a Safety Boundary Card
- supporting a reflection sheet without giving the answer

Text handling:
Do not generate long Japanese text. Use blank labels or very short English placeholders only. Exact labels will be added later.

Safety:
No scoring, judging, grading, ranking, trophy, winner/loser, reward-like elements, money hype, or startup pressure.

Style:
warm hand-drawn educational illustration, clean, parent-safe, Zoom-friendly.

Do not imitate any existing anime, manga, game, mascot, brand, logo, artist, studio, or franchise.

Negative prompt:
existing character resemblance, anime franchise style, game mascot, brand logo, specific artist style, strict teacher, adult authority, judge, examiner, scoreboard, red grading marks, trophy, reward, face-only icon, floating cards, duplicated props, broken hands, broken Japanese text.
```

## 生成後チェック

- Mihoが問いを出すナビゲーターに見えるか。
- 先生、採点者、試験官、ゲームマスターに見えないか。
- Question CardやSafety Boundary Cardが自然に見えるか。
- 子供を評価している構図になっていないか。
- 既存作品や特定絵柄に似ていないか。

## 修正プロンプトテンプレート

```text
Revise the Miho character reference while keeping Miho as a fully original supportive Navigator.

Keep: warm calm guide, Question Card, Reflection Card, Safety Boundary Card, listening and supporting poses.
Fix: [specific issue]
Remove: teacher-like authority, judge or examiner mood, scoreboard, grading marks, trophy, reward, existing character resemblance, floating cards, broken hands, broken Japanese.
Text: keep labels minimal and leave clean blank areas.
```

## 候補保存先

```text
assets/generated/day1/references/candidates/day1_character_miho_reference_candidate_YYYYMMDD_01.png
```

代替:

```text
outputs/day1/image_generation/candidates/day1_character_miho_reference_candidate_YYYYMMDD_01.png
```

## Codexへ戻すテンプレート

```text
page_id: day1_character_miho_reference
prompt_packet_used: outputs/day1/image_generation/prompt_packets/day1_10_image_prompts_for_gpt/day1_09_character_miho_reference_prompt_for_gpt.md
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
