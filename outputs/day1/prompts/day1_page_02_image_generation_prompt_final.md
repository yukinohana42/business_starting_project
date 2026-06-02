# Day1 Page 2 Image Generation Prompt Final

## Purpose

Page 2: Case File - Work の画像生成用prompt。

このpromptは、生成後レビュー、修正prompt、再生成、final判定を前提にする。最初の生成物は `candidate` であり、finalではない。

## Source Prompts To Use

Prepend:

1. `outputs/day1/prompts/day1_visual_anchor_prompt.md`
2. `outputs/day1/prompts/day1_character_prompt.md`
3. This Page 2 prompt

## Page 2 Prompt

Create a 16:9 horizontal key visual for Day1 Page 2 of a Japanese junior high school grade 8 workshop. Keep the same world, warmth, character direction, and discovery-game style as the approved Day1 Page 1 Mission Board direction sample.

Page type: Case File - Work.

Learning message: work means making someone's state a little better. The image should show this through a small Before/After change, not through a long explanation.

Scene: A warm educational case file board is open on a table or wall. The case file contains two large panels: Before Card and After Card. In the Before Card, a same-age student is mildly troubled by a small everyday inconvenience. In the After Card, the same student looks slightly relieved because the situation became easier. The change should be modest and believable.

Yuu / Value Detective is observing the Before/After cards. Yuu is either pointing from Before to After or writing a short observation in a detective notebook. Yuu's hand action, gaze, pen, notebook, and the cards should connect naturally. Props must be physically meaningful and not floating.

Required visual elements:

- Case File board
- Before Card
- After Card
- Detective Note
- Discovery Stamp slot
- Quest Map with the "Observation" step emphasized
- clear blank spaces for later Japanese text overlay

Learner action shown: the learner can see that they should compare the two states and say one example of something that became easier.

Visible change: 困っている人 -> 少し助かった人.

Text handling:

- Generated Japanese should be minimal.
- A large headline area may be left for "仕事は、誰かの状態を少し良くすること。"
- Use blank or very short placeholder labels on cards if needed.
- Exact Japanese body text, labels, and questions will be added later in layout.

Prop rules:

- Use props only when they support the learning action.
- Magnifying glass may appear only if Yuu clearly holds it or if it rests naturally on the table.
- Pen must connect to hand or notebook.
- Detective notebook must be held or placed clearly on the table.
- Do not create duplicate magnifying glasses, extra pens, floating cards, or props emerging from the face/body.

Safety and tone:

- Before state must not be mocked.
- After state must not look like a huge success, victory, prize, or reward.
- No money piles, luxury goods, ranking, score, trophy, winner/loser, or business pressure.
- Fully original characters only; do not imitate existing anime, manga, game, mascot, artist, studio, brand, or franchise.

Output:

- 16:9 horizontal
- warm hand-drawn educational illustration
- clean composition for Zoom sharing
- page should feel like a Case File screen, not a generic explanation slide

## Negative Prompt

- face-only icon
- Yuu standing still without action
- floating magnifying glass
- duplicate props
- props attached to face, hair, torso, or background with no meaning
- broken hands, impossible fingers, confusing arm positions
- card text too tiny to review
- generated long Japanese paragraphs
- broken Japanese used as final text
- Before person being mocked
- After person celebrating victory
- money hype
- competition, score, rank, trophy, reward
- startup pitch poster
- existing character resemblance

## Candidate Review Checklist

After generation, review the actual image before finalizing.

- Beforeが笑いものになっていないか。
- Afterが大成功、勝利、報酬に見えないか。
- ユウが観察していることがわかるか。
- Case Fileとして見えるか。
- Before/Afterの変化がわかるか。
- 小物が意味不明な位置に出ていないか。
- 虫眼鏡、ペン、ノート、カードなどが手や机上と自然につながっているか。
- 日本語文字が崩れていないか。
- 画像生成だけに任せず後載せすべき文字があるか。
- Quest Mapの観察ステップが学習進行として見えるか。
- Discovery Stampが報酬ではなく発見記録に見えるか。

## Correction Prompt Template

Use this if the candidate is close but not final:

```text
Revise the Day1 Page 2 Case File image while keeping the approved warm discovery-game style and Yuu's age-appropriate original character design.

Keep:
- Case File board with Before Card and After Card
- Yuu observing the change
- warm hand-drawn educational style
- 16:9 Zoom-friendly layout

Fix:
- [insert specific broken prop or confusing depiction]

Clarify:
- Yuu's hand should clearly point to the Before/After cards or write in the detective notebook
- props must connect naturally to hands, table, or board
- Before state is mild and respectful
- After state is a small helpful change, not a victory

Remove:
- floating or duplicated props
- broken Japanese paragraphs
- any money hype, score, ranking, trophy, or reward-like elements

Leave clean blank areas for exact Japanese text overlay.
```

## Adoption Rule

The first generated image is saved as `candidate`, not `final`.

Only after visual review and human approval may it be moved to `final`.
