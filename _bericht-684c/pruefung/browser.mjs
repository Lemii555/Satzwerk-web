/* Browserprüfung 684c: sechs Seiten × fünf Breiten × DE/EN × Bewegung an/aus in Chromium.
   Prüft: kein waagerechtes Scrollen, kein Element über der Kante, Auftritt im Endzustand (Deckkraft 1),
   Sprache gesetzt, alle internen Links und Bilder 200. Schreibt Bilder nach _bericht-684c/bilder/.
   Aufruf: NODE_PATH=/opt/node-tools/node_modules node browser.mjs http://127.0.0.1:8084 */
import { createRequire } from "node:module";
const { chromium } = createRequire(import.meta.url)(process.env.PLAYWRIGHT_PFAD || "/opt/node-tools/node_modules/playwright");
import fs from "node:fs"; import path from "node:path";
const BASIS = process.argv[2] || "http://127.0.0.1:8084";
const HIER = path.dirname(new URL(import.meta.url).pathname);
const BILDER = path.join(HIER, "..", "bilder");
const SEITEN = [["start", "/"], ["auswertung", "/auswertung/"], ["ueber", "/ueber/"], ["datenschutz", "/datenschutz/"], ["impressum", "/impressum/"], ["404", "/404.html"]];
const BREITEN = [[375, 812], [393, 852], [430, 932], [1280, 800], [1440, 900]];
const browser = await chromium.launch();
const fehler = [], zeilen = [], geprueft = new Map();

async function pruefeLinks(page, pfad) {
  const urls = await page.evaluate(() => {
    const u = new Set();
    document.querySelectorAll("a[href], img[src], link[href]").forEach(el => {
      const v = el.getAttribute("href") || el.getAttribute("src");
      if (!v || /^(mailto:|https?:|#|tel:)/.test(v)) return;
      u.add(new URL(v, location.href).pathname);
    });
    return [...u];
  });
  for (const u of urls) {
    if (geprueft.has(u)) continue;
    const r = await page.request.get(BASIS + u);
    geprueft.set(u, r.status());
    if (r.status() !== 200) fehler.push(`${pfad}: ${u} -> ${r.status()}`);
  }
}

for (const [name, pfad] of SEITEN) for (const [w, h] of BREITEN) for (const sprache of ["de", "en"]) for (const bewegung of ["reduce", "no-preference"]) {
  const ctx = await browser.newContext({ viewport: { width: w, height: h }, reducedMotion: bewegung, deviceScaleFactor: 1, locale: sprache === "de" ? "de-DE" : "en-US" });
  await ctx.addInitScript(s => { try { localStorage.setItem("satzwerk-sprache", s); } catch (e) {} }, sprache);
  const page = await ctx.newPage();
  const konsole = []; page.on("pageerror", e => konsole.push(String(e)));
  await page.goto(BASIS + pfad, { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready);
  if (bewegung === "no-preference") {
    // einmal durchscrollen, damit jeder Auftritt ins Bild kommt, dann warten, bis die 1,5 s vorbei sind
    const hoehe = await page.evaluate(() => document.documentElement.scrollHeight);
    for (let y = 0; y < hoehe; y += Math.floor(h * 0.8)) { await page.evaluate(y => window.scrollTo(0, y), y); await page.waitForTimeout(60); }
    await page.evaluate(() => window.scrollTo(0, 0)); await page.waitForTimeout(1700);
  }
  const m = await page.evaluate(() => {
    const d = document.documentElement, iw = window.innerWidth;
    const ueber = [];
    document.querySelectorAll("body *").forEach(el => {
      if (el.classList.contains("sprung") || el.closest("[hidden]") || el.closest(".sprung")) return;
      const r = el.getBoundingClientRect(); if (r.width === 0 && r.height === 0) return;
      const st = getComputedStyle(el); if (st.display === "none" || st.visibility === "hidden") return;
      if (r.right > iw + 1 || r.left < -1) ueber.push(`${el.tagName.toLowerCase()}${el.id ? "#" + el.id : ""}.${[...el.classList].join(".")} l=${Math.round(r.left)} r=${Math.round(r.right)}`);
    });
    const auftritte = [...document.querySelectorAll(".auftritt")].filter(el => el.getClientRects().length > 0).map(el => ({ da: el.classList.contains("da"), op: getComputedStyle(el).opacity, f: getComputedStyle(el).filter }));
    return { scrollW: d.scrollWidth, clientW: d.clientWidth, bodyScrollW: document.body.scrollWidth, ueber: ueber.slice(0, 6), auftritte, lang: d.getAttribute("lang"), hoehe: d.scrollHeight,
      grund: getComputedStyle(document.body).backgroundColor,
      leiste: (() => { const l = document.querySelector(".leiste"), f = document.querySelector(".fuss-karte"); if (!l || !f) return null;
        const a = l.getBoundingClientRect(), b = f.getBoundingClientRect(); return { l: a.left, r: a.right, fl: b.left, fr: b.right }; })(), lauf: [...document.getAnimations()].filter(a => a.playState === "running" && a.effect && a.effect.getTiming().iterations === Infinity).length };
  });
  const kennung = `${name}-${w}-${sprache}-${bewegung === "reduce" ? "ruhe" : "bewegt"}`;
  const probleme = [];
  if (m.scrollW > m.clientW || m.bodyScrollW > m.clientW) probleme.push(`waagerecht scrollbar ${m.scrollW}/${m.bodyScrollW} > ${m.clientW}`);
  if (m.ueber.length) probleme.push("über der Kante: " + m.ueber.join(" | "));
  if (name !== "404" && m.lang !== sprache) probleme.push(`Sprache ${m.lang} statt ${sprache}`);
  if (m.grund !== "rgb(242, 242, 247)") probleme.push(`Grund ${m.grund}`);
  if (m.lauf) probleme.push(`${m.lauf} Endlosschleife(n)`);
  // Korrektur 684c: ab 900 px Kanten der Leiste gegen die Kanten der Fusskarte, Toleranz 1 px
  if (w >= 900 && name !== "404") {
    if (!m.leiste) probleme.push("Leiste oder Fusskarte fehlt");
    else if (Math.abs(m.leiste.l - m.leiste.fl) > 1 || Math.abs(m.leiste.r - m.leiste.fr) > 1) probleme.push(`Leiste ${m.leiste.l}..${m.leiste.r} gegen Fusskarte ${m.leiste.fl}..${m.leiste.fr}`);
  }
  const nichtDa = m.auftritte.filter(a => a.op !== "1" || (a.f !== "none" && a.f !== "blur(0px)"));
  if (nichtDa.length) probleme.push(`${nichtDa.length} Auftritte nicht im Endzustand: ` + JSON.stringify(nichtDa.slice(0, 3)));
  if (bewegung === "no-preference" && name !== "404" && m.auftritte.length === 0) probleme.push("kein .auftritt auf der Seite");
  if (konsole.length) probleme.push("Skriptfehler: " + konsole.join("; "));
  if (probleme.length) fehler.push(`${kennung}: ${probleme.join("; ")}`);
  zeilen.push(`| ${name} | ${w} | ${sprache} | ${bewegung === "reduce" ? "aus" : "an"} | ${m.scrollW}/${m.clientW} | ${m.hoehe} | ${m.auftritte.length} | ${m.leiste && w >= 900 ? `${Math.round(m.leiste.l)}–${Math.round(m.leiste.r)} / ${Math.round(m.leiste.fl)}–${Math.round(m.leiste.fr)}` : "–"} | ${probleme.length ? "ROT" : "ok"} |`);
  if (sprache === "de" && bewegung === "reduce") await pruefeLinks(page, pfad);
  // Bilder: ganze Seite auf 393 und 1440 (DE und EN, bewegt = Endzustand); nur oben auf 375, 430, 1280 (DE, Ruhe)
  if ((w === 393 || w === 1440) && bewegung === "no-preference") await page.screenshot({ path: path.join(BILDER, kennung + ".jpg"), fullPage: true, type: "jpeg", quality: 55 });
  else if ((w === 375 || w === 430 || w === 1280) && sprache === "de" && bewegung === "reduce") await page.screenshot({ path: path.join(BILDER, kennung + "-oben.jpg"), type: "jpeg", quality: 55 });
  await ctx.close();
}
// Ein Bild mitten im Auftritt: Startseite 393, 0,4 s nach dem Laden
{
  const ctx = await browser.newContext({ viewport: { width: 393, height: 852 }, reducedMotion: "no-preference" });
  const page = await ctx.newPage(); await page.goto(BASIS + "/", { waitUntil: "load" }); await page.waitForTimeout(400);
  await page.screenshot({ path: path.join(BILDER, "start-393-de-auftritt-0,4s.jpg"), type: "jpeg", quality: 55 });
  await ctx.close();
}
// Korrektur 684c: Bilder mit erzwungenem :hover (Playwright hover = echter Zeiger), dazu das gewaehlte Segment
{
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, reducedMotion: "reduce", hasTouch: false });
  const page = await ctx.newPage();
  const schuss = async (datei, clip) => page.screenshot({ path: path.join(BILDER, datei), type: "jpeg", quality: 80, clip });
  await page.goto(BASIS + "/", { waitUntil: "load" }); await page.evaluate(() => document.fonts.ready);
  const leiste = await page.locator(".leiste").boundingBox();
  const clipLeiste = { x: Math.max(0, leiste.x - 24), y: 0, width: Math.min(1440, leiste.width + 48), height: leiste.y + leiste.height + 24 };
  await page.hover(".leiste .store"); await page.waitForTimeout(600); await schuss("hover-store-1440.jpg", clipLeiste);
  await page.hover(".leiste a.segment[href='/auswertung/']"); await page.waitForTimeout(400); await schuss("hover-segment-1440.jpg", clipLeiste);
  const kreis = page.locator(".kreise .kreis").first(); await kreis.scrollIntoViewIfNeeded(); await kreis.hover(); await page.waitForTimeout(600);
  const kb = await kreis.boundingBox(); await schuss("hover-instagram-kreis-1440.jpg", { x: kb.x - 160, y: kb.y - 120, width: 480, height: 300 });
  await page.hover(".held .store"); await page.waitForTimeout(600); const hb = await page.locator(".held .store").boundingBox();
  await schuss("hover-store-gross-1440.jpg", { x: hb.x - 40, y: hb.y - 40, width: hb.width + 160, height: hb.height + 80 });
  await page.goto(BASIS + "/auswertung/", { waitUntil: "load" }); await page.evaluate(() => document.fonts.ready);
  await page.mouse.move(0, 500); await schuss("gewaehltes-segment-auswertung-1440.jpg", clipLeiste);
  await page.mouse.move(0, 500); await page.goto(BASIS + "/", { waitUntil: "load" }); await page.evaluate(() => document.fonts.ready);
  await schuss("leiste-1440.jpg", clipLeiste);
  await page.setViewportSize({ width: 1280, height: 800 }); await page.waitForTimeout(200);
  const l2 = await page.locator(".leiste").boundingBox(); await schuss("leiste-1280.jpg", { x: 0, y: 0, width: 1280, height: l2.y + l2.height + 24 });
  await ctx.close();
}
await browser.close();
const bericht = ["| Seite | Breite | Sprache | Bewegung | scrollWidth/clientWidth | Höhe | .auftritt | Leiste / Fusskarte (px) | Ergebnis |", "|---|---|---|---|---|---|---|---|---|", ...zeilen].join("\n");
fs.writeFileSync(path.join(HIER, "browser-ergebnis.md"), bericht + "\n\n## Links und Bilder\n\n" + [...geprueft].map(([u, s]) => `${s} ${u}`).sort().join("\n") + "\n\n## Fehler\n\n" + (fehler.length ? fehler.join("\n") : "keine") + "\n");
console.log(fehler.length ? "ROT\n" + fehler.join("\n") : `GRUEN: ${zeilen.length} Lagen, ${geprueft.size} Adressen`);
process.exit(fehler.length ? 1 : 0);
