# Parent 02 Why This Workshop Prompt For GPT

## 使う目的

親が「このワークショップは起業を押し付けるものではなく、価値を見る練習」と理解するための図解candidateを作る。

## GPT画像生成に貼り付ける最終プロンプト

```text
Create a 16:9 warm, calm, parent-friendly educational diagram for a Japanese family workshop.

Theme: Why this workshop exists.

Show a gentle visual flow:
observe everyday trouble -> ask a short question -> try a small safe action -> notice a small positive change.

Use parent-friendly diagrams, guide cards, and simple arrows. Keep it less game-like than child-facing materials. It should feel practical, trustworthy, and clear.

Do not show entrepreneurship as an obligation. Do not show money as the main goal. The focus is "finding value for a concrete person" and "small safe practice."

Text handling:
Do not generate long Japanese text. Exact Japanese title, body text, and labels will be added later. Leave clean overlay areas and blank card surfaces.

Safety:
No pressure, no fear, no competition, no ranking, no scores, no trophies, no money hype.

Originality:
Use original simple people and diagrams only. Avoid any resemblance to existing anime, manga, game, mascot, brand, artist, studio, or franchise.

Negative prompt:
startup pressure poster, money pile, scary future warning, corporate seminar slide, trophy, ranking, score, winner, child comparison, teacher lecture, broken Japanese, crowded text, IP resemblance.
```

## 生成後チェック

- 起業押し付けではなく、価値を見る練習に見えるか。
- 観察、問い、小さく試す、変化を見る流れがあるか。
- 親向けとして落ち着いているか。
- 文字を後載せできる余白があるか。
- お金煽り、競争、将来不安がないか。

## 修正プロンプトテンプレート

```text
Revise the parent "why this workshop" visual.

Keep: observe -> question -> small try -> small positive change flow, calm parent-friendly diagram, 16:9 layout.
Fix: [specific issue]
Remove: startup pressure, money hype, fear warning, ranking, score, trophy, corporate coldness, broken Japanese, IP resemblance.
Text: leave clean blank areas for exact Japanese overlay.
```

## 候補保存先

```text
assets/generated/parents/page_02/candidates/parent_page_02_candidate_YYYYMMDD_01.png
```

代替:

```text
outputs/parents/image_generation/candidates/parent_page_02_candidate_YYYYMMDD_01.png
```

## Codexへ戻すテンプレート

```text
page_id: parent_page_02_why_this_workshop
prompt_packet_used: outputs/parents/image_generation/prompt_packets/parent_02_why_this_workshop_prompt_for_gpt.md
candidate_filename:
candidate_path:
human_candidate_decision: keep / revise / reject / unsure
first_impression:
good_points:
concerns:
text_issues:
parent_role_issues:
safety_check:
next_action_requested_for_codex:
```

## 最終化しないルール

最初の生成画像はcandidateです。視覚レビューと人間承認が終わるまでfinalにしません。

## 日本語テキストの扱い

日本語の見出し、本文、ラベルは画像生成で完成させない。画像には、後から正しい日本語を重ねるための余白と読みやすい配置だけを作る。生成画像に崩れた日本語や不要な英字が出た場合は、候補レビューで修正対象にする。

## 権利とスタイルの禁止事項

既存の漫画、アニメ、ゲーム、ブランド、ロゴ、マスコット、特定作家、特定スタジオのキャラクターや絵柄をまねない。人物、衣装、小物、UIはすべて完全オリジナルとして扱う。
