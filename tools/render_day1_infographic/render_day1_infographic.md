# Day1インフォグラフィック レンダリング手順

## 目的

第1回の6枚構成インフォグラフィックを、PDFではなく日本語文字化けしにくいPNG画像として出力する。

## 元ファイル

- `outputs/day1/session_01_infographic_zoom.md`: 6枚の基本内容
- `outputs/day1/session_01_infographic_copy.md`: ページごとのコピーと図解要素
- `outputs/day1/session_01_infographic_spec.md`: 16:9 / 4:5、文字量、Zoom可読性の設計
- `DESIGN.md`: 色、余白、フォント、みんほす！らしい温かいトーン

## HTML/CSS化の方法

- 16:9版は `outputs/day1/rendered/session_01_infographic_16x9.html` と `session_01_infographic_16x9.css` にまとめる
- 4:5版は `outputs/day1/rendered/session_01_infographic_4x5.html` と `session_01_infographic_4x5.css` にまとめる
- 各ページは `section.page[data-page="1"]` から `data-page="6"` として固定サイズにする
- 図解は画像素材に頼らず、HTML/CSSのカード、矢印、簡単なアイコンで構成する

## PNG化の方法

Chromeのheadless screenshotでHTMLを開き、`?page=1` から `?page=6` の表示を順番にPNG化する。HTML側では、クエリで指定された1ページだけを表示する。

推奨コマンド:

```powershell
$env:NODE_PATH="C:\Users\yukin\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\node_modules"
node tools\render_day1_infographic\render_day1_infographic.cjs
```

Codex bundled Node.jsを明示して使う場合:

```powershell
$env:NODE_PATH="C:\Users\yukin\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\node_modules"
& "C:\Users\yukin\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe" tools\render_day1_infographic\render_day1_infographic.cjs
```

## 16:9版の出力

- サイズ: 1920 x 1080 px
- 用途: Zoom画面共有のメイン教材
- 出力: `outputs/day1/rendered/session_01_infographic_16x9_page_01.png` から `page_06.png`
- 一覧確認: `outputs/day1/rendered/session_01_infographic_16x9_contact_sheet.png`

## 4:5版の出力

- サイズ: 1080 x 1350 px
- 用途: スマホ共有、SNS共有、縦長プレビューの試作
- 出力: `outputs/day1/rendered/session_01_infographic_4x5_page_01.png` から `page_06.png`
- 16:9版より文字を少し短くし、カードを縦積みにしている

## 日本語文字化けを避けるためにしたこと

- PDFではなくPNGで出力する
- HTMLに `<meta charset="utf-8">` を入れる
- CSSで `BIZ UDGothic`, `Yu Gothic`, `Meiryo` を優先する
- ブラウザで描画した状態をそのまま画像化する

## Zoomでの確認方法

1. `outputs/day1/rendered/session_01_infographic_16x9_page_01.png` から順に開く
2. Zoomの画面共有で画像を全画面表示する
3. 文字が小さく見えるページがあれば、HTML/CSS側で文章量か文字サイズを調整する
4. 45分台本のタイミングに合わせて、1枚ずつ切り替えて使う

## 今後修正するときに触るファイル

- 文言を変える: `outputs/day1/rendered/session_01_infographic_16x9.html` と `session_01_infographic_4x5.html`
- 見た目を変える: `outputs/day1/rendered/session_01_infographic_16x9.css` と `session_01_infographic_4x5.css`
- 出力方法を変える: `tools/render_day1_infographic/render_day1_infographic.cjs`
- 元の考え方を変える: `outputs/day1/session_01_infographic_spec.md`
