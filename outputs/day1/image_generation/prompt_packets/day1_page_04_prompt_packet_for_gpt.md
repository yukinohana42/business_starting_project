# Day1 Page 04 Prompt Packet For GPT

## 1. 使用目的

Day1 Page 4「価値とは何か」を、GPT画像生成で1枚ずつcandidate生成するための手渡しパケットです。

このページはCard Table - Valueです。「価値は、相手の変化で見る」を、ユウとソラが価値変換カードを作る場面で見せます。

## 2. 画像生成に貼る最終プロンプト

```text
Create a 16:9 horizontal key visual for Day1 Page 4 of a Japanese junior high school grade 8 entrepreneurship workshop.

This is a discovery-game learning screen, not a normal explanation slide.

Overall style:
- warm, original educational illustration
- calm, friendly, organized, lightly adventurous
- suitable for 1920x1080 Zoom sharing
- warm cream paper background, soft navy structure, muted coral accents, warm yellow discovery highlights, soft green value/help accents, pale blue organizing lines
- fully original characters only
- do not imitate any existing anime, manga, game, mascot, brand, artist, studio, or franchise

Page type:
Card Table - Value.

Learning message:
Value is seen through the other person's change.

Scene:
Yuu and Sora work together at a table. On the table are several large Value Change Cards with Before and After spaces. Yuu points at one card, and Sora writes or moves a sticky note on another card. The table should feel like an active learning workspace, not a static three-card explanation slide.

Yuu visual cues:
- original Japanese grade 8 student
- short neat dark hair
- casual blue top or hoodie
- detective notebook and pen
- observes and compares cards

Sora visual cues:
- original Japanese grade 8 student
- medium dark hair with simple silhouette
- casual green or teal top
- sticky notes, cards, marker pen
- builds and arranges ideas

Required visual elements:
- Card Table
- Value Change Cards with Before and After spaces
- sticky notes
- pen and notebook
- Discovery Stamp slot as a learning record
- Quest Map area with the value-card step emphasized
- clean overlay area for later Japanese headline and short labels

Card ideas to show visually, without relying on text:
- troubled -> helped
- confused -> able to try
- bored -> fun

Character action:
Yuu compares Before and After. Sora arranges or fills in the cards. Hands, pens, sticky notes, notebook, and card edges must be visible and naturally connected.

Learner action shown:
The learner can see that they should choose one card and connect Before to After.

Text handling:
- Do not generate long Japanese text.
- Exact Japanese headline and card labels will be added later in layout.
- Cards can be blank or use very short placeholder labels.

Safety:
- Before states are respectful and not mocked
- After states are small positive changes, not victory poses
- no money hype, ranking, score, trophy, competition, or reward
- collaborative discovery, not a game contest

Negative prompt:
existing anime style, manga franchise style, game character style, mascot style, specific artist imitation, brand logos, copyrighted character resemblance, static three-card slide with no hands or action, face-only Yuu or Sora, characters standing without working, floating cards or sticky notes, duplicated pens or stamps, props emerging from face or body, broken hands, impossible fingers, generated long Japanese paragraphs, Before person being mocked, After as victory celebration, score, rank, trophy, reward, level-up, money hype
```

## 3. 生成後に見るべきチェック項目

- Card Tableに見えるか。
- ただの3枚カード説明ではなく、作業中の場面に見えるか。
- ユウとソラがカードを比べる、書く、並べる行動をしているか。
- Before/Afterの変化が視覚的に読めるか。
- 手、付箋、カード、ペン、ノートが自然につながっているか。
- 小物が浮いたり増殖したりしていないか。
- 日本語本文を後載せできる余白があるか。
- 報酬、勝敗、採点、ランキング、お金煽りがないか。
- 既存IPや特定作品に似ていないか。

## 4. NGなら使う修正プロンプトテンプレート

```text
Revise the Day1 Page 4 Card Table image while keeping the same warm discovery-game educational style.

Keep:
- Yuu and Sora working at a card table
- Value Change Cards with Before and After spaces
- hands, sticky notes, pen, notebook, and Discovery Stamp slot
- 16:9 Zoom-friendly layout

Fix:
- [insert specific static layout, broken hand, floating prop, or unclear card issue]

Clarify:
- Yuu points to or compares a card
- Sora writes or places a sticky note
- cards are learning tools, not decorative cards
- changes are small and respectful
- leave clean blank areas for exact Japanese text overlay

Remove:
- static explanation-slide feel
- floating props, duplicate props, broken Japanese
- money hype, score, ranking, trophy, reward-like elements
- any resemblance to existing characters, anime, manga, games, mascots, brands, or artist styles
```

## 5. ファイル保存先の指示

推奨保存先:

```text
assets/generated/day1/page_04/candidates/day1_page_04_candidate_YYYYMMDD_01.png
```

代替保存先:

```text
outputs/day1/image_generation/candidates/day1_page_04_candidate_YYYYMMDD_01.png
```

## 6. Codexへ戻すときの報告テンプレート

```text
page_id: day1_page_04
prompt_packet: outputs/day1/image_generation/prompt_packets/day1_page_04_prompt_packet_for_gpt.md
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
