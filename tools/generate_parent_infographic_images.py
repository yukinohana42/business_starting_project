from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "output" / "parent_infographic_images_day1_5"
OUT_DIR.mkdir(parents=True, exist_ok=True)

FONT_REG = r"C:\Windows\Fonts\YuGothM.ttc"
FONT_BOLD = r"C:\Windows\Fonts\YuGothB.ttc"

W, H = 1600, 2263
M = 110

COLORS = {
    "navy": "#1F3A5F",
    "ink": "#1D2939",
    "muted": "#667085",
    "line": "#D8E0EA",
    "paper": "#F5F8FC",
    "white": "#FFFFFF",
    "blue": "#2F6FED",
    "green": "#14996B",
    "orange": "#F08A24",
    "purple": "#7B61FF",
    "red": "#DC4C3E",
    "yellow": "#F3B61F",
    "light_blue": "#EEF5FF",
    "light_green": "#EEF9F5",
    "light_orange": "#FFF6EA",
    "light_purple": "#F4F0FF",
    "light_red": "#FFF1F0",
    "light_yellow": "#FFF9E8",
    "dark_panel": "#15233A",
}


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def text_w(draw, text, f):
    return draw.textbbox((0, 0), text, font=f)[2]


def wrap_text(draw, text, f, width):
    lines = []
    for raw in str(text).split("\n"):
        if not raw:
            lines.append("")
            continue
        current = ""
        for ch in raw:
            candidate = current + ch
            if text_w(draw, candidate, f) <= width:
                current = candidate
            else:
                if current:
                    lines.append(current)
                current = ch
        if current:
            lines.append(current)
    return lines


def draw_text(draw, xy, text, f, fill, width=None, line_gap=10):
    x, y = xy
    if width is None:
        draw.text((x, y), text, font=f, fill=fill)
        return y + f.size + line_gap
    for line in wrap_text(draw, text, f, width):
        draw.text((x, y), line, font=f, fill=fill)
        y += int(f.size * 1.55)
    return y


def rounded(draw, box, radius, fill, outline=None, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def header(draw, day_no, title, subtitle, accent):
    draw.rectangle((0, 0, W, 92), fill=COLORS["navy"])
    draw.rectangle((int(W * 0.38), 0, W, 92), fill=accent)
    draw.text((M, 126), f"Day {day_no}", font=font(32, True), fill=accent)
    draw.text((W - M - 92, 126), f"{day_no} / 5", font=font(24), fill=COLORS["muted"])
    draw.text((M, 178), title, font=font(58, True), fill=COLORS["navy"])
    draw_text(draw, (M, 270), subtitle, font(31, True), COLORS["ink"], W - M * 2, 8)


def card(draw, x, y, w, h, title, body, accent, fill="#FBFDFF", title_size=31, body_size=25):
    rounded(draw, (x, y, x + w, y + h), 22, fill, COLORS["line"], 2)
    draw.rounded_rectangle((x + 22, y + 24, x + 82, y + 42), radius=9, fill=accent)
    draw.text((x + 28, y + 62), title, font=font(title_size, True), fill=COLORS["navy"])
    draw_text(draw, (x + 28, y + 116), body, font(body_size), COLORS["ink"], w - 56, 8)


def section(draw, x, y, label, accent):
    draw.rounded_rectangle((x, y, x + 14, y + 44), radius=7, fill=accent)
    draw.text((x + 30, y - 2), label, font=font(34, True), fill=COLORS["navy"])


def step(draw, x, y, w, n, text, accent):
    h = 126
    rounded(draw, (x, y, x + w, y + h), 20, COLORS["white"], COLORS["line"], 2)
    draw.ellipse((x + 28, y + 30, x + 78, y + 80), fill=accent)
    draw.text((x + 45, y + 36), str(n), font=font(27, True), fill=COLORS["white"])
    draw_text(draw, (x + 100, y + 28), text, font(27), COLORS["ink"], w - 130, 6)
    return y + h + 20


def footer(draw, text):
    draw.line((M, H - 122, W - M, H - 122), fill=COLORS["line"], width=2)
    draw_text(draw, (M, H - 92), text, font(24), COLORS["muted"], W - M * 2)


def formula(draw, x, y, w, text):
    rounded(draw, (x, y, x + w, y + 72), 18, COLORS["dark_panel"], None, 0)
    tw = text_w(draw, text, font(26, True))
    draw.text((x + (w - tw) / 2, y + 18), text, font=font(26, True), fill=COLORS["white"])


def day_image(cfg):
    img = Image.new("RGB", (W, H), COLORS["white"])
    draw = ImageDraw.Draw(img)
    accent = cfg["accent"]
    header(draw, cfg["day"], cfg["title"], cfg["subtitle"], accent)

    half = (W - M * 2 - 28) // 2
    y = 430
    card(draw, M, y, half, 270, "目的", cfg["purpose"], accent, cfg["light"])
    card(draw, M + half + 28, y, half, 270, "成果物", cfg["output"], accent, COLORS["paper"])
    if cfg.get("formula"):
        formula(draw, M + half + 58, y + 174, half - 60, cfg["formula"])

    y = 770
    section(draw, M, y, "やり方", accent)
    y += 78
    for i, s in enumerate(cfg["steps"], 1):
        y = step(draw, M, y, W - M * 2, i, s, accent)

    if cfg.get("three_cards"):
        y += 12
        cw = (W - M * 2 - 40) // 3
        for i, (t, b) in enumerate(cfg["three_cards"]):
            card(draw, M + i * (cw + 20), y, cw, 235, t, b, accent, COLORS["paper"], 27, 21)
        y += 265
    elif cfg.get("signal_cards"):
        y += 10
        cw = (W - M * 2 - 40) // 3
        signal = [
            ("青信号", "自分から使いたがる\n友達にすすめる\n2回目も使う", COLORS["blue"], COLORS["light_blue"]),
            ("黄信号", "面白いけど続かなそう\n説明すれば反応する\n今は困っていない", COLORS["yellow"], COLORS["light_yellow"]),
            ("赤信号", "反応が薄い\n今の方法で満足\n誰の問題かぼんやり", COLORS["red"], COLORS["light_red"]),
        ]
        for i, (t, b, a, f) in enumerate(signal):
            card(draw, M + i * (cw + 20), y, cw, 260, t, b, a, f, 28, 23)
        y += 290

    if y < H - 420:
        y = H - 410
    card(draw, M, y, W - M * 2, 210, "親の関わり", cfg["parent"], accent, cfg["light"], 31, 26)
    footer(draw, cfg["footer"])
    return img


CONFIGS = [
    {
        "day": 1,
        "title": "働く・お金・価値",
        "subtitle": "仕事は「物を売ること」だけではなく、誰かの状態を良くすることだと理解します。",
        "accent": COLORS["green"],
        "light": COLORS["light_green"],
        "purpose": "仕事は誰かへの価値提供であり、お金はその対価だと知る。\n問い: 一番ラクに稼いでいそうな仕事は？",
        "output": "最後に、仕事の意味を1文でまとめます。",
        "formula": "仕事とは、____ を ____ に変えること。",
        "steps": [
            "ラーメン屋、コンビニ、YouTuberなど、身近な仕事を出す。",
            "その仕事が「誰のどんな状態を良くしているか」を考える。",
            "困ったを助かったに、面倒をラクに、退屈を楽しいに変えるゲームをする。",
            "仕事とお金を「価値へのありがとう」として言い換える。",
        ],
        "three_cards": [
            ("子供がやること", "仕事の例を出す\n誰が助かっているか考える\n価値変換の1文を書く"),
            ("親が聞くこと", "その仕事は誰をどう助けている？"),
            ("見たい変化", "お金ではなく価値から仕事を見る"),
        ],
        "parent": "正解を言わず、「その仕事は誰をどう助けている？」と聞きます。",
        "footer": "Day1の合言葉: 仕事は、誰かの状態を少し良くすること。",
        "filename": "day1_value_work.png",
    },
    {
        "day": 2,
        "title": "価値の見つけ方",
        "subtitle": "すごい発明だけがビジネスの種ではありません。日常の不満、面倒、好きの中から価値の種を探します。",
        "accent": COLORS["orange"],
        "light": COLORS["light_orange"],
        "purpose": "困りごとや欲しい気持ちを観察し、相手に聞く準備をする。\n問い: 最近イラッとしたことは？",
        "output": "困りごとリストと、3人に聞くインタビュー質問を作る。",
        "steps": [
            "最近のイラッ、面倒、もっと楽しくしたいことを10個出す。",
            "それは誰が、いつ、どれくらい困っているのかを考える。",
            "家族、友達、先生など安全な相手に聞く質問を作る。",
            "次回までに3人へインタビューする。",
        ],
        "three_cards": [
            ("良い聞き方", "最近それで困ったことはある？\n今はどうやって解決している？"),
            ("避けたい聞き方", "こういうアプリがあったら使う？だけで終わらせない"),
            ("宿題", "安全な身近な相手に3人聞く"),
        ],
        "parent": "「欲しい？」ではなく、過去の行動を聞くよう促します。相手の個人情報は書かず、安全な相手にだけ聞きます。",
        "footer": "Day2の合言葉: 困りごとは、価値の種。",
        "filename": "day2_finding_value.png",
    },
    {
        "day": 3,
        "title": "アイデア作り",
        "subtitle": "インタビューから見えた困りごとをもとに、「誰の何を解決するのか」を具体的にします。",
        "accent": COLORS["purple"],
        "light": COLORS["light_purple"],
        "purpose": "自分たちが作りたいものではなく、相手が本当に欲しいものに近づける。\n問い: 誰が一番困っている？",
        "output": "誰の何を解決するかを、基本文でまとめます。",
        "formula": "これは、____ な人が ____ で困る時のサービス",
        "steps": [
            "インタビュー結果を共有し、意外だった答えを出す。",
            "「みんな」ではなく、助けたい具体的な1人にしぼる。",
            "10分で20個の解決案を出す。変な案も出してよい。",
            "困り度、頻度、試しやすさで点数をつけ、1つ選ぶ。",
        ],
        "three_cards": [
            ("困り度", "本当に困っているか"),
            ("頻度", "何度も起きるか"),
            ("試しやすさ", "明日小さく試せるか"),
        ],
        "parent": "「もっとすごい案にしよう」ではなく、「誰が一番困っている？」「今はどうしている？」に戻します。",
        "footer": "Day3の合言葉: 良いアイデアは、誰に、どんな価値を、どう届けるかが見える。",
        "filename": "day3_idea_creation.png",
    },
    {
        "day": 4,
        "title": "PMFと小さな実験",
        "subtitle": "PMFは、作ったものと欲しい人の気持ちがピタッとはまること。完璧に作る前に、小さく試します。",
        "accent": COLORS["red"],
        "light": COLORS["light_red"],
        "purpose": "作りたいものではなく、相手が本当に欲しいものになっているか確認する。\n問い: 無料なら使う人は本当に欲しい人？",
        "output": "小さな実験計画を1つ作る。",
        "steps": [
            "PMFを「作ったものと欲しい人の気持ちがピタッとはまること」と説明する。",
            "反応を青、黄、赤の信号で見る。赤信号も学びとして扱う。",
            "紙の説明、LINE、1回だけのお試しなど、作り込まない方法を選ぶ。",
            "誰に試してもらい、何を観察するかを決める。",
        ],
        "signal_cards": True,
        "parent": "赤信号を失敗扱いしません。「この方向ではないとわかった学び」として、次に直すところを一緒に考えます。",
        "footer": "Day4の合言葉: 完璧に考えるより、小さく試して反応を見る。",
        "filename": "day4_pmf_experiment.png",
    },
    {
        "day": 5,
        "title": "3分ピッチとセミナー準備",
        "subtitle": "起業セミナーに参加する前に、自分たちの視点を持ち、誰のどんな問題をどう解くのかを3分で説明します。",
        "accent": COLORS["blue"],
        "light": COLORS["light_blue"],
        "purpose": "ただ話を聞くだけではなく、セミナーで見るポイントを持って参加する。\n問い: 何を一番伝える？",
        "output": "3分ピッチ原稿と、セミナーで聞きたい質問メモ。",
        "steps": [
            "僕たちが見つけた問題は、______ です。",
            "困っている人は、______ です。",
            "今は ______ で解決していますが、______ という不満があります。",
            "そこで僕たちは、______ を考えました。まずは ______ で試します。",
        ],
        "three_cards": [
            ("親が見る", "誰の問題か具体的か\n今の方法の不満があるか"),
            ("セミナーで見る", "他の人はどんな問題を見つけたか"),
            ("質問する", "どう試す？誰に聞いた？"),
        ],
        "parent": "発表の上手さより、「誰の何を解決するのか」「本当に使いたい人はいるか」「まず何を試すか」を質問します。",
        "footer": "Day5の合言葉: すごさより、誰のどんな問題をどう解くかが伝わること。",
        "filename": "day5_pitch.png",
    },
]


def main():
    created = []
    for cfg in CONFIGS:
        img = day_image(cfg)
        path = OUT_DIR / cfg["filename"]
        img.save(path, format="PNG", optimize=True)
        created.append(path)

    (OUT_DIR / "README.md").write_text(
        "# 親御さん向けインフォグラフィック画像 Day1-5\n\n"
        "PDFではなく、1日1枚のPNG画像として保存しています。\n\n"
        + "\n".join(f"- `{p.name}`" for p in created)
        + "\n",
        encoding="utf-8",
    )

    for p in created:
        print(f"{p.name}\t{p.stat().st_size}")
    print(f"folder={OUT_DIR}")


if __name__ == "__main__":
    main()
