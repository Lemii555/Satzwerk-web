#!/usr/bin/env python3
"""Korrektur 684c (Kevin, 22.10.2026, 09:19): Fuelleffekt und Segment-Pillen zurueck wie in 5d382dd,
Leiste auf breiten Schirmen so breit wie die Fusskarte. Jede Ersetzung muss genau einmal treffen."""
import sys, pathlib, subprocess, re
W = pathlib.Path(__file__).resolve().parents[2]
SEITEN = ["index.html", "auswertung/index.html", "ueber/index.html", "datenschutz/index.html", "impressum/index.html"]
alt = subprocess.run(["git", "-C", str(W), "show", "5d382dd:index.html"], capture_output=True, text=True, check=True).stdout
# Der Fuelleffekt, woertlich aus 5d382dd (vom Kommentar bis zur letzten :focus-visible-Zeile)
FUELLEN_5D = re.search(r"/\* Die Marke laeuft von links hinein.*?\.fuellen:active \.nur-dunkel,\.fuellen:focus-visible \.nur-dunkel\{ display:block \}", alt, re.S).group(0)
FUELLEN_684C = """/* Zeigen und Druecken: wie in 684 nur die Deckkraft, mit der Kurve der App.
   Der Fuelleffekt von links faellt weg (684c: ein Bewegungsmuster). Die
   leeren .fuell-Spannen im HTML bleiben stehen und tun nichts. :hover nur mit
   Zeiger, am iPhone bliebe er sonst nach dem Tippen haengen. */
.fuellen{ transition:opacity var(--dauer-bewegung) var(--kurve-bewegung) }
.fuell{ display:none }
@media (hover:hover){ .fuellen:hover{ opacity:.8 } }
.fuellen:active{ opacity:.8 }"""
E = [
    (FUELLEN_684C, FUELLEN_5D, "fuellen zurueck"),
    ("""  --schatten:none;
  --leiste-schatten:none;
  --segment-schatten:none;""",
     """  --schatten:none;        /* Karten ohne Schatten (684c) */
  /* Die Segmentleiste wie in 5d382dd (Korrektur 684c, 22.10.2026): Spur = Band,
     das gewaehlte Segment = weisse Pille mit dem Schatten des iOS-Segmented-
     Control. Schatten und Zustaende, keine Creme: benannte Ausnahme in farben.py. */
  --leiste-schatten:0 4px 16px rgba(0,0,0,.08);
  --segment-schatten:0 3px 8px rgba(0,0,0,.12), 0 3px 1px rgba(0,0,0,.04);""", "schatten der leiste"),
    ("""@media (hover:hover){ .segment:hover{ color:var(--tinte) } }""",
     """@media (hover:hover){ .segment:hover{ color:var(--tinte); background:rgba(0,0,0,.05) } }""", "segment hover"),
    ("""  transition:color var(--dauer-bewegung) var(--kurve-bewegung) }
.segment svg{""",
     """  transition:background-color .2s ease, color .2s ease }
.segment svg{""", "segment transition wie 5d382dd"),
    ("""   Der Kopf selbst ist durchsichtig und laesst Klicks durch, nur die Leiste
   nimmt sie an. */""",
     """   Der Kopf selbst ist durchsichtig und laesst Klicks durch, nur die Leiste
   nimmt sie an. Ab 900 px ist die Leiste so breit wie die Fusskarte (Korrektur
   684c, 22.10.2026): Rand 24 px wie .rahmen, hoechstens 1120 minus 48 px.
   Wortmarke links, App Store rechts, die Segmente dazwischen. */""", "kommentar kopf"),
    (""".kopf-innen{ position:relative; z-index:1; width:max-content; max-width:100%; margin:0 auto;
  pointer-events:auto }""",
     """.kopf-innen{ position:relative; z-index:1; width:max-content; max-width:100%; margin:0 auto;
  pointer-events:auto }
@media (min-width:900px){
  .kopf{ padding:12px 24px }
  .kopf-innen{ width:100%; max-width:1072px }
  .segment-marke{ margin-right:auto }
  .kopf-innen .leiste .store{ margin-left:auto }   /* schlaegt .leiste .store{ margin-left:4px } weiter unten */
}""", "leiste breit"),
]
for s in SEITEN:
    p = W / s; t = p.read_text(encoding="utf-8")
    for a, n, name in E:
        if t.count(a) != 1: sys.exit(f"ABBRUCH {s}: '{name}' trifft {t.count(a)} mal")
        t = t.replace(a, n)
    p.write_text(t, encoding="utf-8"); print("korrigiert", s)
