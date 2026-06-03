# Parent 01 Cover Facilitator Guide Prompt For GPT

## 使う目的

親説明用資料の表紙または導入ページ用に、親が伴走者として関わる雰囲気のcandidate画像を作る。

## GPT画像生成に貼り付ける最終プロンプト

```text
Create a 16:9 warm, calm, parent-friendly educational visual for a Japanese family workshop.

This is a Parent Facilitator Guide cover, not a child-facing game screen and not a corporate seminar poster.

Show a parent sitting beside a junior high school student at the same table. The parent gently offers or points to a Question Card while listening. The child has a worksheet or note open. The relationship feels supportive and safe.

The parent is a facilitator, not a teacher, judge, scorer, examiner, or game master.

Use warm cream paper tones, calm gray-blue structure, muted coral question accents, soft green support accents, and pale blue organization lines. Keep large clean areas for exact Japanese title and subtitle overlay.

Text handling:
Do not generate long Japanese text. Exact Japanese body text will be added later.

Safety:
No startup pressure, no money hype, no anxiety about the future, no ranking, no scores, no trophies, no prizes, no grading, no comparison between children.

Originality:
Use fully original people and avoid resemblance to existing anime, manga, game, mascot, brand, artist, studio, or franchise.

Negative prompt:
teacher at blackboard, parent pointing down at child, judge panel, scoring sheet, game master pose, trophy, score, ranking, prize, money pile, fear warning, corporate stock art, broken Japanese, existing character resemblance.
```

## 生成後チェック

- 親が横で支える伴走者に見えるか。
- 親が先生、採点者、ゲームマスターに見えないか。
- 子供が評価される側として萎縮していないか。
- 親向けらしい落ち着きがあるか。
- 後載せ文字の余白があるか。
- 起業押し付け、お金煽り、競争、将来不安がないか。

## 修正プロンプトテンプレート

```text
Revise the parent cover visual while keeping the warm calm facilitator-guide tone.

Keep: parent beside child, Question Card, shared table, supportive listening mood, 16:9 layout.
Fix: [specific issue]
Remove: teacher, judge, scorer, game master, pressure, money hype, ranking, trophy, broken Japanese, IP resemblance.
Text: leave clean blank areas for exact Japanese overlay.
```

## 候補保存先

```text
assets/generated/parents/page_01/candidates/parent_page_01_candidate_YYYYMMDD_01.png
```

代替:

```text
outputs/parents/image_generation/candidates/parent_page_01_candidate_YYYYMMDD_01.png
```

## Codexへ戻すテンプレート

```text
page_id: parent_page_01_cover
prompt_packet_used: outputs/parents/image_generation/prompt_packets/parent_01_cover_facilitator_guide_prompt_for_gpt.md
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
