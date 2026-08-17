import { build } from "esbuild";
import { cp, mkdir, readFile, rm, writeFile } from "node:fs/promises";
import { fileURLToPath, pathToFileURL } from "node:url";
import React from "react";
import { renderToStaticMarkup } from "react-dom/server";

const outputDir = new URL("../docs/", import.meta.url);
const compiledPage = new URL("../.static-page.mjs", import.meta.url);

await rm(outputDir, { recursive: true, force: true });
await mkdir(outputDir, { recursive: true });
await cp(new URL("../public/", import.meta.url), outputDir, { recursive: true });

await build({
  entryPoints: [fileURLToPath(new URL("../app/page.tsx", import.meta.url))],
  outfile: fileURLToPath(compiledPage),
  bundle: true,
  format: "esm",
  platform: "node",
  jsx: "automatic",
  external: ["react", "react-dom", "react/jsx-runtime"],
});

const { default: Home } = await import(`${pathToFileURL(fileURLToPath(compiledPage))}?v=${Date.now()}`);
const markup = renderToStaticMarkup(React.createElement(Home))
  .replaceAll('src="/', 'src="./')
  .replaceAll('href="/', 'href="./');
const css = (await readFile(new URL("../app/globals.css", import.meta.url), "utf8"))
  .replace(/^@import\s+"tailwindcss";\s*/m, "")
  .replaceAll("url('/", "url('./");

const html = `<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="ЮАР — 10 дней жизни на краю света. Авторское путешествие по Кейптауну.">
  <meta property="og:title" content="ЮАР — 10 дней жизни на краю света">
  <meta property="og:description" content="Кейптаун, океан, сафари, винодельни и люди, которые покажут страну изнутри.">
  <meta property="og:image" content="./og.png">
  <title>ЮАР — 10 дней жизни на краю света</title>
  <link rel="icon" href="./favicon.svg">
  <style>${css}</style>
</head>
<body>${markup}</body>
</html>`;

await writeFile(new URL("index.html", outputDir), html);
await writeFile(new URL(".nojekyll", outputDir), "");
await rm(compiledPage, { force: true });
