# Day1 10 Common UI Parts Prompt For GPT

## 使う目的

Day1本編、後続カード、ワークシート制作で使える共通UI素材のcandidateを作る。

## GPT画像生成に貼り付ける最終プロンプト

```text
Create a 16:9 horizontal clean reference sheet of common learning UI parts for a Japanese junior high school grade 8 workshop.

Style:
warm hand-drawn educational illustration, soft paper texture, warm cream, soft navy, muted coral, warm yellow, soft green, pale blue. Parent-safe, calm, organized, Zoom-friendly.

Use fully original UI parts only. Do not imitate existing games, anime, manga, mascots, brands, logos, artists, studios, or franchises.

Create these common UI parts:
- Mission Card
- Detective Note
- Evidence Card
- Value Change Card
- Discovery Stamp
- Quest Map
- Final Mission Sheet
- Question Card

Functional rule:
These are learning tools, not rewards or game loot. They help learners see, choose, write, talk, compare, and reflect.

Design rule:
Leave surfaces clean and mostly blank so exact Japanese text can be added later. Avoid long generated Japanese text. Short English placeholders like MISSION, NOTE, EVIDENCE, QUESTION are acceptable if subtle.

Safety:
No trophy, score, ranking, prize, level-up, reward chest, winner badge, cash, luxury, startup pressure, or competition mood.

Negative prompt:
existing game UI, loot box, trophy, score board, ranking board, prize, reward badge, level-up reward, cash, luxury, brand logo, copyrighted character, specific artist style, broken Japanese, tiny unreadable text, cluttered poster, floating meaningless icons.
```

## 生成後チェック

- UI partsが学習道具に見えるか。
- Mission Card、Detective Note、Evidence Card、Value Change Card、Discovery Stamp、Quest Map、Final Mission Sheet、Question Cardがそろっているか。
- 報酬、ゲーム内アイテム、トロフィー、スコアに見えないか。
- 後載せ日本語の余白があるか。
- 既存ゲームUIやブランドに似ていないか。

## 修正プロンプトテンプレート

```text
Revise the common UI parts sheet while keeping the warm educational paper style.

Keep: Mission Card, Detective Note, Evidence Card, Value Change Card, Discovery Stamp, Quest Map, Final Mission Sheet, Question Card.
Fix: [specific issue]
Clarify: all parts are learning tools, not rewards or game loot. Leave blank areas for exact Japanese overlay.
Remove: trophy, score, ranking, prize, reward chest, level-up, cash, brand resemblance, broken Japanese.
```

## 候補保存先

```text
assets/generated/day1/ui_parts/candidates/day1_common_ui_parts_candidate_YYYYMMDD_01.png
```

代替:

```text
outputs/day1/image_generation/candidates/day1_common_ui_parts_candidate_YYYYMMDD_01.png
```

## Codexへ戻すテンプレート

```text
page_id: day1_common_ui_parts
prompt_packet_used: outputs/day1/image_generation/prompt_packets/day1_10_image_prompts_for_gpt/day1_10_common_ui_parts_prompt_for_gpt.md
candidate_filename:
candidate_path:
human_candidate_decision: keep / revise / reject / unsure
first_impression:
good_points:
concerns:
meaningless_depictions:
text_issues:
hand_prop_gaze_issues:
safety_check:
next_action_requested_for_codex:
```

## 最終化しないルール

最初の生成画像はcandidateです。視覚レビューと人間承認が終わるまでfinalにしません。

## 日本語テキストの扱い

日本語の見出し、本文、ラベルは画像生成で完成させない。画像には、後から正しい日本語を重ねるための余白と読みやすい配置だけを作る。生成画像に崩れた日本語や不要な英字が出た場合は、候補レビューで修正対象にする。

## 権利とスタイルの禁止事項

既存の漫画、アニメ、ゲーム、ブランド、ロゴ、マスコット、特定作家、特定スタジオのキャラクターや絵柄をまねない。人物、衣装、小物、UIはすべて完全オリジナルとして扱う。
