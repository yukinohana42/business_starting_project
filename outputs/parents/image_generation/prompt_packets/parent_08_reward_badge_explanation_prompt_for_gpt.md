# Parent 08 Reward Badge Explanation Prompt For GPT

## 使う目的

ゲーミフィケーションは報酬ではなく学びの足場だと親に伝えるcandidate画像を作る。

## GPT画像生成に貼り付ける最終プロンプト

```text
Create a 16:9 warm, calm parent-facing educational visual explaining that badges and stamps are learning records, not rewards.

Show:
- Discovery Stamp as a small learning record
- Reflection Stamp as a reflection record
- a notebook or observation log
- a parent and child looking at what was noticed, not celebrating a prize

Design:
Less game-like than child-facing materials. Calm, practical, parent-friendly. No glittery reward look.

Text handling:
Do not generate long Japanese text. Exact explanation and labels will be added later. Leave clean overlay areas.

Learning message:
Stamps and badges record observation, questions, trying, and improvement. They do not rank ability and do not compare children.

Parent role:
Parent praises process, not results or money potential.

Safety:
No trophy, prize, winner, score, ranking, level-up reward, loot, money hype, startup pressure, or comparison.

Originality:
Use original visuals only. Do not imitate existing anime, manga, game, mascot, brand, logo, artist, studio, or franchise.

Negative prompt:
trophy, medal winner, prize, reward chest, loot box, level-up, scoreboard, ranking, money pile, confetti victory, judging parent, child comparison, broken Japanese, IP resemblance.
```

## 生成後チェック

- スタンプやバッジが学びの記録に見えるか。
- 報酬、勝利、レベルアップに見えないか。
- 親がプロセスを見ている構図か。
- 後載せ文字の余白があるか。
- お金煽り、競争、比較がないか。

## 修正プロンプトテンプレート

```text
Revise the reward/badge explanation visual.

Keep: Discovery Stamp and Reflection Stamp as learning records, notebook, parent and child reflecting calmly.
Fix: [specific issue]
Remove: trophy, prize, winner, level-up, loot, score, ranking, money hype, judging parent, broken Japanese, IP resemblance.
Text: leave clean blank areas for exact Japanese overlay.
```

## 候補保存先

```text
assets/generated/parents/page_08/candidates/parent_page_08_candidate_YYYYMMDD_01.png
```

代替:

```text
outputs/parents/image_generation/candidates/parent_page_08_candidate_YYYYMMDD_01.png
```

## Codexへ戻すテンプレート

```text
page_id: parent_page_08_reward_badge_explanation
prompt_packet_used: outputs/parents/image_generation/prompt_packets/parent_08_reward_badge_explanation_prompt_for_gpt.md
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
