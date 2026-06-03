# Day1 05 Page 05 Business Detective Case File Prompt For GPT

## 使う目的

Day1 Page5「この仕事は、誰をどう変えている？」を、3つの身近な仕事から観察するcandidate画像として作る。

## GPT画像生成に貼り付ける最終プロンプト

```text
Create a 16:9 horizontal warm hand-drawn educational illustration for a Japanese junior high school grade 8 workshop.

This is a discovery-game learning screen, not a generic example list, ranking board, or business poster.

Use fully original characters only. Do not imitate existing anime, manga, game, mascot, brand, logo, artist, studio, or franchise.

Page type: Business Detective Case File.

Scene:
A large Business Detective Case File board is open. Exactly three Evidence Cards are attached with pins, tape, or connecting lines. Yuu observes with a detective notebook. Sora pins, moves, or writes one evidence card.

Three cases:
1. Convenience store: rushed person -> can buy quickly and feels helped.
2. Tutoring / learning support: confused learner -> feels able to try.
3. Smartphone game: bored time -> fun time.

Smartphone game rule:
Show a safe everyday entertainment example only. Do not suggest addiction, gacha, gambling, payment pressure, monetization, or excessive screen use. Do not resemble an existing game.

Show:
- Case File board
- exactly three Evidence Cards
- Detective Note
- Discovery Stamp slot as a learning record
- Quest Map with the case step emphasized
- clean blank headline area for later Japanese overlay: "この仕事は、誰をどう変えている？"

Character action:
Yuu inspects the board. Sora actively pins, writes, or moves a card. Both characters support the investigation.

Text handling:
Do not generate long Japanese text. Exact Japanese labels and example text will be added later. Leave clean overlay areas.

Safety:
Do not rank the jobs. Do not imply one job is superior. No money hype, startup pressure, score, trophy, winner/loser, prize, or reward-like elements.

Negative prompt:
existing anime, manga, game, mascot, brand, logo, specific artist style, studio style, plain three-example slide, five or more example cards, YouTuber, ramen shop, job ranking, score, winner, trophy, money hype, profit celebration, smartphone addiction, gacha, gambling, payment pressure, existing game resemblance, face-only characters, standing without action, floating cards, duplicated props, broken hands, impossible fingers, long generated Japanese paragraphs.
```

## 生成後チェック

- Business Detective Case Fileに見えるか。
- Evidence Cardが3枚だけか。
- YouTuberやラーメン屋など余計な例が入っていないか。
- 3例がランキングや優劣に見えないか。
- 「誰が、どう変わるか」が見えるか。
- YuuとSoraが観察、貼る、書くなどの行動をしているか。
- スマホゲームが依存、課金、ガチャ、ギャンブル、既存ゲーム風に見えないか。
- 日本語を後載せできる余白があるか。
- お金煽り、勝敗、採点、報酬化がないか。
- 既存作品や特定絵柄に似ていないか。

## 修正プロンプトテンプレート

```text
Revise the Day1 Page5 Business Detective Case File image while keeping the warm discovery-game educational style.

Keep: large Case File board, exactly three Evidence Cards for convenience store, tutoring / learning support, smartphone game, Yuu observing, Sora pinning or writing, 16:9 layout.
Fix: [specific issue]
Clarify: each Evidence Card shows who changes and how. Smartphone game is safe everyday fun, not addiction or payment pressure. Cards are evidence, not ranking cards.
Remove: YouTuber, ramen shop, extra examples, money hype, ranking, score, trophy, reward, job superiority, floating props, broken Japanese, IP resemblance.
Text: leave clean blank areas for exact Japanese overlay.
```

## 候補保存先

```text
assets/generated/day1/page_05/candidates/day1_page_05_candidate_YYYYMMDD_01.png
```

代替:

```text
outputs/day1/image_generation/candidates/day1_page_05_candidate_YYYYMMDD_01.png
```

## Codexへ戻すテンプレート

```text
page_id: day1_page_05
prompt_packet_used: outputs/day1/image_generation/prompt_packets/day1_10_image_prompts_for_gpt/day1_05_page_05_business_detective_case_file_prompt_for_gpt.md
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
