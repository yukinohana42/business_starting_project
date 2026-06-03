# Day1 Page 01 Prompt Packet For GPT

## 1. 使用目的

Day1 Page 1「今日のミッション」を、GPT画像生成で1枚ずつcandidate生成するための手渡しパケットです。

このページはMission Boardです。中学2年生が「今日は何を発見するのか」を一目でわかるようにします。画像はfinalではなくcandidateとして扱います。

## 2. 画像生成に貼る最終プロンプト

```text
Create a 16:9 horizontal key visual for Day1 Page 1 of a Japanese junior high school grade 8 entrepreneurship workshop.

This is not a business poster and not a normal explanation slide. It is a discovery-game learning screen where the student can see today's mission.

Overall style:
- warm, original educational illustration
- calm, friendly, organized, lightly adventurous
- suitable for 1920x1080 Zoom sharing
- warm cream paper background, soft navy structure, muted coral accents, warm yellow discovery highlights, soft green value/help accents, pale blue organizing lines
- fully original characters only
- do not imitate any existing anime, manga, game, mascot, brand, artist, studio, or franchise

Page type:
Mission Board.

Learning message:
The student is starting a mission to discover the true shape of money and work. The final learning goal is to write one sentence: "Work means changing ____ into ____." Do not render this Japanese sentence in the image. Leave a clean blank area for exact Japanese overlay text later.

Scene:
Yuu, an original Japanese grade 8 student and Value Detective, stands beside a warm wooden mission board. Yuu is actively writing in a detective notebook while holding or receiving a mission card. Yuu looks curious and calm, not childish and not overly mature.

Yuu visual cues:
- short neat dark hair
- casual blue top or hoodie
- navy or dark pants
- detective notebook and pen
- mission card
- optional small magnifying glass only if clearly held or naturally resting on the table

Required visual elements:
- Mission Board
- Mission Card
- Detective Note with blank lines
- Quest Map area showing the first step of a mission
- subtle Discovery Stamp slot as a record of discovery, not a reward
- a large clean headline area for later Japanese overlay
- a large clean final-sentence area for later Japanese overlay

Character action:
Show hands, pen, notebook, mission card, gaze, and posture. Yuu must be writing or checking the mission, not just standing.

Learner action shown:
The learner should understand: confirm the mission, look for value changes, and prepare to write the final sentence in their own words.

Visible change cue:
Show a small symbolic pair of cards suggesting the thinking shift from "work as getting money" to "work as seeing someone's positive change." Do not show cash piles.

Text handling:
- Do not generate long Japanese text.
- Do not rely on generated Japanese as final copy.
- Leave blank, clean areas for exact Japanese headline and final sentence overlay later.
- Very short English placeholder labels like "MISSION" or "NOTE" are acceptable if subtle.

Safety:
- no money piles, cash rain, luxury goods, winner/loser framing, score, ranking, trophy, prize, reward bait, business pressure, fear-based future warnings, or "you must become an entrepreneur" mood
- Discovery Stamp is a learning record, not a prize

Negative prompt:
existing anime style, manga franchise style, game character style, mascot style, specific artist imitation, brand logos, copyrighted character resemblance, face-only character icon, character standing still with no learning action, generic business poster, crowded explanation slide, money piles, luxury lifestyle, trophy, ranking, score, reward badge, floating magnifying glass, duplicated props, props emerging from face or body, broken hands, impossible fingers, broken Japanese text, tiny unreadable text
```

## 3. 生成後に見るべきチェック項目

- Mission Boardに見えるか。
- ユウが「書く・確認する・観察する」行動をしているか。
- 手、ペン、探偵ノート、ミッションカードが自然につながっているか。
- 虫眼鏡が浮いたり増殖したりしていないか。
- 今日のゴールを書く余白が十分あるか。
- Discovery Stampが報酬ではなく発見記録に見えるか。
- 起業押し付け、お金煽り、勝敗、採点、ランキングがないか。
- 既存IPや特定作品に似ていないか。
- 文字崩れがあっても後載せで隠せる範囲か。

## 4. NGなら使う修正プロンプトテンプレート

```text
Revise the Day1 Page 1 Mission Board image while keeping the same warm discovery-game educational style.

Keep:
- Yuu as an original grade 8 Value Detective
- Mission Board, Mission Card, Detective Note, Quest Map, and Discovery Stamp slot
- 16:9 Zoom-friendly layout

Fix:
- [insert specific issue]

Clarify:
- Yuu's hand should clearly write in the detective notebook or hold the mission card
- props must connect naturally to hands, table, notebook, or board
- leave large clean blank areas for Japanese overlay text
- Discovery Stamp is a learning record, not a prize

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
assets/generated/day1/page_01/candidates/day1_page_01_candidate_YYYYMMDD_01.png
```

代替保存先:

```text
outputs/day1/image_generation/candidates/day1_page_01_candidate_YYYYMMDD_01.png
```

## 6. Codexへ戻すときの報告テンプレート

`outputs/day1/image_generation/user_handoff_template.md` を使ってください。

最小報告:

```text
page_id: day1_page_01
prompt_packet: outputs/day1/image_generation/prompt_packets/day1_page_01_prompt_packet_for_gpt.md
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
