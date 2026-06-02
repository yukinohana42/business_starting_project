# Day1 Page 06 Prompt Packet For GPT

## 1. 使用目的

Day1 Page 6「Final Mission」を、GPT画像生成で1枚ずつcandidate生成するための手渡しパケットです。

このページはFinal Mission Sheetです。成功/失敗ではなく、自分の観察を1文にまとめる場面として見せます。

## 2. 画像生成に貼る最終プロンプト

```text
Create a 16:9 horizontal key visual for Day1 Page 6 of a Japanese junior high school grade 8 entrepreneurship workshop.

This is a calm final reflection screen, not a grading sheet, not a reward screen, and not a business poster.

Overall style:
- warm, original educational illustration
- calm, friendly, organized, lightly adventurous
- suitable for 1920x1080 Zoom sharing
- warm cream paper background, soft navy structure, muted coral accents, warm yellow discovery highlights, soft green value/help accents, pale blue organizing lines
- fully original characters only
- do not imitate any existing anime, manga, game, mascot, brand, artist, studio, or franchise

Page type:
Final Mission Sheet.

Learning message:
Say the true shape of work in your own words.

Scene:
A large Final Mission Sheet lies on a table. Yuu or Sora writes into a large blank sentence area. Miho gently offers a Question Card that helps the learner think, without giving the answer. A few previous Evidence Cards and Discovery Stamps are placed nearby as learning records.

Required sentence area:
Leave a large clean blank area where exact Japanese text will be overlaid later: "仕事とは、＿＿を＿＿に変えること。"
Do not try to render this Japanese text accurately inside the generated image.

Yuu visual cues:
- original Japanese grade 8 student
- short neat dark hair
- casual blue top or hoodie
- detective notebook and pen

Sora visual cues:
- original Japanese grade 8 student
- casual green or teal top
- cards, sticky notes, marker pen

Miho visual cues:
- original warm navigator character
- calm outfit
- Question Card or Reflection Card
- supportive, not teacher-like, not judging

Required visual elements:
- Final Mission Sheet
- large blank sentence area
- Question Card from Miho
- Detective Note or previous Evidence Cards nearby
- Reflection Stamp or Discovery Stamp as learning record
- Quest Map area with the summary step emphasized
- clean overlay area for later Japanese headline and exact sentence

Character action:
Yuu or Sora is writing. Miho holds out a Question Card. The posture should feel reflective and calm, not judged or scored.

Learner action shown:
The learner can see that they should write one sentence in their own words.

Visible change:
Seeing work vaguely -> seeing who changes and how.

Text handling:
- Do not generate long Japanese text.
- Leave a large blank sentence area.
- The Question Card may be blank or use a very short placeholder.
- Exact Japanese headline, sentence, and card text will be added later in layout.

Safety:
- no scoring, grading, judgment, correct/incorrect mark, success/failure mark, trophy, prize, reward, level-up, ranking, or winner framing
- Miho supports with a question, not an answer
- Final Mission is a learning record, not a reward
- no pressure to become an entrepreneur

Negative prompt:
existing anime style, manga franchise style, game character style, mascot style, specific artist imitation, brand logos, copyrighted character resemblance, grading sheet, red score marks, correct/incorrect stamp, trophy, reward, winner, level-up, teacher judging student, parent judge panel, face-only characters, floating Question Card, pen not connected to hand, duplicated props, broken hands, impossible fingers, generated long Japanese paragraphs, broken Japanese used as final text, money hype, startup pressure
```

## 3. 生成後に見るべきチェック項目

- Final Mission Sheetに見えるか。
- 大きな空欄が十分にあるか。
- 「仕事とは、＿＿を＿＿に変えること。」を後載せできるか。
- ユウまたはソラが書いている行動をしているか。
- ミホが正解を教える先生ではなく、問いカードで支えているか。
- 採点、合否、報酬、成功/失敗に見えないか。
- Evidence CardやDiscovery Stampが学びの記録に見えるか。
- ペン、カード、シート、スタンプが自然につながっているか。
- 日本語本文を後載せできる余白があるか。
- 起業押し付け、お金煽り、勝敗、ランキングがないか。
- 既存IPや特定作品に似ていないか。

## 4. NGなら使う修正プロンプトテンプレート

```text
Revise the Day1 Page 6 Final Mission Sheet image while keeping the same warm discovery-game educational style.

Keep:
- large Final Mission Sheet
- Yuu or Sora writing in a large blank sentence area
- Miho offering a Question Card
- previous Evidence Cards and Discovery Stamps as learning records
- 16:9 Zoom-friendly layout

Fix:
- [insert specific issue: grading feel, floating card, small blank area, broken hand, broken text]

Clarify:
- Final Mission is a reflection and learning record, not a reward
- Miho supports with a question, not an answer
- the pen connects naturally to the hand
- leave a large blank area for exact Japanese overlay text

Remove:
- score, grade, correct/incorrect marks, trophy, reward, level-up, ranking
- floating props, duplicated props, broken Japanese
- money hype or startup pressure
- any resemblance to existing characters, anime, manga, games, mascots, brands, or artist styles
```

## 5. ファイル保存先の指示

生成画像はfinalにしないでください。candidateとして保存します。

推奨保存先:

```text
assets/generated/day1/page_06/candidates/day1_page_06_candidate_YYYYMMDD_01.png
```

代替保存先:

```text
outputs/day1/image_generation/candidates/day1_page_06_candidate_YYYYMMDD_01.png
```

## 6. Codexへ戻すときの報告テンプレート

```text
page_id: day1_page_06
prompt_packet: outputs/day1/image_generation/prompt_packets/day1_page_06_prompt_packet_for_gpt.md
candidate_path:
first_impression:
good_points:
concerns:
meaningless_depictions:
text_issues:
hand_prop_gaze_issues:
human_candidate_decision: keep / revise / reject / unsure
next_action_requested_for_codex:
```
