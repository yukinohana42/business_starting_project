# Parent 04 OK NG Response Sheet Prompt For GPT

## 使う目的

親向けのOK/NG声かけ表を後載せしやすい、落ち着いた2列シートのcandidate画像を作る。

## GPT画像生成に貼り付ける最終プロンプト

```text
Create a 16:9 warm, calm parent-facing OK/NG Response Sheet visual for a Japanese family workshop.

Design a practical two-column sheet with blank areas:
Left column: NG voice examples area.
Right column: OK facilitator questions area.

Do not write the actual Japanese phrases. Leave clean blank spaces for exact Japanese overlay later.

Visual tone:
Parent-friendly, gentle, trustworthy, not childish, not corporate-cold. Less game-like than child-facing materials.

Show small supportive icons or cards:
- Question Card
- listening mark
- observation note
- safety boundary mark

Parent role:
Parent asks questions and supports observation, not teaches correct answers or evaluates.

Safety:
No scoring, grading, ranking, trophy, winner, prize, comparison between children, startup pressure, money hype, or fear warning.

Originality:
No existing anime, manga, game, mascot, brand, logo, artist, studio, or franchise resemblance.

Negative prompt:
grading sheet, red correction marks, score board, ranking, trophy, reward, strict teacher, judge panel, game UI loot, money pile, business pressure, broken Japanese, tiny generated Japanese text, IP resemblance.
```

## 生成後チェック

- OK/NG Response Sheetに見えるか。
- 正確な日本語を後載せできる余白があるか。
- 親が評価者に見える要素がないか。
- 採点表、点数表、ランキング表に見えないか。
- 子供向けゲームUIが強すぎないか。

## 修正プロンプトテンプレート

```text
Revise the OK/NG Response Sheet visual.

Keep: two-column practical sheet, blank areas for Japanese overlay, calm parent-friendly tone, Question Card and observation note.
Fix: [specific issue]
Remove: grading, red score marks, ranking, trophy, reward, judge mood, game loot, money hype, broken Japanese, IP resemblance.
Text: keep generated text minimal and blank.
```

## 候補保存先

```text
assets/generated/parents/page_04/candidates/parent_page_04_candidate_YYYYMMDD_01.png
```

代替:

```text
outputs/parents/image_generation/candidates/parent_page_04_candidate_YYYYMMDD_01.png
```

## Codexへ戻すテンプレート

```text
page_id: parent_page_04_ok_ng_response_sheet
prompt_packet_used: outputs/parents/image_generation/prompt_packets/parent_04_ok_ng_response_sheet_prompt_for_gpt.md
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
