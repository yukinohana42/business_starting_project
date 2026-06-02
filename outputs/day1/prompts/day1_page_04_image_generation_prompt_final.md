# Day1 Page 4 Image Generation Prompt Final

## Purpose

Page 4: Card Table - Value の画像生成用prompt。

このpromptは、生成後レビュー、修正prompt、再生成、final判定を前提にする。最初の生成物は `candidate` であり、finalではない。

## Source Prompts To Use

Prepend:

1. `outputs/day1/prompts/day1_visual_anchor_prompt.md`
2. `outputs/day1/prompts/day1_character_prompt.md`
3. This Page 4 prompt

## Page Prompt

Create a 16:9 horizontal key visual for Day1 Page 4 of a Japanese junior high school grade 8 workshop. Keep the same warm discovery-game world as Page 1 and Page 2.

Page type: Card Table - Value.

Learning message: value is seen through the other person's change.

Scene: Yuu and Sora work together at a table. On the table are several Value Change Cards with Before and After spaces. Yuu points at one card, and Sora writes or moves a sticky note on another card. The table should feel like an active learning workspace, not a static three-card explanation slide.

Required card ideas:

- troubled -> helped
- confused -> can try
- bored -> fun

Character action: Yuu compares Before and After. Sora arranges or fills in the cards. Hands, pens, sticky notes, notebook, and card edges should be visible and naturally connected.

Required visual elements:

- Card Table
- Value Change Cards
- sticky notes
- pen and notebook
- Discovery Stamp slot
- Quest Map with the "Value Cards" step emphasized
- clean overlay area for headline and short labels

Learner action shown: the learner can see that they should choose one card and connect Before to After.

## Text Handling

- Generated Japanese should be minimal.
- Leave a headline area for "価値は、相手の変化で見る。"
- Card text can be blank or simple placeholders.
- Exact Japanese card labels and instructions will be added later in layout.
- Avoid long generated Japanese text.

## Prop Rules

- Pens should connect to hands or rest clearly on the table.
- Sticky notes should be on the cards, table, or in Sora's hand.
- Cards should be large enough to understand as work materials.
- Do not make cards float.
- Do not duplicate pens, notes, stamps, or cards unnecessarily.
- Do not cover faces, hands, or key card surfaces with props.

## Safety And Tone

- Before states should be respectful and not mocked.
- After states should be small positive changes, not victory poses.
- No money hype, ranking, score, trophy, competition, or reward.
- The scene should feel like collaborative discovery, not a game contest.
- Fully original characters only. Do not imitate existing IP or specific artist styles.

## Negative Prompt

- static three-card slide with no hands or action
- face-only Yuu or Sora
- characters standing without working
- floating cards or sticky notes
- duplicated pens, stamps, notes
- props emerging from face or body
- broken hands, impossible fingers, confusing arm positions
- generated long Japanese paragraphs
- Before person being mocked
- After as victory celebration
- score, rank, trophy, reward, level-up
- money hype
- existing character resemblance

## Candidate Review Checklist

After generation, review the actual image before finalizing.

- Card Tableとして見えるか。
- ただの3枚カード並びではなく、作業中の場面に見えるか。
- ユウとソラがカードを並べる、指差す、書くなどの行動をしているか。
- 「困った -> 助かった」「わからない -> できそう」「退屈 -> 楽しい」の変化が読み取れるか。
- 手元、付箋、カード、ペン、ノートが自然につながっているか。
- Quest Mapの「価値カード」ステップが機能しているか。
- スタンプが報酬ではなく発見記録に見えるか。
- 日本語文字が崩れていないか。
- どの文字を後載せするべきか。

## Correction Prompt Template

Use this if the candidate is close but not final:

```text
Revise the Day1 Page 4 Card Table image while keeping the approved warm discovery-game style.

Keep:
- Yuu and Sora working at a card table
- Value Change Cards with Before and After spaces
- hands, sticky notes, pen, notebook, and discovery stamp slot
- 16:9 Zoom-friendly layout

Fix:
- [insert specific static layout, broken hand, floating prop, or unclear card issue]

Clarify:
- Yuu points to a card
- Sora writes or places a sticky note
- cards are learning tools, not decorative cards
- changes are small and respectful

Remove:
- static explanation-slide feel
- floating props, duplicate props, broken Japanese
- money hype, score, ranking, trophy, reward-like elements

Leave clean blank areas for exact Japanese text overlay.
```

## Adoption Rule

The first generated image is saved as `candidate`, not `final`.

Only after visual review and human approval may it be moved to `final`.
