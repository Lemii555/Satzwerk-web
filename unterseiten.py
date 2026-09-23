# -*- coding: utf-8 -*-
# Baut Impressum und Datenschutz im Rahmen der Startseite: Kopf, Fuss, Farben
# und Glas kommen aus der GEBAUTEN index.html (eine Quelle), der Rechtstext
# (<main>) unveraendert aus den bisherigen Seiten.
import re, json, sys
WEB = "/sessions/determined-funny-newton/mnt/outputs/satzwerk-web/"
QUELLE = WEB+"quellen/"          # die Seiten vor diesem Umbau
idx = open(WEB+"index.html", encoding="utf-8").read()

def zwischen(s, a, b, mit=True):
    i = s.index(a); j = s.index(b, i) + (len(b) if mit else 0)
    assert s.count(a) == 1, a
    return s[i:j]

css = zwischen(idx, "<style>", "</style>")
# Startseiten-Abschnitte ohne Gegenstueck auf den Unterseiten raus
held = css.index("/* ---------- Heldenbereich")
fuss = css.index("/* ---------- Fuss ----------")
assert held < fuss and css.count("/* ---------- Heldenbereich") == 1
css = css[:held] + css[fuss:]
fruehskript = zwischen(idx, "<script>\n/* Hell oder dunkel", "</script>")
sprung = zwischen(idx, '<a class="sprung"', "</a>")
kopf   = zwischen(idx, "<!-- Die Brechung", "</header>")
fuss_h = zwischen(idx, "<footer>", "</footer>")
texte  = json.loads(re.search(r"var TEXTE = (\{.*?\n\});", idx, re.S).group(1))
SCHL = ["skip","lang","lang_aria","store","claim","fuss2","folgen","rechtliches",
        "impressum","datenschutz","fuss_iphone","marken","ig_label","li_label"]
klein = {l: {k: texte[l][k] for k in SCHL} for l in ("de","en")}

def unter(pfad):   # img/ liegt eine Ebene hoeher
    return pfad.replace('src="img/', 'src="../img/').replace('href="img/', 'href="../img/')

def seite(name, stand_abstand):
    alt = open(QUELLE+name+".html", encoding="utf-8").read()
    titel = re.search(r"<title>.*?</title>", alt).group(0)
    besch = re.search(r'<meta name="description"[^>]*>', alt).group(0)
    main  = zwischen(alt, "<main>", "</main>")
    assert main.count("<main>") == 1
    main  = main.replace("<main>", '<main class="recht" id="inhalt">', 1)
    eigen = """
/* ---------- Rechtstext ----------
   Die Regeln der bisherigen Seite, auf main.recht begrenzt: die Startseite
   setzt h1, h2, p und .klein fuer ihren Aufbau, der Rechtstext braucht
   seine eigene, ruhigere Leiter. */
main.recht{ max-width:760px; margin:0 auto; padding:40px 24px 96px }
main.recht h1{ font-family:"Fraunces","Iowan Old Style","Palatino Linotype",serif; font-weight:700;
  font-size:clamp(32px,6vw,44px); line-height:1.1; letter-spacing:-.02em; margin:0 0 8px }
main.recht .stand{ color:var(--leise); font-size:15px; margin:0 0 %dpx }
main.recht h2{ font-family:"Public Sans","Helvetica Neue",Arial,sans-serif; font-size:20px; font-weight:600;
  line-height:1.3; margin:44px 0 12px; letter-spacing:-.01em }
main.recht h3{ font-size:17px; font-weight:600; margin:28px 0 8px }
main.recht p{ margin:0 0 14px; max-width:62ch }
main.recht ul{ margin:0 0 14px; padding-left:20px; max-width:62ch }
main.recht li{ margin:0 0 6px }
main.recht address{ font-style:normal; margin:0 0 14px }
main.recht a{ text-decoration:none }
main.recht a:hover{ text-decoration:underline }
main.recht .klein{ font-size:15px; color:var(--leise) }
main.recht .karte{ background:var(--karte); box-shadow:var(--schatten); border-radius:20px;
  padding:24px 28px; margin:0 0 8px }
main.recht .karte p:last-child,main.recht .karte ul:last-child{ margin-bottom:0 }
main.recht .kurz{ border-left:3px solid var(--akzent); padding:4px 0 4px 20px; margin:0 0 40px }
main.recht .kurz p{ font-size:19px; margin-bottom:8px }
main.recht .kurz p:last-child{ margin-bottom:0 }
main.recht hr{ border:0; border-top:1px solid var(--kante); margin:56px 0 }
/* Sprachumschaltung im Rechtstext: DE- und EN-Block stehen beide im
   Dokument, data-lang am html waehlt. Kopf und Fuss uebersetzt das Skript. */
main [lang="en"]{ display:none }
html[data-lang="en"] main [lang="de"]{ display:none }
html[data-lang="en"] main>[lang="en"]{ display:block }
html[data-lang="en"] main [lang="en"].klein{ display:inline }
""" % stand_abstand
    css_s = css.replace("</style>", eigen + "</style>")
    skript = """<script>
/* Kopf und Fuss wie auf der Startseite; der Rechtstext hat DE- und EN-Block.
   Ohne gespeicherte Wahl entscheidet die Browsersprache (wie bisher). */
var TEXTE = %s;
(function(){
  var h = document.documentElement;
  function hole(o, k){ return o && o[k]; }
  function setzeSprache(l){
    var t = TEXTE[l] || TEXTE.de;
    h.setAttribute("data-lang", l); h.setAttribute("lang", l);
    document.querySelectorAll("[data-t]").forEach(function(el){
      var v = hole(t, el.getAttribute("data-t")); if (typeof v === "string") el.textContent = v; });
    document.querySelectorAll("[data-t-aria]").forEach(function(el){
      var v = hole(t, el.getAttribute("data-t-aria")); if (typeof v === "string") el.setAttribute("aria-label", v); });
    try{ localStorage.setItem("satzwerk-sprache", l); }catch(e){}
  }
  var g = null; try{ g = localStorage.getItem("satzwerk-sprache"); }catch(e){}
  setzeSprache(g === "de" || g === "en" ? g : ((navigator.language||"de").slice(0,2) === "de" ? "de" : "en"));
  document.getElementById("sprache").addEventListener("click", function(){
    setzeSprache(h.getAttribute("data-lang") === "en" ? "de" : "en");
  });
})();
</script>""" % json.dumps(klein, ensure_ascii=False, indent=1)
    s = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{titel}
{besch}
<meta name="robots" content="index,follow">
<meta name="theme-color" media="(prefers-color-scheme: light)" content="#F4F2EE">
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="#000000">
<link rel="icon" href="../img/bildmarke.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="../img/apple-touch-icon.png">
<link rel="preload" href="/fonts/fraunces.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/publicsans.woff2" as="font" type="font/woff2" crossorigin>
{fruehskript}
{css_s}
</head>
<body>
{sprung}

{unter(kopf)}

{main}

{unter(fuss_h)}

{skript}
</body>
</html>
"""
    assert 'src="img/' not in s and "satzwerk-modus\", neu" not in s and 'id="modus"' not in s
    return s

for name, abstand in (("impressum", 48), ("datenschutz", 40)):
    s = seite(name, abstand)
    for ziel in (WEB+name+"/index.html",
                 "/sessions/determined-funny-newton/mnt/Satzwerk App/website-satzwerk/"+name+"/index.html"):
        open(ziel, "w", encoding="utf-8").write(s)
    print(name, "ok", len(s))
