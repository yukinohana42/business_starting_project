# Day1 Page 03 Prompt Packet For GPT

## 1. 使用目的

Day1 Page 3「お金とは何か」を、GPT画像生成で1枚ずつcandidate生成するための手渡しパケットです。

このページはEvidence Board - Moneyです。「お金は『ありがとう』が見える形」を、価値が届いたサインとして見せます。画像はfinalではなくcandidateです。

## 2. 画像生成に貼る最終プロンプト

```text
Create a 16:9 horizontal key visual for Day1 Page 3 of a Japanese junior high school grade 8 entrepreneurship workshop.

This is a discovery-game learning screen, not a business poster, not a shopping poster, and not a normal explanation slide.

Overall style:
- warm, original educational illustration
- calm, friendly, organized, lightly adventurous
- suitable for 1920x1080 Zoom sharing
- warm cream paper background, soft navy structure, muted coral accents, warm yellow discovery highlights, soft green value/help accents, pale blue organizing lines
- fully original characters only
- do not imitate any existing anime, manga, game, mascot, brand, artist, studio, or franchise

Page type:
Evidence Board - Money.

Learning message:
Money is a visible form of "thank you." Show money as a quiet sign that value reached someone, not as profit, status, or luxury.

Scene:
A warm Evidence Board is visible. A same-age student who was helped hands a small thank-you card to Yuu. Yuu attaches a thank-you card or value-arrived evidence card to the Evidence Board. A small receipt, tiny coin, or simple money sign card may appear only as a quiet record of value received. It must not dominate the image.

Yuu visual cues:
- original Japanese grade 8 student
- short neat dark hair
- casual blue top or hoodie
- detective notebook and pen
- curious, calm, observant

Required visual elements:
- Evidence Board
- Thank-you Card
- Value-arrived Evidence Card
- small money sign card, receipt, or one coin as a quiet sign
- Detective Note area
- Discovery Stamp slot as a learning record
- Quest Map area with the money/thank-you step emphasized
- clean blank area for later Japanese headline overlay

Character action:
Yuu is actively pinning or placing the evidence card on the board while looking at the thank-you card. The helped student looks gently relieved. Hands and card exchange should be visible and natural.

Learner action shown:
The learner can see that they should think of something people pay for by asking what helpful change it gave someone.

Visible flow:
1. value reaches someone
2. thank-you appears
3. money is recorded as a small visible sign

Text handling:
- Do not generate long Japanese text.
- Exact Japanese headline, labels, and note text will be added later in layout.
- Blank cards or very short placeholder labels are acceptable.

Safety:
- money is a sign of gratitude, not a reward or status
- no pressure to earn money
- no money piles, cash rain, gold bars, luxury goods, expensive watches, rich lifestyle, profit celebration, ranking, score, trophy, prize, or reward bait

Negative prompt:
existing anime style, manga franchise style, game character style, mascot style, specific artist imitation, brand logos, copyrighted character resemblance, money piles, cash rain, gold bars, luxury car, expensive watch, shopping trophy, profit celebration, winner/loser, score, ranking, trophy, prize, level-up reward, Yuu standing without action, face-only icon, floating thank-you card, duplicate coins, random money props, broken hands, impossible fingers, broken Japanese paragraphs, tiny unreadable text
```

## 3. 生成後に見るべきチェック項目

- Evidence Boardに見えるか。
- 「価値が届く -> ありがとう -> お金のサイン」の流れが見えるか。
- お金が小さな記録であり、主役になっていないか。
- ユウがカードを貼る、見る、メモするなどの行動をしているか。
- 助かった人が自然にありがとうを渡しているか。
- 手、カード、ピン、ノート、コイン/レシートが自然につながっているか。
- 小物が浮いたり増殖したりしていないか。
- 日本語本文を後載せできる余白があるか。
- お金煽り、報酬化、勝敗、採点、ランキングがないか。
- 既存IPや特定作品に似ていないか。

## 4. NGなら使う修正プロンプトテンプレート

```text
Revise the Day1 Page 3 Evidence Board image while keeping the same warm discovery-game educational style.

Keep:
- Evidence Board
- Yuu pinning or placing a thank-you / value-arrived evidence card
- a helped student gently handing a thank-you card
- a small, quiet money sign as a record of value received
- 16:9 Zoom-friendly layout

Fix:
- [insert specific broken prop, confusing flow, or money-hype issue]

Clarify:
- money is a small sign of gratitude, not profit or status
- Yuu's hand connects naturally to the evidence card or board
- thank-you card exchange is easy to understand
- leave clean blank areas for exact Japanese text overlay

Remove:
- money piles, luxury goods, duplicate coins, floating cards
- broken Japanese paragraphs
- score, ranking, trophy, reward-like elements
- any resemblance to existing characters, anime, manga, games, mascots, brands, or artist styles
```

## 5. ファイル保存先の指示

生成画像はfinalにしないでください。candidateとして保存します。

推奨保存先:

```text
assets/generated/day1/page_03/candidates/day1_page_03_candidate_YYYYMMDD_01.png
```

代替保存先:

```text
outputs/day1/image_generation/candidates/day1_page_03_candidate_YYYYMMDD_01.png
```

## 6. Codexへ戻すときの報告テンプレート

`outputs/day1/image_generation/user_handoff_template.md` を使ってください。

```text
page_id: day1_page_03
prompt_packet: outputs/day1/image_generation/prompt_packets/day1_page_03_prompt_packet_for_gpt.md
candidate_filename:
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
