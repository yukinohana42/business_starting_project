# Day1 Page 02 Prompt Packet For GPT

## 1. 使用目的

Day1 Page 2「仕事とは何か」を、GPT画像生成で1枚ずつcandidate生成するための手渡しパケットです。

このページはCase File - Workです。「仕事は、誰かの状態を少し良くすること」をBefore/Afterで見せます。画像はfinalではなくcandidateとして扱います。

## 2. 画像生成に貼る最終プロンプト

```text
Create a 16:9 horizontal key visual for Day1 Page 2 of a Japanese junior high school grade 8 entrepreneurship workshop.

This is a discovery-game learning screen, not a normal explanation slide and not a business poster.

Overall style:
- warm, original educational illustration
- calm, friendly, organized, lightly adventurous
- suitable for 1920x1080 Zoom sharing
- warm cream paper background, soft navy structure, muted coral accents, warm yellow discovery highlights, soft green value/help accents, pale blue organizing lines
- fully original characters only
- do not imitate any existing anime, manga, game, mascot, brand, artist, studio, or franchise

Page type:
Case File - Work.

Learning message:
Work means making someone's state a little better. Show this through a small Before/After change, not through long explanation text.

Scene:
A warm educational case file board is open on a table or wall. The case file contains two large panels: Before Card and After Card. In the Before Card, a same-age student is mildly troubled by a small everyday inconvenience. In the After Card, the same student looks slightly relieved because the situation became easier.

Yuu, the original grade 8 Value Detective, observes the Before/After cards. Yuu points from Before to After or writes a short observation in a detective notebook.

Yuu visual cues:
- short neat dark hair
- casual blue top or hoodie
- navy or dark pants
- detective notebook and pen
- optional small magnifying glass only if clearly held or resting naturally on the table

Required visual elements:
- Case File board
- Before Card
- After Card
- Detective Note
- Discovery Stamp slot as a learning record, not a reward
- Quest Map area with the observation step emphasized
- clean blank areas for later Japanese headline and question overlay

Character action:
Yuu's hand action, gaze, pen, notebook, and the cards should connect naturally. Yuu must be observing or comparing, not standing still.

Learner action shown:
The learner can see that they should compare the two states and say one everyday example where something became easier.

Visible change:
A respectful small change: mildly troubled -> slightly helped / relieved. Do not mock the Before person. Do not make After a big success, victory, prize, or reward.

Text handling:
- Do not generate long Japanese text.
- Exact Japanese headline, labels, and question will be added later in layout.
- Blank cards or very short placeholder labels are acceptable.

Safety:
- no money piles, luxury goods, ranking, score, trophy, winner/loser framing, reward bait, or business pressure
- no laughing at the troubled person
- no dramatic victory pose

Negative prompt:
existing anime style, manga franchise style, game character style, mascot style, specific artist imitation, brand logos, copyrighted character resemblance, face-only Yuu, Yuu standing still, floating magnifying glass, duplicated pens or cards, props emerging from face or body, broken hands, impossible fingers, Before person being mocked, After person celebrating victory, money hype, score, ranking, trophy, prize, reward, broken Japanese paragraphs, tiny unreadable text
```

## 3. 生成後に見るべきチェック項目

- Case Fileに見えるか。
- Before/Afterの変化が「困っている -> 少し助かった」として読めるか。
- Beforeを笑いものにしていないか。
- Afterが勝利、成功、報酬に見えないか。
- ユウが観察または比較しているか。
- 手、ノート、ペン、カードが自然につながっているか。
- 小物が浮いたり増殖したりしていないか。
- 日本語本文を後載せできる余白があるか。
- 起業押し付け、お金煽り、勝敗、採点、ランキングがないか。
- 既存IPや特定作品に似ていないか。

## 4. NGなら使う修正プロンプトテンプレート

```text
Revise the Day1 Page 2 Case File image while keeping the same warm discovery-game educational style.

Keep:
- Case File board with Before Card and After Card
- Yuu observing or comparing the change
- Detective Note, Quest Map, and Discovery Stamp slot
- 16:9 Zoom-friendly layout

Fix:
- [insert specific issue]

Clarify:
- Yuu's hand should clearly point to the Before/After cards or write in the detective notebook
- Before state is mild and respectful
- After state is a small helpful change, not a victory
- leave clean blank areas for exact Japanese overlay text

Remove:
- floating or duplicated props
- broken Japanese text
- money hype, score, ranking, trophy, reward-like elements
- any resemblance to existing characters, anime, manga, games, mascots, brands, or artist styles
```

## 5. ファイル保存先の指示

生成画像はfinalにしないでください。candidateとして保存します。

推奨保存先:

```text
assets/generated/day1/page_02/candidates/day1_page_02_candidate_YYYYMMDD_01.png
```

代替保存先:

```text
outputs/day1/image_generation/candidates/day1_page_02_candidate_YYYYMMDD_01.png
```

## 6. Codexへ戻すときの報告テンプレート

`outputs/day1/image_generation/user_handoff_template.md` を使ってください。

```text
page_id: day1_page_02
prompt_packet: outputs/day1/image_generation/prompt_packets/day1_page_02_prompt_packet_for_gpt.md
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
