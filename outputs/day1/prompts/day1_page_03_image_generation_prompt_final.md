# Day1 Page 3 Image Generation Prompt Final

## Purpose

Page 3: Evidence Board - Money の画像生成用prompt。

このpromptは、生成後レビュー、修正prompt、再生成、final判定を前提にする。最初の生成物は `candidate` であり、finalではない。

## Source Prompts To Use

Prepend:

1. `outputs/day1/prompts/day1_visual_anchor_prompt.md`
2. `outputs/day1/prompts/day1_character_prompt.md`
3. This Page 3 prompt

## Page Prompt

Create a 16:9 horizontal key visual for Day1 Page 3 of a Japanese junior high school grade 8 workshop. Keep the same warm discovery-game world as the approved Page 1 Mission Board and Page 2 Case File directions.

Page type: Evidence Board - Money.

Learning message: money is a visible form of "thank you." The image should show money as a quiet sign that value reached someone, not as profit or luxury.

Scene: A warm evidence board is visible. A same-age student who was helped hands a small thank-you card to Yuu. Yuu attaches the thank-you card or value-arrived evidence card to the Evidence Board. A small money sign, receipt, or one simple coin may appear as a tiny record of value received. It should not dominate the image.

Character action: Yuu is actively pinning or placing the evidence card on the board while looking at the thank-you card. The helped student looks gently relieved. Hands and card exchange should be visible and natural.

Required visual elements:

- Evidence Board
- Thank-you Card
- Value-arrived Evidence Card
- small Money Sign Card, receipt, or one coin as a quiet sign
- Detective Note area
- Discovery Stamp slot
- Quest Map with the "Money" step emphasized
- open blank area for later Japanese headline overlay

Learner action shown: the learner can see that they should think of a paid thing by asking what helpful change it gave someone.

Visible flow:

1. value reaches someone
2. thank-you appears
3. money is recorded as a small sign

## Text Handling

- Generated Japanese should be minimal.
- Leave a clear headline area for "お金は「ありがとう」が見える形。"
- Use blank cards or very short placeholder labels if needed.
- Exact Japanese explanation, card text, Quest Map labels, and note text will be added later in layout.
- Do not ask image generation to write long Japanese sentences.

## Prop Rules

- The thank-you card must be held, handed, or pinned clearly.
- A coin, receipt, or money sign may appear only as a small supporting record.
- Do not create money piles, cash rain, luxury objects, shopping trophies, or rich lifestyle props.
- Pins, cards, notebook, and pen must connect naturally to hands, board, or table.
- Do not create floating cards, duplicate coins, or props emerging from faces or bodies.

## Safety And Tone

- Money is a sign of value received, not a reward or status.
- The helped person should look mildly relieved, not worshipful or overly grateful.
- No pressure to earn money.
- No winner/loser, score, ranking, trophy, level-up, or reward framing.
- Fully original characters only. Do not imitate existing anime, manga, games, mascots, studios, brands, franchises, or artists.

## Negative Prompt

- money piles
- cash rain
- gold bars
- luxury car, luxury watch, expensive goods
- profit celebration
- winner/loser
- score board, ranking, trophy, prize, level-up reward
- business seminar poster
- Yuu standing without action
- face-only icon
- floating thank-you card
- duplicate coins or random money props
- broken hands, impossible fingers, confusing arm positions
- generated long Japanese paragraphs
- broken Japanese used as final teaching text
- existing character resemblance

## Candidate Review Checklist

After generation, review the actual image before finalizing.

- お金が「ありがとうが見える形」として扱われているか。
- お金の束、高級品、儲け煽りに見えないか。
- ユウがEvidence Boardにカードを貼る、または観察していることがわかるか。
- 助かった人がありがとうカードを渡す場面が自然か。
- 価値が届く -> ありがとう -> お金のサイン、の流れが見えるか。
- Quest Mapの「お金」ステップが学習進行として見えるか。
- 小物が意味不明な位置に出ていないか。
- カード、ペン、ノート、コイン、レシートが手や机上、ボードと自然につながっているか。
- 日本語文字が崩れていないか。
- どの文字を後載せするべきか。

## Correction Prompt Template

Use this if the candidate is close but not final:

```text
Revise the Day1 Page 3 Evidence Board image while keeping the approved warm discovery-game style.

Keep:
- Evidence Board
- Yuu pinning or placing a thank-you / value-arrived evidence card
- a helped student gently handing a thank-you card
- small, quiet money sign as a record of value received
- 16:9 Zoom-friendly layout

Fix:
- [insert specific broken prop, confusing flow, or money-hype issue]

Clarify:
- money is a small sign of gratitude, not profit
- Yuu's hand connects naturally to the evidence card or board
- thank-you card exchange is easy to understand

Remove:
- money piles, luxury goods, duplicate coins, floating cards
- broken Japanese paragraphs
- score, ranking, trophy, reward-like elements

Leave clean blank areas for exact Japanese text overlay.
```

## Adoption Rule

The first generated image is saved as `candidate`, not `final`.

Only after visual review and human approval may it be moved to `final`.
