# Parent 09 After Session Reflection Prompt For GPT

## 使う目的

実施後に親子で短く振り返り、次の小さな改善につなげるcandidate画像を作る。

## GPT画像生成に貼り付ける最終プロンプト

```text
Create a 16:9 warm, calm parent-facing reflection support visual for a Japanese family workshop.

Theme: after-session reflection.

Show:
- parent and child sitting side by side
- a Reflection Support Sheet with blank areas
- a small Observation Log
- a Question Card nearby
- calm mood of looking back and choosing one next small step

The parent listens and asks, not grades. The child writes or points to their own reflection.

Text handling:
Do not generate long Japanese text. Exact reflection questions, labels, and checklist will be added later. Leave clean overlay areas.

Safety:
No grading, no score, no correct/incorrect mark, no ranking, no trophy, no prize, no money hype, no startup pressure, no comparison with siblings or other children.

Originality:
Use fully original people and visuals. Do not imitate existing anime, manga, game, mascot, brand, logo, artist, studio, or franchise.

Negative prompt:
grading sheet, red correction marks, test score, judge panel, parent scolding, trophy, ranking, prize, money pile, pressure, sad failure mood, broken Japanese, IP resemblance.
```

## 生成後チェック

- 実施後の振り返りに見えるか。
- 親が聞く、支える、問いを出す役割に見えるか。
- 採点、合否、失敗責めに見えないか。
- 次の小さな一歩へつながる雰囲気があるか。
- 後載せ文字の余白があるか。

## 修正プロンプトテンプレート

```text
Revise the after-session reflection visual.

Keep: parent and child side by side, Reflection Support Sheet, Observation Log, Question Card, calm reflection mood.
Fix: [specific issue]
Remove: grading, red correction marks, score, ranking, trophy, parent scolding, failure mood, money hype, broken Japanese, IP resemblance.
Text: leave clean blank areas for exact Japanese overlay.
```

## 候補保存先

```text
assets/generated/parents/page_09/candidates/parent_page_09_candidate_YYYYMMDD_01.png
```

代替:

```text
outputs/parents/image_generation/candidates/parent_page_09_candidate_YYYYMMDD_01.png
```

## Codexへ戻すテンプレート

```text
page_id: parent_page_09_after_session_reflection
prompt_packet_used: outputs/parents/image_generation/prompt_packets/parent_09_after_session_reflection_prompt_for_gpt.md
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
