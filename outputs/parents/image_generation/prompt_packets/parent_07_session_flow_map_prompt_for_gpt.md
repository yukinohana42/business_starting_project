# Parent 07 Session Flow Map Prompt For GPT

## 使う目的

親がDay1からDay5の全体像を理解するためのSession Flow Map candidate画像を作る。

## GPT画像生成に貼り付ける最終プロンプト

```text
Create a 16:9 warm, calm parent-facing Session Flow Map for a Japanese family workshop.

Show a gentle five-step flow from Day1 to Day5:
1. value and work
2. finding everyday troubles
3. making ideas visible
4. small safe experiments
5. sharing value and reflection

Use calm map cards or connected panels. It should be less game-like than child-facing materials and not look like a race, ranking, or level-up path.

Keep card surfaces clean for exact Japanese overlay. Do not generate long Japanese text.

Parent role:
Parent follows the flow as a facilitator and asks questions. Parent is not teacher, judge, scorer, or game master.

Safety:
No competition, no score, no trophy, no ranking, no prize, no money hype, no startup pressure, no future anxiety.

Originality:
Use fully original diagrams and people. Do not imitate existing anime, manga, game, mascot, brand, logo, artist, studio, or franchise.

Negative prompt:
race track, leaderboard, level-up path, trophy, score, ranking, prize, game stage clear screen, money pile, startup pressure, strict teacher, judge panel, broken Japanese, crowded tiny text, IP resemblance.
```

## 生成後チェック

- Day1からDay5の流れが見えるか。
- レース、ランキング、レベルアップに見えないか。
- 親向けとして落ち着いているか。
- 本文を後載せできる余白があるか。
- 親が採点者やゲームマスターに見えないか。

## 修正プロンプトテンプレート

```text
Revise the Session Flow Map visual.

Keep: five-step Day1-Day5 map, calm connected panels, parent-friendly tone, blank text areas.
Fix: [specific issue]
Remove: race, leaderboard, level-up, trophy, score, ranking, game clear mood, money hype, strict teacher, judge mood, broken Japanese, IP resemblance.
Text: leave clean blank areas for exact Japanese overlay.
```

## 候補保存先

```text
assets/generated/parents/page_07/candidates/parent_page_07_candidate_YYYYMMDD_01.png
```

代替:

```text
outputs/parents/image_generation/candidates/parent_page_07_candidate_YYYYMMDD_01.png
```

## Codexへ戻すテンプレート

```text
page_id: parent_page_07_session_flow_map
prompt_packet_used: outputs/parents/image_generation/prompt_packets/parent_07_session_flow_map_prompt_for_gpt.md
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
