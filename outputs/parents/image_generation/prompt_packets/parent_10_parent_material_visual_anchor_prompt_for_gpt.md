# Parent 10 Parent Material Visual Anchor Prompt For GPT

## 使う目的

親説明用資料全体の共通トーンを確認するanchor candidateを作る。各親向けpromptの前提として使える。

## GPT画像生成に貼り付ける最終プロンプト

```text
Create a 16:9 parent-facing visual anchor for a Japanese family workshop.

Overall purpose:
The parent understands the workshop and supports the child as a facilitator. The parent is not a teacher, judge, scorer, examiner, or game master.

Tone:
warm, calm, gentle, trustworthy, parent-friendly, not childish, not corporate-cold, less game-like than child-facing materials.

Visual system:
warm cream background, calm gray-blue structure, muted coral question accents, soft green support accents, pale blue organization lines, clean paper/card surfaces, readable large empty areas for later Japanese overlay.

Allowed elements:
Facilitator Guide, Question Card, OK/NG Response Sheet, Safety Boundary Card, Session Flow Map, Observation Log, Reflection Support Sheet, Praise Guide.

People:
Original parent and child sitting side by side or working at the same table. Parent listens, offers a question, or points gently to a safety boundary. Child remains respected and not evaluated.

Text handling:
Do not generate long Japanese text. Exact Japanese body text, OK/NG examples, tables, checklists, and page numbers will be added later.

Safety:
No startup pressure, no money hype, no anxiety about the future, no competition, no ranking, no score, no trophy, no prize, no grading, no comparison between children.

Originality:
Use fully original people and visual elements. Do not imitate existing anime, manga, game, mascot, brand, logo, artist, studio, or franchise.

Negative prompt:
teacher lecture, judge panel, parent as examiner, game master, scoring sheet, red grading marks, leaderboard, trophy, prize, reward chest, money pile, scary future warning, corporate stock art, childish game UI, broken Japanese, tiny text, IP resemblance.
```

## 生成後チェック

- 親向けの落ち着いた共通トーンになっているか。
- 親がファシリテーターとして見えるか。
- 先生、採点者、ゲームマスターに見えないか。
- 子供向けゲームUIが強すぎないか。
- 後載せ文字の余白があるか。
- 起業押し付け、お金煽り、競争、採点がないか。

## 修正プロンプトテンプレート

```text
Revise the parent visual anchor while keeping it warm, calm, and facilitator-focused.

Keep: parent beside child, Question Card or Safety Boundary Card, calm guide-paper style, clean blank overlay areas, 16:9 layout.
Fix: [specific issue]
Remove: teacher, judge, scorer, game master, childish game UI, corporate coldness, ranking, trophy, money hype, fear warning, broken Japanese, IP resemblance.
Text: leave clean blank areas for exact Japanese overlay.
```

## 候補保存先

```text
assets/generated/parents/anchor/candidates/parent_visual_anchor_candidate_YYYYMMDD_01.png
```

代替:

```text
outputs/parents/image_generation/candidates/parent_visual_anchor_candidate_YYYYMMDD_01.png
```

## Codexへ戻すテンプレート

```text
page_id: parent_visual_anchor
prompt_packet_used: outputs/parents/image_generation/prompt_packets/parent_10_parent_material_visual_anchor_prompt_for_gpt.md
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
