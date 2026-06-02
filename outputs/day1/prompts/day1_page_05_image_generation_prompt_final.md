# Day1 Page 5 Image Generation Prompt Final

## Purpose

Page 5: Business Detective Case File の画像生成用prompt。

このpromptは、生成後レビュー、修正prompt、再生成、final判定を前提にする。最初の生成物は `candidate` であり、finalではない。

## Source Prompts To Use

Prepend:

1. `outputs/day1/prompts/day1_visual_anchor_prompt.md`
2. `outputs/day1/prompts/day1_character_prompt.md`
3. This Page 5 prompt

## Page Prompt

Create a 16:9 horizontal key visual for Day1 Page 5 of a Japanese junior high school grade 8 workshop. Keep the same warm discovery-game world as the approved Page 1 and Page 2 directions.

Page type: Business Detective Case File.

Learning message: this work changes whom, and how?

Scene: A large Business Detective Case File board is open. Three Evidence Cards are attached to the board with pins or tape. Yuu observes the board with a detective notebook. Sora pins, moves, or writes one evidence card. The board should feel like a case investigation, not a normal list of examples.

Three evidence examples:

1. Convenience store: rushed person -> can buy quickly and feels helped
2. Tutoring / learning support: confused learner -> feels able to try
3. Smartphone game: bored time -> fun time

Smartphone game rule: show only a small, safe everyday entertainment example. Do not suggest addiction, gambling, gacha, payment pressure, or monetization.

Required visual elements:

- Business Detective Case File
- three Evidence Cards
- Detective Note
- Discovery Stamp slot
- pins, tape, or connecting lines
- Quest Map with the "Case" step emphasized
- clean overlay area for headline and exact Japanese labels later

Learner action shown: the learner can see that they should choose one evidence card and say who changes and how.

## Text Handling

- Generated Japanese should be minimal.
- Leave headline space for "この仕事は、誰をどう変えている？"
- Evidence Cards may use blank areas or very short placeholder labels.
- Exact Japanese example text will be added later in layout.
- Do not generate long Japanese paragraphs.

## Prop Rules

- Evidence Cards must be pinned, held, or clearly placed on the case file board.
- Yuu's notebook, pen, or optional magnifying glass must connect naturally to hands or table.
- Sora's hand should clearly pin, move, or write a card.
- Do not create floating cards, duplicated magnifying glasses, random money props, or props emerging from faces or bodies.
- Cards should not cover faces or key hand actions.

## Safety And Tone

- Do not rank the three examples.
- Do not imply one job is superior.
- Do not show money or profit as the point of the examples.
- Do not make smartphone game about addiction, payment, gambling, or reward loops.
- Keep the tone curious and observational.
- Fully original characters only. Do not imitate existing IP, games, anime, manga, studios, brands, franchises, or artists.

## Negative Prompt

- plain three-example explanation slide
- five or more crowded example cards
- YouTuber or ramen shop on this page
- job ranking, score, winner, trophy
- money hype or profit celebration
- smartphone addiction, gacha, gambling, payment pressure
- face-only characters
- Yuu or Sora standing without action
- floating evidence cards
- duplicated props
- broken hands, impossible fingers, confusing arms
- generated long Japanese paragraphs
- broken Japanese used as final text
- existing character or game resemblance

## Candidate Review Checklist

After generation, review the actual image before finalizing.

- Business Detective Case Fileとして見えるか。
- Evidence Cardを貼る、選ぶ、メモする動作が見えるか。
- ただの3例一覧になっていないか。
- 3例が「誰が、どう変わるか」として見えるか。
- スマホゲームが依存や課金を連想させず、退屈な時間が楽しい時間になる程度に限定されているか。
- Quest Mapの「ケース」ステップが機能しているか。
- 小物、カード、ピン、ノート、ペンが自然につながっているか。
- お金や職業ランキングに見えないか。
- 日本語文字が崩れていないか。
- どの文字を後載せするべきか。

## Correction Prompt Template

Use this if the candidate is close but not final:

```text
Revise the Day1 Page 5 Business Detective Case File image while keeping the approved warm discovery-game style.

Keep:
- large Case File board
- three Evidence Cards: convenience store, tutoring / learning support, smartphone game
- Yuu observing and Sora pinning or writing a card
- 16:9 Zoom-friendly layout

Fix:
- [insert specific issue: static list, unclear action, floating cards, smartphone risk, broken text]

Clarify:
- each Evidence Card shows who changes and how
- smartphone game is safe everyday fun, not addiction or payment pressure
- cards are investigation evidence, not ranking cards

Remove:
- money hype, ranking, score, trophy, reward, job superiority
- floating props, duplicated props, broken Japanese
- any existing game or character resemblance

Leave clean blank areas for exact Japanese text overlay.
```

## Adoption Rule

The first generated image is saved as `candidate`, not `final`.

Only after visual review and human approval may it be moved to `final`.
