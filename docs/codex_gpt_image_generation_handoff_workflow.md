# Codex / GPT Image Generation Handoff Workflow

## Purpose

このリポジトリの画像生成運用では、Codexが画像生成そのものを実行することを標準にしません。

標準運用は manual handoff mode です。Codexはプロンプト、制作計画、レビュー基準、ファイル管理、candidate/final管理、後載せ文字設計、修正プロンプト作成を担当します。ユーザーがChatGPT / GPT画像生成へprompt packetを貼り、生成した画像をrepoへ戻します。

この運用はDay1だけでなく、Day2からDay5、親説明用資料、親チェックリスト、子供向けカード、ワークシート、4:5スマホ共有版、A4印刷物にも適用します。

## Roles

| Role | Does | Does Not Do |
| --- | --- | --- |
| Codex | prompt packet作成、計画、レビュー、修正prompt、保存先指定、candidate/final管理、後載せ文字設計 | 勝手に画像生成を実行しない。画像を見ていないのに見たふりをしない |
| GPT画像生成 | ユーザーが貼ったpromptからcandidate画像を作る | final判定、教材安全性判断、後載せ日本語の正確な組版 |
| ユーザー | prompt packetを貼る、画像をrepoに置く、第一印象と判断を返す、人間承認を行う | 画像をfinal扱いで保存しない。レビューなしに採用しない |

## Standard Flow

1. Codexが学習目的、画面タイプ、キャラクター行動、ゲーム要素、学習行動を整理する。
2. Codexがprompt packetを作る。
3. ユーザーがprompt packet内の「画像生成に貼る最終プロンプト」をChatGPT / GPT画像生成へ貼る。
4. ユーザーが1ページずつcandidate画像を生成する。
5. ユーザーが画像をrepoのcandidate保存先へ置く。
6. ユーザーがhandoff templateで第一印象、良い点、気になる点をCodexへ返す。
7. Codexが画像を確認できる場合はvisual reviewを作る。確認できない場合は `human visual review required` と明記する。
8. 問題があればCodexが修正promptを作る。
9. 人間承認後にだけfinal候補へ進める。
10. final画像が揃ってから、contact sheet、後載せ文字、4:5、A4、台本・カード・ワークシート反映へ進む。

## Prompt Packet Requirements

各prompt packetには必ず次を入れます。

- 使用目的。
- GPT画像生成に貼る最終プロンプト。
- 生成後チェックリスト。
- NG時の修正プロンプトテンプレート。
- candidate画像の保存先。
- Codexへ戻す報告テンプレート。
- final化しないルール。
- 文字は後載せ前提であること。

## File Management

推奨保存先:

```text
outputs/<session>/image_generation/prompt_packets/
outputs/<session>/image_generation/candidates/
outputs/<session>/image_generation/reviews/
assets/generated/<session>/page_<nn>/candidates/
assets/generated/<session>/page_<nn>/final/
assets/generated/<session>/page_<nn>/rejected/
```

初回生成物は必ず `candidate` です。レビューなしに `final` へ移動しません。

保存時には、できる限り次を記録します。

- page id
- prompt packet path
- aspect ratio
- generation date
- candidate filename
- selected / rejected / pending
- human memo
- Codex review memo
- next action

## Review Rules

画像レビューでは次を確認します。

- キャラクターが学習行動をしているか。
- 手、小物、視線、姿勢が意味を持っているか。
- game elementが飾りではなく、見る、選ぶ、話す、書く、比べる、試す行動につながっているか。
- 価値が相手のBefore/Afterとして見えるか。
- 壊れた日本語や小さすぎる文字をfinal本文として使っていないか。
- 起業を押し付けていないか。
- お金を煽っていないか。
- 勝敗、採点、ランキング、報酬化がないか。
- 既存IPや特定作家の模倣に見えないか。

## API Automation Boundary

将来OpenAI画像生成APIを使う場合でも、このmanual handoff workflowを置き換えるのではなく補助します。

API自動化を始める前に、公式ドキュメント確認、secret管理、manifest設計、dry-run、1ページpilot、人間レビューを必須にします。APIがないことは、プロンプト整備、手動生成、レビュー、教材設計を止める理由にはなりません。

## Parent-Facing Materials

親向け資料でも同じcandidate / review / revise / final運用を使います。ただし、子供向けの発見ゲームUIをそのまま強く出しません。

親向けは次の形を優先します。

- Parent Facilitator Guide
- Question Card
- OK/NG Response Sheet
- Safety Boundary Card
- Session Flow Map
- Praise Guide

親は先生、採点者、ゲームマスターではありません。問いを出す伴走者として描きます。
