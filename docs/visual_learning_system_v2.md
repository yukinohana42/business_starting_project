# Visual Learning System v2

## Basic Definition

この教材は、説明スライドではありません。発見ゲーム型の学習体験です。

ただし、ゲームは報酬や勝敗のためではありません。観察、問い、仮説、小さな実験、振り返りを進めるための足場です。

子供向け資料は、読むだけの資料ではなく、見る、選ぶ、並べる、書く、話す、試すための画面として設計します。

## Child-Facing Material Types

子供向け資料は、以下のどれかの画面として設計します。

- Mission Board
- Quest Map
- Detective Note
- Case File
- Evidence Board
- Card Table
- Experiment Lab
- Pitch Stage
- Final Mission Sheet
- Reflection Log

### Child-Facing Prohibitions

- 見出し、本文、カードを並べただけの普通の説明スライド。
- キャラクターを顔アイコンや名前ラベルとして置くだけ。
- ゲーム用語をタイトルに入れただけ。
- ミッションカード、探偵ノート、ケースファイル、スタンプが学習行動とつながっていない。
- バッジやスタンプを報酬のように扱う。
- 採点、ランキング、勝敗、儲かる順、早く終わった順。

## Parent-Facing Material Types

親向け資料は、子供向けほどゲームUIを強くしません。ただし、無機質な説明資料にもしてはいけません。

親向け資料は、以下のどれかの形で設計します。

- Facilitator Guide
- Parent Briefing
- Question Card
- OK/NG Response Sheet
- Observation Log
- Safety Boundary Card
- Reflection Support Sheet
- Praise Guide
- Session Flow Map

### Parent-Facing Rules

- 親は先生ではなくファシリテーター。
- 親は採点者ではない。
- 親はゲームマスターではない。
- 子供の答えを評価するのではなく、観察、問い、試したことを支える。
- 褒めるときは結果ではなく、観察、問い、試行、改善を褒める。
- 起業を押し付けない。
- 不安を煽らない。
- お金で煽らない。
- 子供を他人や兄弟と比べない。

## Character Rules

キャラクターは飾りではありません。思考の代理人として行動します。

### Required Character Actions

各ページで、キャラクターは次のどれかをしている必要があります。

- メモする
- 観察する
- 指差す
- カードを並べる
- 付箋を書く
- ラフスケッチする
- 質問する
- 試す
- 反応を見る
- 振り返る
- 発表する

### Character Prohibitions

- 丸アイコンだけ。
- 顔だけ。
- 名前ラベルだけ。
- 立っているだけ。
- 同じ人物絵を色違いで使うだけ。
- キャラクターが内容と関係ない場所に置かれているだけ。

HTML/CSSで作る場合も、丸い顔アイコンだけでは不合格です。少なくとも手元、姿勢、小物、視線、行動が見えるようにします。必要ならinline SVG、手描き風SVG、または完全オリジナルの画像生成素材を使います。

## Game Element Rules

ゲーム要素は装飾ではなく、学びの進行を見える化するUIです。

### Allowed Elements

- Mission Card
- Quest Map
- Case File
- Detective Note
- Evidence Card
- Value Change Card
- Problem Card
- Customer Card
- Idea Card
- Experiment Card
- PMF Signal Card
- Pitch Card
- Discovery Stamp
- Learning Badge
- Reflection Stamp
- Final Mission Sheet

### Game Element Prohibitions

- ゲーム要素をタイトルに入れるだけ。
- 実際に子供が考える行動とつながっていないスタンプ。
- ご褒美のようなバッジ。
- 勝者表示。
- スコア。
- ランキング。
- トロフィー。
- レベルアップ報酬。
- 儲かる順。

## Required Screen Check

すべての子供向けインフォグラフィック、スライド、カード、ワークシートで、最低限以下を確認します。

- キャラクターの行動があるか。
- 子供が何を考えればよいかが画面上でわかるか。
- ゲーム要素が学習行動と結びついているか。
- 価値や学びが相手の変化として見えるか。
- 1画面1メッセージになっているか。
- Zoomまたは印刷で読めるか。
- 勝敗、採点、報酬、金儲け煽りに見えないか。
- 既存作品や既存キャラクターの模倣になっていないか。

## Stop Rule Before Production

以下が未定義の場合、HTML/CSS、PNG、PDF、PPTX、印刷レイアウトの生成へ進みません。

- ページごとのキャラクター行動。
- ページごとのゲーム要素。
- 子供または親がその画面でする行動。
- Before/Afterまたは学びの変化。
- 合格基準表。

## Image-First Production Addendum

今後の子供向けビジュアル教材は、HTML/CSSだけで絵を完成させることを標準にしません。

標準は、画像生成または専用イラスト素材で「場面、キャラクター行動、手元、小物、相手の変化」を作り、その後でHTML/CSSやレイアウトツールを使って正確な日本語本文、空欄、カード文言、ページ番号、16:9/4:5/A4書き出しを補います。

制作前に必ず読む:

- `docs/image_first_visual_workflow_analysis.md`
- `docs/image_first_visual_production_workflow.md`
- `docs/global_visual_system_spec.md`

画像生成promptに入れる必須項目:

- page type
- character action
- game element function
- learner action
- visible change
- props and hand action
- text overlay area
- negative prompt

HTML/CSSは主役のビジュアル生成手段ではなく、文字載せ、構図補正、フォーマット展開、contact sheet作成の補助として扱います。

生成後には必ず `docs/image_generation_review_and_refinement_workflow.md` と `docs/image_generation_visual_review_checklist.md` に沿ってcandidateを確認します。最初の生成物はfinalではありません。小物の意味不明な位置、手や視線との不一致、文字崩れ、報酬や勝敗に見える要素があれば、修正promptを作るか再生成します。
