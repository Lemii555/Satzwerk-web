#!/usr/bin/env python3
"""Ticket 684c: Farben, Bewegung auf den sechs Seiten. Jede Ersetzung muss genau so oft treffen wie angegeben,
sonst bricht das Skript ab (Exit 1) und aendert nichts."""
import re, sys, pathlib
WURZEL = pathlib.Path(__file__).resolve().parents[2]
SEITEN = ["index.html", "auswertung/index.html", "ueber/index.html", "datenschutz/index.html", "impressum/index.html"]

ROOT_NEU = """/* ---------- Farben: alle Werte hier, sonst nirgends ----------
   Nur hell. Die Werte sind die der App (_vorlage-684/website-684/tokens.css,
   dort steht zu jedem Wert der Name in src/stil.js); keine Farbe, die
   tokens.css nicht hat (Ticket 684c, 22.10.2026). Kein Schatten: die App
   traegt auf Karten keinen. */
:root{
  --grund:#F2F2F7;        /* --grund, systemGray6 */
  --band:#E5E5EA;         /* --linie-leise, systemGray5: Spur, Band, Fuss */
  --karte:#FFFFFF;        /* --weiss */
  --tinte:#000000;        /* --tinte */
  --leise:#5C5C5E;        /* --tinte-leiser */
  --kante:#D1D1D6;        /* --linie, systemGray4 */
  --akzent:#8116E0;       /* --marke */
  --marke-voll:#8116E0;
  --auf-marke:#FFFFFF;
  --store-voll:#000000;
  --schatten:none;
  --leiste-schatten:none;
  --segment-schatten:none;
  /* Bewegung: die eine Kurve und die Dauern der App (tokens.css, Ticket 298) */
  --kurve-bewegung:cubic-bezier(.33, 1, .68, 1);
  --dauer-auftritt:1.5s;
  --dauer-bewegung:.5s;
  --auftritt-blur:6px;
  color-scheme:light;
}"""

FUELLEN_ALT = """/* Die Marke laeuft von links hinein, ueberall gleich. :hover nur mit Zeiger,
   am iPhone bliebe er sonst nach dem Tippen haengen. */
.fuellen{ position:relative; isolation:isolate; overflow:hidden; transition:color .475s ease }
.fuell{ position:absolute; inset:0; z-index:-1; border-radius:inherit; pointer-events:none;
  background:var(--marke-voll); clip-path:inset(0 100% 0 0); transition:clip-path .475s ease }
@media (hover:hover){
  .fuellen:hover{ color:var(--auf-marke) }
  .fuellen:hover .fuell{ clip-path:inset(0 0 0 0) }
  .fuellen:hover .nur-hell{ display:none }
  .fuellen:hover .nur-dunkel{ display:block }
}
.fuellen:active,.fuellen:focus-visible{ color:var(--auf-marke) }
.fuellen:active .fuell,.fuellen:focus-visible .fuell{ clip-path:inset(0 0 0 0) }
.fuellen:active .nur-hell,.fuellen:focus-visible .nur-hell{ display:none }
.fuellen:active .nur-dunkel,.fuellen:focus-visible .nur-dunkel{ display:block }"""
FUELLEN_NEU = """/* Zeigen und Druecken: wie in 684 nur die Deckkraft, mit der Kurve der App.
   Der Fuelleffekt von links faellt weg (684c: ein Bewegungsmuster). Die
   leeren .fuell-Spannen im HTML bleiben stehen und tun nichts. :hover nur mit
   Zeiger, am iPhone bliebe er sonst nach dem Tippen haengen. */
.fuellen{ transition:opacity var(--dauer-bewegung) var(--kurve-bewegung) }
.fuell{ display:none }
@media (hover:hover){ .fuellen:hover{ opacity:.8 } }
.fuellen:active{ opacity:.8 }"""

RUHE_ALT = """/* Pflicht: alles still, wenn der Nutzer es so eingestellt hat */
@media (prefers-reduced-motion: reduce){
  *{ animation:none !important; transition:none !important }
  .blende{ opacity:1; transform:none }
}"""
RUHE_NEU = """/* ---------- Bewegung: ein Muster, einmal (aus 684) ----------
   tlTitelAuftritt der App: aus der Unschaerfe, ohne Weg. Was .auftritt traegt,
   tritt einmal auf, wenn es ins Bild kommt (das Skript setzt .da), mit der
   Kurve der App. Ohne Skript und bei reduzierter Bewegung gibt es keinen
   versteckten Anfangszustand: die Animation steht nur unter no-preference,
   und der Ruhe-Block schaltet jede Bewegung ab. */
@keyframes tritt{ from{ opacity:0; filter:blur(var(--auftritt-blur)) } to{ opacity:1; filter:blur(0) } }
@media (prefers-reduced-motion: no-preference){
  .js .auftritt{ animation:tritt var(--dauer-auftritt) var(--kurve-bewegung) both; animation-play-state:paused }
  .js .auftritt.da{ animation-play-state:running }
}
/* RUHE-BLOCK: reduzierte Bewegung heisst Endzustand, sofort */
@media (prefers-reduced-motion: reduce){
  *, *::before, *::after{ animation:none !important; transition:none !important }
  .auftritt{ opacity:1 !important; filter:none !important }
}"""

BLENDE_ALT = """/* Einmal einblenden beim Laden, gestaffelt 0 / 120 / 240 ms. Danach nichts mehr. */
.blende{ opacity:0; transform:translateY(12px);
  animation:einblenden 600ms cubic-bezier(0.16,1,0.3,1) forwards }
.blende-2{ animation-delay:120ms }
.blende-3{ animation-delay:240ms }
@keyframes einblenden{ to{ opacity:1; transform:none } }

"""
SCHWEBEN_ALT = """@keyframes schweben{ from{ transform:translateY(-9px) } to{ transform:translateY(9px) } }
.mockup-vorn{ animation:schweben 6.0s ease-in-out infinite alternate }
.mockup-hinten{ animation:schweben 7.4s ease-in-out infinite alternate; animation-delay:-2.1s }
"""
SCHWEBEN_NEU = """/* Kein Schweben mehr (684c): die Mockups stehen, sie treten mit dem Kopf auf. */
"""

KOPFSKRIPT_ALT = """(function(){ try{ localStorage.removeItem("satzwerk-modus"); }catch(err){} })();"""
KOPFSKRIPT_NEU = """(function(){ try{ localStorage.removeItem("satzwerk-modus"); }catch(err){} })();
/* .js vor dem ersten Zeichnen: nur mit Skript gibt es den Auftritt (684c). */
document.documentElement.classList.add("js");"""

SPRACHE_ALT = """  document.querySelectorAll("[data-sprachknopf]").forEach(function(k){
    k.addEventListener("click", function(){
      setzeSprache(html.getAttribute("lang") === "de" ? "en" : "de");
    });
  });

})();"""
SPRACHE_NEU = """  document.querySelectorAll("[data-sprachknopf]").forEach(function(k){
    k.addEventListener("click", function(){
      setzeSprache(html.getAttribute("lang") === "de" ? "en" : "de");
    });
  });

  /* Auftritt (aus 684, seite.js): einmal, beim Reinscrollen. Das Skript setzt
     nur die Klasse .da, die Bewegung selbst steht im CSS. Ohne
     IntersectionObserver steht alles sofort. */
  (function beobachte(auswahl, schwelle){
    var ziele = Array.prototype.slice.call(document.querySelectorAll(auswahl));
    if (!("IntersectionObserver" in window)) { ziele.forEach(function(el){ el.classList.add("da"); }); return; }
    var io = new IntersectionObserver(function(eintraege){
      eintraege.forEach(function(e){
        if (!e.isIntersecting) return;
        e.target.classList.add("da");
        io.unobserve(e.target);
      });
    }, { threshold: schwelle });
    ziele.forEach(function(el){ io.observe(el); });
  })(".auftritt", 0);

})();"""

SPRACHE_UNTER_ALT = """  document.querySelectorAll("[data-sprachknopf]").forEach(function(k){
    k.addEventListener("click", function(){
      setzeSprache(h.getAttribute("data-lang") === "en" ? "de" : "en");
    });
  });
})();"""
BEOBACHTER = SPRACHE_NEU.split("\n\n", 1)[1]
SPRACHE_UNTER_NEU = SPRACHE_UNTER_ALT[:-len("})();")] + "\n" + BEOBACHTER

def ersetze(text, alt, neu, n, name, datei):
    k = text.count(alt)
    if k != n:
        sys.exit(f"ABBRUCH {datei}: '{name}' trifft {k} mal, erwartet {n}")
    return text.replace(alt, neu)

ALLE = [  # (alt, neu, anzahl, name) fuer die fuenf grossen Seiten
    ('<meta name="theme-color" content="#F4F2EE">', '<meta name="theme-color" content="#F2F2F7">', 1, "theme-color"),
    (FUELLEN_ALT, FUELLEN_NEU, 1, "fuellen"),
    ("""  transition:background-color .2s ease, color .2s ease }""",
     """  transition:color var(--dauer-bewegung) var(--kurve-bewegung) }""", 1, "segment-transition"),
    ("""@media (hover:hover){ .segment:hover{ color:var(--tinte); background:rgba(0,0,0,.05) } }""",
     """@media (hover:hover){ .segment:hover{ color:var(--tinte) } }""", 1, "segment-hover"),
    (RUHE_ALT, RUHE_NEU, 1, "ruhe-block"),
    (KOPFSKRIPT_ALT, KOPFSKRIPT_NEU, 1, "kopfskript-js"),
]
START = [(SPRACHE_ALT, SPRACHE_NEU, 1, "beobachter")] + [
    (BLENDE_ALT, "", 1, "blende-css"),
    (SCHWEBEN_ALT, SCHWEBEN_NEU, 1, "schweben"),
    ("""  transform:rotate(45deg); transition:transform 200ms ease }""",
     """  transform:rotate(45deg); transition:transform var(--dauer-bewegung) var(--kurve-bewegung) }""", 1, "faq-pfeil"),
    ('<h1 id="titel" class="blende"', '<h1 id="titel" class="auftritt"', 1, "h1"),
    ('<p class="blende blende-2" data-t="lead"', '<p class="auftritt" data-t="lead"', 1, "lead"),
    ('<div class="blende blende-3"><a class="store', '<div class="auftritt"><a class="store', 1, "store"),
    ('<p class="klein blende blende-3" data-t="hinweis"', '<p class="klein auftritt" data-t="hinweis"', 1, "hinweis"),
    ('<div class="mockups blende blende-2">', '<div class="mockups auftritt">', 1, "mockups"),
    ('<h2 id="zeigen-titel"', '<h2 id="zeigen-titel" class="auftritt"', 1, "h2 zeigen"),
    ('<h2 id="haltung-titel"', '<h2 id="haltung-titel" class="auftritt"', 1, "h2 haltung"),
    ('<h2 id="drin-titel"', '<h2 id="drin-titel" class="auftritt"', 1, "h2 drin"),
    ('<h2 id="pro-titel">', '<h2 id="pro-titel" class="auftritt">', 1, "h2 pro"),
    ('<h2 id="faq-titel"', '<h2 id="faq-titel" class="auftritt"', 1, "h2 faq"),
]
UNTER = {
    "auswertung/index.html": [(SPRACHE_UNTER_ALT, SPRACHE_UNTER_NEU, 1, "beobachter"), ("<h1>Was Satzwerk auswertet</h1>", '<h1 class="auftritt">Was Satzwerk auswertet</h1>', 1, "h1 de"),
                              ("<h1>What Satzwerk analyzes</h1>", '<h1 class="auftritt">What Satzwerk analyzes</h1>', 1, "h1 en")],
    "ueber/index.html": [(SPRACHE_UNTER_ALT, SPRACHE_UNTER_NEU, 1, "beobachter"), ("<h1>Über Satzwerk</h1>", '<h1 class="auftritt">Über Satzwerk</h1>', 1, "h1 de"),
                         ("<h1>About Satzwerk</h1>", '<h1 class="auftritt">About Satzwerk</h1>', 1, "h1 en")],
    "datenschutz/index.html": [(SPRACHE_UNTER_ALT, SPRACHE_UNTER_NEU, 1, "beobachter"), ("<h1>Datenschutz</h1>", '<h1 class="auftritt">Datenschutz</h1>', 1, "h1 de"),
                               ("<h1>Privacy</h1>", '<h1 class="auftritt">Privacy</h1>', 1, "h1 en")],
    "impressum/index.html": [(SPRACHE_UNTER_ALT, SPRACHE_UNTER_NEU, 1, "beobachter"), ("<h1>Impressum</h1>", '<h1 class="auftritt">Impressum</h1>', 1, "h1 de"),
                             ("<h1>Legal notice</h1>", '<h1 class="auftritt">Legal notice</h1>', 1, "h1 en")],
}

ROOT_RE = re.compile(r"/\* ---------- Farben: alle Werte hier, sonst nirgends ----------.*?\n:root\{.*?color-scheme:light;\n\}", re.S)

for s in SEITEN:
    p = WURZEL / s
    t = p.read_text(encoding="utf-8")
    if len(ROOT_RE.findall(t)) != 1:
        sys.exit(f"ABBRUCH {s}: :root-Block nicht genau einmal")
    t = ROOT_RE.sub(lambda m: ROOT_NEU, t)
    for alt, neu, n, name in ALLE + (START if s == "index.html" else UNTER[s]):
        t = ersetze(t, alt, neu, n, name, s)
    p.write_text(t, encoding="utf-8")
    print("umgebaut", s)

# 404: nur Farben
p = WURZEL / "404.html"
t = p.read_text(encoding="utf-8")
t = ersetze(t, '<meta name="theme-color" content="#F4F2EE">', '<meta name="theme-color" content="#F2F2F7">', 1, "theme-color", "404.html")
t = ersetze(t, "  --grund:#F4F2EE;", "  --grund:#F2F2F7;        /* --grund der App, systemGray6 (684c) */", 1, "grund", "404.html")
p.write_text(t, encoding="utf-8")
print("umgebaut 404.html")
