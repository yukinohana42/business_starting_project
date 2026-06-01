const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");
const { pathToFileURL } = require("url");
const Module = require("module");

if (process.env.NODE_PATH) {
  Module._initPaths();
}

const { PNG } = require("pngjs");

const ROOT = path.resolve(__dirname, "..", "..");
const OUT_DIR = path.join(ROOT, "outputs", "day1", "rendered");

const CHROME_CANDIDATES = [
  "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe",
  "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
  "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
];

const RENDERS = [
  {
    name: "16x9",
    width: 1920,
    height: 1080,
    html: "session_01_infographic_16x9.html",
    prefix: "session_01_infographic_16x9_page_",
  },
  {
    name: "4x5",
    width: 1080,
    height: 1350,
    html: "session_01_infographic_4x5.html",
    prefix: "session_01_infographic_4x5_page_",
  },
];

function pad2(n) {
  return String(n).padStart(2, "0");
}

async function renderDeck(chromePath, config) {
  const htmlPath = path.join(OUT_DIR, config.html);
  const created = [];
  for (let i = 1; i <= 6; i += 1) {
    const output = path.join(OUT_DIR, `${config.prefix}${pad2(i)}.png`);
    const url = `${pathToFileURL(htmlPath).href}?page=${i}`;
    execFileSync(chromePath, [
      "--headless=new",
      "--disable-gpu",
      "--disable-gpu-sandbox",
      "--disable-software-rasterizer",
      "--disable-accelerated-2d-canvas",
      "--disable-features=VizDisplayCompositor",
      "--no-sandbox",
      "--hide-scrollbars",
      "--allow-file-access-from-files",
      "--force-device-scale-factor=1",
      `--window-size=${config.width},${config.height}`,
      `--screenshot=${output}`,
      "--virtual-time-budget=1000",
      url,
    ], { stdio: "pipe" });
    created.push(output);
  }
  return created;
}

async function createContactSheet(files) {
  const thumbW = 480;
  const thumbH = 270;
  const gap = 28;
  const width = gap + 3 * thumbW + 2 * gap + gap;
  const height = gap + 2 * thumbH + gap + gap;
  const sheet = new PNG({ width, height });
  fillPng(sheet, 255, 248, 237, 255);

  for (let i = 0; i < files.length; i += 1) {
    const row = Math.floor(i / 3);
    const col = i % 3;
    const left = gap + col * (thumbW + gap);
    const top = gap + row * (thumbH + gap);
    const source = PNG.sync.read(fs.readFileSync(files[i]));
    drawResized(source, sheet, left, top, thumbW, thumbH);
  }

  const output = path.join(OUT_DIR, "session_01_infographic_16x9_contact_sheet.png");
  fs.writeFileSync(output, PNG.sync.write(sheet));
  return output;
}

function fillPng(png, r, g, b, a) {
  for (let y = 0; y < png.height; y += 1) {
    for (let x = 0; x < png.width; x += 1) {
      const idx = (png.width * y + x) << 2;
      png.data[idx] = r;
      png.data[idx + 1] = g;
      png.data[idx + 2] = b;
      png.data[idx + 3] = a;
    }
  }
}

function drawResized(source, target, left, top, width, height) {
  for (let y = 0; y < height; y += 1) {
    const srcY = Math.floor((y / height) * source.height);
    for (let x = 0; x < width; x += 1) {
      const srcX = Math.floor((x / width) * source.width);
      const sourceIdx = (source.width * srcY + srcX) << 2;
      const targetIdx = (target.width * (top + y) + (left + x)) << 2;
      target.data[targetIdx] = source.data[sourceIdx];
      target.data[targetIdx + 1] = source.data[sourceIdx + 1];
      target.data[targetIdx + 2] = source.data[sourceIdx + 2];
      target.data[targetIdx + 3] = source.data[sourceIdx + 3];
    }
  }
}

async function main() {
  fs.mkdirSync(OUT_DIR, { recursive: true });
  const chromePath = CHROME_CANDIDATES.find((candidate) => fs.existsSync(candidate));
  if (!chromePath) {
    throw new Error("Chrome or Edge executable was not found.");
  }

  const rendered = {};
  for (const config of RENDERS) {
    rendered[config.name] = await renderDeck(chromePath, config);
  }

  const contactSheet = await createContactSheet(rendered["16x9"]);

  for (const [name, files] of Object.entries(rendered)) {
    console.log(`${name}: ${files.length} PNG files`);
    for (const file of files) {
      const meta = PNG.sync.read(fs.readFileSync(file));
      console.log(`- ${path.relative(ROOT, file)} ${meta.width}x${meta.height}`);
    }
  }
  const sheetMeta = PNG.sync.read(fs.readFileSync(contactSheet));
  console.log(`contact-sheet: ${path.relative(ROOT, contactSheet)} ${sheetMeta.width}x${sheetMeta.height}`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
