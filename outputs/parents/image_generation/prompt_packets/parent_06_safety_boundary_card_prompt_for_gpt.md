# Parent 06 Safety Boundary Card Prompt For GPT

## 使う目的

親が家庭内ワークショップの安全な範囲を確認するSafety Boundary Cardのcandidate画像を作る。

## GPT画像生成に貼り付ける最終プロンプト

```text
Create a 16:9 warm, calm parent-facing Safety Boundary Card visual for a Japanese family workshop.

The visual should help parents keep the workshop safe and gentle.

Show:
- a large blank Safety Boundary Card
- small calm icons for home, conversation, safe question, small try, and stop-if-uncomfortable
- parent and child beside each other, not facing each other like an interview test
- clean areas for exact Japanese overlay

Do not write long Japanese text. Exact safety rules will be added later.

Tone:
Parent-friendly, gentle, trustworthy, not childish, not corporate-cold, less game-like than child-facing materials.

Parent role:
Parent protects safety and asks questions. Parent does not push sales, judge ideas, compare children, or force interviews.

Safety:
No pressure, no fear, no money hype, no competition, no grading, no score, no trophy, no ranking.

Originality:
Use original visuals only. Do not imitate existing anime, manga, game, mascot, brand, logo, artist, studio, or franchise.

Negative prompt:
warning poster, scary danger signs, sales pressure, forced interview, judge panel, teacher lecture, score board, ranking, trophy, money pile, corporate coldness, broken Japanese, IP resemblance.
```

## 生成後チェック

- Safety Boundary Cardとして見えるか。
- 親が安全を守る伴走者に見えるか。
- 脅しや不安訴求に見えないか。
- 無理な販売、比較、採点に見えないか。
- 後載せ文字の余白があるか。

## 修正プロンプトテンプレート

```text
Revise the Safety Boundary Card visual.

Keep: large blank safety card, calm home workshop mood, parent beside child, safe-question and small-try icons.
Fix: [specific issue]
Remove: scary warning, sales pressure, forced interview, judge mood, scoring, ranking, money hype, broken Japanese, IP resemblance.
Text: leave clean blank areas for exact Japanese overlay.
```

## 候補保存先

```text
assets/generated/parents/page_06/candidates/parent_page_06_candidate_YYYYMMDD_01.png
```

代替:

```text
outputs/parents/image_generation/candidates/parent_page_06_candidate_YYYYMMDD_01.png
```

## Codexへ戻すテンプレート

```text
page_id: parent_page_06_safety_boundary
prompt_packet_used: outputs/parents/image_generation/prompt_packets/parent_06_safety_boundary_card_prompt_for_gpt.md
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
