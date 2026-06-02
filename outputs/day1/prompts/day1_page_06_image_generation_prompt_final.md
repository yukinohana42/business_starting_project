# Day1 Page 6 Image Generation Prompt Final

## Purpose

Page 6: Final Mission Sheet の画像生成用prompt。

このpromptは、生成後レビュー、修正prompt、再生成、final判定を前提にする。最初の生成物は `candidate` であり、finalではない。

## Source Prompts To Use

Prepend:

1. `outputs/day1/prompts/day1_visual_anchor_prompt.md`
2. `outputs/day1/prompts/day1_character_prompt.md`
3. This Page 6 prompt

## Page Prompt

Create a 16:9 horizontal key visual for Day1 Page 6 of a Japanese junior high school grade 8 workshop. Keep the same warm discovery-game world as the approved Page 1 and Page 2 directions.

Page type: Final Mission Sheet.

Learning message: say the true shape of work in your own words.

Scene: A large Final Mission Sheet lies on a table. Yuu or Sora writes into a large blank sentence area. Miho gently offers a Question Card that helps the learner think, without giving the answer. A few previous Evidence Cards and Discovery Stamps are placed nearby as learning records.

Required sentence area:

- "仕事とは、＿＿を＿＿に変えること。"

The generated image should leave a large clean blank space where this sentence can be overlaid exactly later.

Character action: Yuu or Sora is writing. Miho holds out a Question Card. The posture should feel reflective and calm, not judged or scored.

Required visual elements:

- Final Mission Sheet
- large blank sentence area
- Question Card from Miho
- Detective Note or previous Evidence Cards nearby
- Reflection Stamp or Discovery Stamp as learning record
- Quest Map with the "Summary" step emphasized
- clean overlay area for headline and exact Japanese sentence

Learner action shown: the learner can see that they should write one sentence in their own words.

Visible change: seeing work vaguely -> seeing who changes and how.

## Text Handling

- Generated Japanese should be minimal.
- Leave space for "仕事の正体を、自分の言葉で言う。"
- Leave a large blank sentence area for exact overlay of "仕事とは、＿＿を＿＿に変えること。"
- The Question Card may be blank or use a very short placeholder.
- Do not generate long Japanese paragraphs.

## Prop Rules

- The writing pen must connect naturally to the writer's hand.
- The Final Mission Sheet must be on a table or held clearly.
- Miho's Question Card must be in Miho's hand and not floating.
- Evidence Cards and stamps should be nearby as learning records, not rewards.
- Do not create score marks, grade marks, trophy symbols, prize badges, or winner icons.
- Do not duplicate pens, cards, stamps, or notebooks unnecessarily.

## Safety And Tone

- No scoring, grading, judgment, or success/failure mark.
- Final Mission is a learning record, not a reward.
- Miho is a supportive navigator, not a teacher giving the answer.
- The mood should be calm, reflective, and encouraging.
- No money hype, competition, rank, trophy, or pressure to become an entrepreneur.
- Fully original characters only. Do not imitate existing IP or specific artist styles.

## Negative Prompt

- grading sheet
- red score marks
- correct/incorrect stamp
- trophy, reward, winner, level-up
- teacher judging student
- parent judge panel
- face-only characters
- floating Question Card
- pen not connected to hand
- duplicated props
- broken hands, impossible fingers, confusing arms
- generated long Japanese paragraphs
- broken Japanese used as final text
- money hype
- startup pressure
- existing character resemblance

## Candidate Review Checklist

After generation, review the actual image before finalizing.

- Final Mission Sheetとして見えるか。
- 「仕事とは、＿＿を＿＿に変えること。」の後載せ余白が十分か。
- ユウまたはソラが書き込んでいることがわかるか。
- ミホが問いカードで支えており、正解を教える先生に見えないか。
- 採点感、合否、報酬感がないか。
- これまでのEvidence CardやDiscovery Stampが学びの記録として見えるか。
- Quest Mapの「まとめ」ステップが機能しているか。
- ペン、カード、シート、スタンプが自然につながっているか。
- 日本語文字が崩れていないか。
- どの文字を後載せするべきか。

## Correction Prompt Template

Use this if the candidate is close but not final:

```text
Revise the Day1 Page 6 Final Mission Sheet image while keeping the approved warm discovery-game style.

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

Leave clean blank areas for exact Japanese text overlay.
```

## Adoption Rule

The first generated image is saved as `candidate`, not `final`.

Only after visual review and human approval may it be moved to `final`.
