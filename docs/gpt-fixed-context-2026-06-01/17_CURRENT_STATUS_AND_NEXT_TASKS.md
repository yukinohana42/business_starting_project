# Current Status and Next Tasks

## 現在の状態

- 5回分のワークショップ設計は初稿として揃っている。
- 子供向けスライド原稿は5回分揃っている。
- 親向け説明スライドとインフォグラフィック原稿がある。
- PDF版は文字化けリスクがあるため、PNG画像版が実用的。
- カード教材とワークシートは初稿として揃っている。
- `.agents/skills/` に5つのSkillがある。
- 第1回のZoom実施パッケージは `outputs/day1/` に作成済み。
- 第1回のZoom共有用複数枚インフォグラフィック原稿は6枚構成で作成済み。
- 第1回のZoom共有用インフォグラフィックは16:9 PNG 6枚として `outputs/day1/rendered/` に出力済み。
- 4:5版のスマホ共有用試作PNG 6枚も `outputs/day1/rendered/` に出力済み。
- Gitリポジトリは初期化済みで、GitHubへの初回pushは成功済み。

## Git/GitHub固定状態

- Git repo: あり
- project root: `C:\Users\yukin\OneDrive\ドキュメント\Starting_a_business_for_family\junior-entrepreneurship-workshop`
- GitHub repo: `https://github.com/yukinohana42/business_starting_project.git`
- branch: `main`
- initial pushed HEAD: `5719070925575acca6ca0b92eefa2c7eafa73543`
- remote main HEAD: `5719070925575acca6ca0b92eefa2c7eafa73543`
- worktree: clean at initial push
- initial commit message: `initial entrepreneurship workshop project`
- 主要フォルダ: `docs/`, `sessions/`, `slides/`, `cards/`, `worksheets/`, `outputs/`, `prompts/`, `tools/`, `.agents/`
- `output/parent_infographic_pdf/chrome-profile/` と `output/parent_infographic_pdf/edge-profile/` はブラウザプロファイル由来データを含むためpush対象外。
- `.gitignore` にブラウザプロファイル除外を追加済み。

## Priority 1

- 第1回Zoom実施パッケージを実際に画面共有で確認する。
- 第1回を実施し、子供の反応を `session_01_after_action_review.md` に記録する。
- 第1回PNGをZoomで実表示し、文字サイズとページ切り替えのテンポを確認する。
- 教材全体のデザイン方針を、ゲーミフィケーション、同世代に近い人物イラスト、マンガ的な具体例、価値の変化を見せる図解として具体化する。

## Priority 2

- 親向け説明スライドを10分説明用に整える。
- 5回全体の実施スケジュールを作る。
- 第2回のZoom実施パッケージを作る。
- Day1教材を、発見ゲームとして進む構成に磨く。

## Priority 3

- 全スライドのデザイン統一。
- PDF化、PPTX化、PNG化の安定した出力手順を作る。
- カードの印刷レイアウト化。

## 注意点

- `AGENTS.md` を正式なAI作業ルールファイルとして扱う。
- `SOURCE_OF_TRUTH.md` を正式な思想ファイルとして扱う。
- `SOURCE_OF_TRUTH.md` のファイル名を誤記しない。
- 教材改善時は、起業を押し付ける方向にしない。
- docs-only作業では、教材生成物、画像、PDF、PPTXを再生成しない。
- ブラウザプロファイル、Cookie、Login Data、Cache、Crashpad dump、`.env`、秘密情報をcommitしない。
- 既存漫画・アニメの固有キャラクター、ロゴ、固有の絵柄を模倣しない。
