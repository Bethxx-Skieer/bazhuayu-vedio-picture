#!/usr/bin/env node

import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { pathToFileURL } from "node:url";

const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";

function parseArgs(argv) {
  if (!argv.length) {
    throw new Error("Usage: export_xhs_templates.mjs TEMPLATE_DIR [--output-dir DIR] [--montage-path FILE]");
  }
  const result = { templateDir: argv[0], outputDir: null, montagePath: null };
  for (let index = 1; index < argv.length; index += 1) {
    const option = argv[index];
    const value = argv[index + 1];
    if (option === "--output-dir" && value) {
      result.outputDir = value;
      index += 1;
    } else if (option === "--montage-path" && value) {
      result.montagePath = value;
      index += 1;
    } else {
      throw new Error(`Unknown or incomplete option: ${option}`);
    }
  }
  return result;
}

function escapeHtml(value) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

async function renderPage(browser, source, output, width, height) {
  const page = await browser.newPage({ viewport: { width, height }, deviceScaleFactor: 1 });
  try {
    await page.goto(pathToFileURL(source).href, { waitUntil: "load" });
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: output, fullPage: false });
  } finally {
    await page.close();
  }
}

function montageDocument(previews, canvasHeight) {
  const cards = previews.map(({ file, label }) => `
    <figure class="card">
      <img src="${escapeHtml(pathToFileURL(file).href)}" alt="">
      <figcaption>${escapeHtml(label)}</figcaption>
    </figure>`).join("");

  return `<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <style>
    * { box-sizing: border-box; }
    html, body { width: 2160px; height: ${canvasHeight}px; margin: 0; overflow: hidden; }
    body {
      padding: 78px 40px 20px;
      background: linear-gradient(145deg, #eef6ff, #dceaff);
      color: #14213d;
      font-family: "PingFang SC", "Microsoft YaHei", sans-serif;
    }
    h1 { position: absolute; top: 18px; left: 56px; margin: 0; font-size: 38px; }
    .grid {
      display: grid;
      grid-template-columns: repeat(4, 360px);
      gap: 20px 28px;
      justify-content: center;
    }
    .card {
      position: relative;
      width: 360px;
      height: 480px;
      margin: 0;
      overflow: hidden;
      border: 1px solid rgba(0, 85, 255, 0.16);
      border-radius: 18px;
      background: white;
      box-shadow: 0 14px 32px rgba(35, 76, 138, 0.13);
    }
    .card img { display: block; width: 100%; height: 100%; object-fit: cover; }
    .card figcaption {
      position: absolute;
      left: 0;
      right: 0;
      bottom: 0;
      padding: 13px 16px 15px;
      background: rgba(20, 33, 61, 0.86);
      color: white;
      font-size: 25px;
      font-weight: 650;
      text-align: center;
    }
  </style>
</head>
<body>
  <h1>八爪鱼冰蓝模板总览</h1>
  <main class="grid">${cards}</main>
</body>
</html>`;
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const templateDir = path.resolve(args.templateDir);
  const outputDir = path.resolve(args.outputDir ?? templateDir);
  const playwrightEntry = path.resolve(path.dirname(process.execPath), "..", "node_modules", "playwright", "index.mjs");
  const { chromium } = await import(pathToFileURL(playwrightEntry).href);

  await fs.mkdir(outputDir, { recursive: true });
  const entries = await fs.readdir(templateDir, { withFileTypes: true });
  const templates = entries
    .filter((entry) => entry.isFile() && entry.name.endsWith(".html"))
    .map((entry) => entry.name)
    .sort((left, right) => left.localeCompare(right, "zh-CN"));
  if (!templates.length) throw new Error(`No HTML templates found in ${templateDir}`);

  const browser = await chromium.launch({
    headless: true,
    executablePath: chrome,
    args: ["--no-sandbox", "--disable-gpu", "--allow-file-access-from-files"],
  });
  try {
    const previews = [];
    for (const name of templates) {
      const source = path.join(templateDir, name);
      const label = path.basename(name, ".html");
      const output = path.join(outputDir, `${label}.png`);
      process.stdout.write(`Rendering ${name} ...\n`);
      await renderPage(browser, source, output, 1080, 1440);
      previews.push({ file: output, label });
      process.stdout.write(`${output}\n`);
    }

    if (args.montagePath) {
      const montagePath = path.resolve(args.montagePath);
      const montageRows = Math.ceil(previews.length / 4);
      const montageHeight = 78 + montageRows * 480 + Math.max(0, montageRows - 1) * 20 + 20;
      await fs.mkdir(path.dirname(montagePath), { recursive: true });
      const tempDir = await fs.mkdtemp(path.join(os.tmpdir(), "codex-xhs-montage-"));
      try {
        const source = path.join(tempDir, "montage.html");
        await fs.writeFile(source, montageDocument(previews, montageHeight), "utf8");
        await renderPage(browser, source, montagePath, 2160, montageHeight);
        process.stdout.write(`${montagePath}\n`);
      } finally {
        await fs.rm(tempDir, { recursive: true, force: true });
      }
    }
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
