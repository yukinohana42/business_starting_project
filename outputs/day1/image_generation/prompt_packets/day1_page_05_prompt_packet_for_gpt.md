# Day1 Page 05 Prompt Packet For GPT

## 1. 使用目的

Day1 Page 5「ビジネス探偵ミッション」を、GPT画像生成で1枚ずつcandidate生成するための手渡しパケットです。

このページはBusiness Detective Case Fileです。3つの身近な例から「誰が、どう変わるか」を観察します。YouTuberとラーメン屋はこのページには入れません。

## 2. 画像生成に貼る最終プロンプト

```text
Create a 16:9 horizontal key visual for Day1 Page 5 of a Japanese junior high school grade 8 entrepreneurship workshop.

This is a discovery-game learning screen, not a normal example list, not a ranking board, and not a business poster.

Overall style:
- warm, original educational illustration
- calm, friendly, organized, lightly adventurous
- suitable for 1920x1080 Zoom sharing
- warm cream paper background, soft navy structure, muted coral accents, warm yellow discovery highlights, soft green value/help accents, pale blue organizing lines
- fully original characters only
- do not imitate any existing anime, manga, game, mascot, brand, artist, studio, or franchise

Page type:
Business Detective Case File.

Learning message:
This work changes whom, and how?

Scene:
A large Business Detective Case File board is open. Three Evidence Cards are attached to the board with pins, tape, or connecting lines. Yuu observes the board with a detective notebook. Sora pins, moves, or writes one evidence card. The board should feel like a case investigation, not a normal list of examples.

Three evidence examples:
1. Convenience store: rushed person -> can buy quickly and feels helped
2. Tutoring / learning support: confused learner -> feels able to try
3. Smartphone game: bored time -> fun time

Smartphone game rule:
Show only a small, safe everyday entertainment example. Do not suggest addiction, gambling, gacha, payment pressure, monetization, or brand/game resemblance.

Yuu visual cues:
- original Japanese grade 8 student
- short neat dark hair
- casual blue top or hoodie
- detective notebook and pen
- optional magnifying glass only if clearly held or resting naturally

Sora visual cues:
- original Japanese grade 8 student
- medium dark hair with simple silhouette
- casual green or teal top
- sticky notes, cards, marker pen
- pins, moves, or writes an evidence card

Required visual elements:
- Business Detective Case File
- exactly three Evidence Cards
- Detective Note
- Discovery Stamp slot as a learning record
- pins, tape, or connecting lines
- Quest Map area with the case step emphasized
- clean overlay area for later Japanese headline and exact card labels

Character action:
Yuu inspects the Evidence Cards. Sora actively pins or writes one card. Both characters support the investigation.

Learner action shown:
The learner can see that they should choose one evidence card and say who changes and how.

Text handling:
- Do not generate long Japanese text.
- Exact Japanese labels and example text will be added later in layout.
- Evidence Cards may use blank areas or very short placeholder labels.

Safety:
- do not rank the three examples
- do not imply one job is superior
- do not show money or profit as the point
- no YouTuber or ramen shop on this main page
- no score, winner, trophy, prize, reward, or business pressure

Negative prompt:
existing anime style, manga franchise style, game character style, mascot style, specific artist imitation, brand logos, copyrighted character resemblance, plain three-example explanation slide, five or more crowded example cards, YouTuber, ramen shop, job ranking, score, winner, trophy, money hype, profit celebration, smartphone addiction, gacha, gambling, payment pressure, existing game resemblance, face-only characters, Yuu or Sora standing without action, floating evidence cards, duplicated props, broken hands, impossible fingers, generated long Japanese paragraphs, broken Japanese used as final text
```

## 3. 生成後に見るべきチェック項目

- Business Detective Case Fileに見えるか。
- 3例だけになっているか。
- YouTuberとラーメン屋が入っていないか。
- 3例がランキングや優劣に見えないか。
- 各Evidence Cardから「誰が、どう変わるか」が見えるか。
- ユウとソラが観察、貼る、書くなどの行動をしているか。
- スマホゲームが依存、課金、ガチャ、ギャンブル、既存ゲーム風に見えないか。
- 小物、カード、ピン、ノート、ペンが自然につながっているか。
- 日本語本文を後載せできる余白があるか。
- お金煽り、勝敗、採点、報酬化がないか。
- 既存IPや特定作品に似ていないか。

## 4. NGなら使う修正プロンプトテンプレート

```text
Revise the Day1 Page 5 Business Detective Case File image while keeping the same warm discovery-game educational style.

Keep:
- large Case File board
- exactly three Evidence Cards: convenience store, tutoring / learning support, smartphone game
- Yuu observing and Sora pinning or writing a card
- 16:9 Zoom-friendly layout

Fix:
- [insert specific issue: static list, unclear action, floating cards, smartphone risk, broken text]

Clarify:
- each Evidence Card shows who changes and how
- smartphone game is safe everyday fun, not addiction or payment pressure
- cards are investigation evidence, not ranking cards
- leave clean blank areas for exact Japanese text overlay

Remove:
- YouTuber, ramen shop, extra examples
- money hype, ranking, score, trophy, reward, job superiority
- floating props, duplicated props, broken Japanese
- any existing game, character, anime, manga, mascot, brand, or artist resemblance
```

## 5. ファイル保存先の指示

生成画像はfinalにしないでください。candidateとして保存します。

推奨保存先:

```text
assets/generated/day1/page_05/candidates/day1_page_05_candidate_YYYYMMDD_01.png
```

代替保存先:

```text
outputs/day1/image_generation/candidates/day1_page_05_candidate_YYYYMMDD_01.png
```

## 6. Codexへ戻すときの報告テンプレート

```text
page_id: day1_page_05
prompt_packet: outputs/day1/image_generation/prompt_packets/day1_page_05_prompt_packet_for_gpt.md
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
