# Parent 05 Question Card Prompt For GPT

## 使う目的

親がその場で使うQuestion Cardの雰囲気を作るcandidate画像を作る。

## GPT画像生成に貼り付ける最終プロンプト

```text
Create a 16:9 warm, calm parent-facing educational visual showing a set of Question Cards for a Japanese family workshop.

The cards help parents ask short questions instead of giving correct answers.

Show:
- several blank Question Cards on a table
- a parent's hand gently offering one card
- a child's worksheet nearby, not being graded
- calm supportive layout with room for exact Japanese overlay

Do not write long Japanese text on the cards. Use blank surfaces or very short placeholder labels only.

Tone:
Practical, gentle, parent-friendly, not childish, not corporate-cold, less game-like than child-facing materials.

Parent role:
Parent is a facilitator and listener, not teacher, judge, examiner, or game master.

Safety:
No scoring, ranking, trophy, reward, competition, money hype, startup pressure, or future anxiety.

Originality:
Use original visual design. Do not imitate existing anime, manga, game, mascot, brand, logo, artist, studio, or franchise.

Negative prompt:
game loot cards, reward cards, trophy, score, ranking, grading sheet, strict teacher, judge panel, parent scolding, money pile, startup pressure, broken Japanese, tiny unreadable text, IP resemblance.
```

## 生成後チェック

- Question Cardが問いを出す道具に見えるか。
- 報酬カードやゲームアイテムに見えないか。
- 親が先生や採点者に見えないか。
- 正確な問いを後載せできる余白があるか。
- 起業押し付け、お金煽り、競争がないか。

## 修正プロンプトテンプレート

```text
Revise the parent Question Card visual.

Keep: blank question cards, parent gently offering one card, child worksheet nearby, calm parent-friendly tone.
Fix: [specific issue]
Remove: game loot feel, reward card feel, score, ranking, trophy, strict teacher, judge mood, money hype, broken Japanese, IP resemblance.
Text: leave card surfaces blank for exact Japanese overlay.
```

## 候補保存先

```text
assets/generated/parents/page_05/candidates/parent_page_05_candidate_YYYYMMDD_01.png
```

代替:

```text
outputs/parents/image_generation/candidates/parent_page_05_candidate_YYYYMMDD_01.png
```

## Codexへ戻すテンプレート

```text
page_id: parent_page_05_question_card
prompt_packet_used: outputs/parents/image_generation/prompt_packets/parent_05_question_card_prompt_for_gpt.md
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
