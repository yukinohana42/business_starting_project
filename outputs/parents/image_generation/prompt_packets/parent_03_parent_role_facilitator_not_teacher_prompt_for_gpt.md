# Parent 03 Parent Role Facilitator Not Teacher Prompt For GPT

## 使う目的

親の役割が「先生・採点者」ではなく「問いを出す伴走者」だと伝えるcandidate画像を作る。

## GPT画像生成に貼り付ける最終プロンプト

```text
Create a 16:9 warm, calm, parent-friendly educational visual for a Japanese family workshop.

Theme: Parent role. Facilitator, not teacher.

Show a side-by-side visual contrast without harsh judgment:
Left: parent almost becoming teacher or judge, shown only as a muted caution silhouette, not scary.
Right: parent sitting beside the child, offering a Question Card and listening.

The right side should be the clear positive model. Parent supports observation, questions, trying, and improvement.

Design:
Less game-like than child-facing materials. Warm cream background, calm gray-blue structure, muted coral for question accent, soft green for support.

Text handling:
Do not generate long Japanese text. Exact OK/NG labels and explanation will be added later. Leave clean overlay areas.

Safety:
No grading, no score, no red correction marks, no comparison with siblings or other children, no money hype, no startup pressure.

Originality:
Use fully original people and avoid resemblance to existing anime, manga, game, mascot, brand, artist, studio, or franchise.

Negative prompt:
strict teacher, judge panel, exam grading, red score marks, parent scolding child, game master, trophy, ranking, score, money pile, future anxiety, broken Japanese, IP resemblance.
```

## 生成後チェック

- 親が伴走者として見えるか。
- 親が先生、採点者、ゲームマスターに見えないか。
- 子供が萎縮していないか。
- OK/NGの後載せ余白があるか。
- 起業押し付け、お金煽り、採点感がないか。

## 修正プロンプトテンプレート

```text
Revise the parent role visual.

Keep: facilitator-not-teacher message, parent beside child, Question Card, listening mood, 16:9 layout.
Fix: [specific issue]
Remove: strict teacher, judge, scorer, game master, grading marks, pressure, money hype, broken Japanese, IP resemblance.
Text: leave clean blank areas for exact Japanese overlay.
```

## 候補保存先

```text
assets/generated/parents/page_03/candidates/parent_page_03_candidate_YYYYMMDD_01.png
```

代替:

```text
outputs/parents/image_generation/candidates/parent_page_03_candidate_YYYYMMDD_01.png
```

## Codexへ戻すテンプレート

```text
page_id: parent_page_03_parent_role
prompt_packet_used: outputs/parents/image_generation/prompt_packets/parent_03_parent_role_facilitator_not_teacher_prompt_for_gpt.md
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
