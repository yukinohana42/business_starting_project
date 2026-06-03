# Day1 01 Page 01 Mission Board Prompt For GPT

## 使う目的

Day1 Page1「お金と仕事の正体を見破れ」を、GPT画像生成で1枚のcandidateとして作る。

## GPT画像生成に貼り付ける最終プロンプト

```text
Create a 16:9 horizontal warm hand-drawn educational illustration for a Japanese junior high school grade 8 workshop.

This is a discovery-game learning screen, not a generic explanation slide and not a business poster.

Use fully original characters only. Do not imitate any existing anime, manga, game, mascot, brand, logo, artist, studio, or franchise.

Page type: Mission Board.

Scene:
Yuu, an original same-age junior high school student and Value Detective, starts the mission. Yuu receives or holds a Mission Card and uses a detective notebook and pen. Yuu looks curious, thoughtful, and warm.

Show:
- Mission Board
- Mission Card
- Detective Note
- Quest Map
- Discovery Stamp slot as a learning record, not a reward
- Goal card area for later Japanese overlay: "仕事とは、＿＿を＿＿に変えること。"
- large clean headline area for later Japanese overlay: "お金と仕事の正体を見破れ"

Character action:
Yuu is writing in the detective notebook or checking the mission card. Show hands, pen, notebook, card, gaze, and posture. Yuu must not be a face-only icon and must not stand still without action.

Learning idea:
The learner should understand that today's mission is to discover work as "changing someone's state," not as money hype.

Text handling:
Do not generate long Japanese text. Important Japanese body text will be added later. Leave clean blank areas for headline, goal sentence, card labels, and page number.

Safety:
No startup pressure. No money piles. No luxury goods. No winner/loser. No ranking, score, trophy, prize, level-up, or reward-like elements.

Prop rules:
Use a magnifying glass only if Yuu clearly holds it or it rests naturally on a table. Avoid random, floating, duplicated, or body-emerging props.

Negative prompt:
existing anime, manga, game, mascot, brand, logo, specific artist style, studio style, face-only icon, static character, floating magnifying glass, duplicated props, broken hands, impossible fingers, broken Japanese text, crowded poster, cash pile, luxury lifestyle, trophy, score, ranking, reward bait, pressure to become an entrepreneur.
```

## 生成後チェック

- Mission Boardに見えるか。
- Yuuが書く、確認する、観察する行動をしているか。
- Mission Card、Detective Note、Quest Map、Discovery Stamp slotが学習行動につながっているか。
- 虫眼鏡や小物が浮いたり増殖したりしていないか。
- 日本語を後載せできる余白があるか。
- 起業押し付け、お金煽り、勝敗、採点、ランキング、報酬化がないか。
- 既存作品や特定絵柄に似ていないか。

## 修正プロンプトテンプレート

```text
Revise the Day1 Page1 Mission Board image while keeping the warm discovery-game educational style.

Keep: Yuu as an original grade 8 Value Detective, Mission Board, Mission Card, Detective Note, Quest Map, Discovery Stamp slot, 16:9 layout.
Fix: [specific issue]
Clarify: Yuu's hand writes in the notebook or holds the mission card. Props connect naturally to hands, table, notebook, or board.
Remove: floating or duplicated props, broken Japanese text, money hype, score, ranking, trophy, reward-like elements, IP resemblance.
Text: leave clean blank areas for exact Japanese overlay.
```

## 候補保存先

```text
assets/generated/day1/page_01/candidates/day1_page_01_candidate_YYYYMMDD_01.png
```

代替:

```text
outputs/day1/image_generation/candidates/day1_page_01_candidate_YYYYMMDD_01.png
```

## Codexへ戻すテンプレート

```text
page_id: day1_page_01
prompt_packet_used: outputs/day1/image_generation/prompt_packets/day1_10_image_prompts_for_gpt/day1_01_page_01_mission_board_prompt_for_gpt.md
candidate_filename:
candidate_path:
human_candidate_decision: keep / revise / reject / unsure
first_impression:
good_points:
concerns:
meaningless_depictions:
text_issues:
hand_prop_gaze_issues:
safety_check:
next_action_requested_for_codex:
```

## 最終化しないルール

最初の生成画像はcandidateです。視覚レビューと人間承認が終わるまでfinalにしません。

## 日本語テキストの扱い

日本語の見出し、本文、ラベルは画像生成で完成させない。画像には、後から正しい日本語を重ねるための余白と読みやすい配置だけを作る。生成画像に崩れた日本語や不要な英字が出た場合は、候補レビューで修正対象にする。

## 権利とスタイルの禁止事項

既存の漫画、アニメ、ゲーム、ブランド、ロゴ、マスコット、特定作家、特定スタジオのキャラクターや絵柄をまねない。人物、衣装、小物、UIはすべて完全オリジナルとして扱う。
