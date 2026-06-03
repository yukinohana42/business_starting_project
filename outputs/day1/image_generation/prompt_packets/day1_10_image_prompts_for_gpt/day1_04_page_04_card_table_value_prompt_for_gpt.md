# Day1 04 Page 04 Card Table Value Prompt For GPT

## 使う目的

Day1 Page4「価値は、相手の変化で見る」を、YuuとSoraがカードを使って考えるcandidate画像として作る。

## GPT画像生成に貼り付ける最終プロンプト

```text
Create a 16:9 horizontal warm hand-drawn educational illustration for a Japanese junior high school grade 8 workshop.

This is a discovery-game learning screen, not a generic explanation slide.

Use fully original characters only. Do not imitate existing anime, manga, game, mascot, brand, logo, artist, studio, or franchise.

Page type: Card Table - Value.

Scene:
Yuu and Sora work together at a table. Several Value Change Cards are on the table. Each card has a Before space and an After space. Yuu points at one card. Sora writes or moves a sticky note on another card.

Show visual card ideas:
- troubled -> helped
- confused -> able to try
- bored -> fun

Show:
- Card Table
- Value Change Cards
- sticky notes
- pens
- detective notebook
- Discovery Stamp slot as a learning record
- Quest Map with the value-card step emphasized
- clean blank headline area for later Japanese overlay: "価値は、相手の変化で見る"

Character action:
Yuu compares Before and After. Sora arranges or writes cards. Hands, cards, sticky notes, pens, and notebook must connect naturally.

Important:
Do not make this just three static cards. It must look like students are actively working.

Text handling:
Do not generate long Japanese text. Important Japanese body text and labels will be added later. Leave clean overlay areas.

Safety:
Before states are respectful. After states are small positive changes, not victory poses. No money hype, ranking, score, trophy, competition, or reward.

Negative prompt:
existing anime, manga, game, mascot, brand, logo, specific artist style, studio style, static three-card slide with no hands, face-only Yuu or Sora, characters standing without action, floating cards, floating sticky notes, duplicated pens, props emerging from face or body, broken hands, impossible fingers, generated Japanese paragraphs, Before person mocked, After victory celebration, score, rank, trophy, reward, money hype.
```

## 生成後チェック

- Card Tableに見えるか。
- YuuとSoraがカードを比べる、書く、並べる行動をしているか。
- ただの3枚カード説明になっていないか。
- 3つの変化が視覚的に読めるか。
- 手、付箋、カード、ペン、ノートが自然につながっているか。
- 日本語を後載せできる余白があるか。
- 報酬、勝敗、採点、ランキング、お金煽りがないか。
- 既存作品や特定絵柄に似ていないか。

## 修正プロンプトテンプレート

```text
Revise the Day1 Page4 Card Table image while keeping the warm discovery-game educational style.

Keep: Yuu and Sora working at a card table, Value Change Cards, sticky notes, pens, notebook, Discovery Stamp slot, 16:9 layout.
Fix: [specific issue]
Clarify: Yuu points to or compares a card. Sora writes or places a sticky note. Cards are learning tools, not decorative cards.
Remove: static slide feel, floating props, duplicate props, broken Japanese, money hype, score, ranking, trophy, reward-like elements, IP resemblance.
Text: leave clean blank areas for exact Japanese overlay.
```

## 候補保存先

```text
assets/generated/day1/page_04/candidates/day1_page_04_candidate_YYYYMMDD_01.png
```

代替:

```text
outputs/day1/image_generation/candidates/day1_page_04_candidate_YYYYMMDD_01.png
```

## Codexへ戻すテンプレート

```text
page_id: day1_page_04
prompt_packet_used: outputs/day1/image_generation/prompt_packets/day1_10_image_prompts_for_gpt/day1_04_page_04_card_table_value_prompt_for_gpt.md
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
