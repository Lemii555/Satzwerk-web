#!/usr/bin/env python3
"""Farbprüfung 684c: jede Farbe in den sechs Seiten muss wörtlich in tokens.css stehen.
Aufruf: farben.py [Datei ...]   (ohne Argumente: die sechs Seiten). Exit 1 = ROT."""
import re, sys, pathlib
W = pathlib.Path(__file__).resolve().parents[2]
SEITEN = ["index.html", "auswertung/index.html", "ueber/index.html", "datenschutz/index.html", "impressum/index.html", "404.html"]
FARBE = re.compile(r"#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|hsla?\([^)]*\)")
tokens = {m.lower().replace(" ", "") for m in FARBE.findall((W / "_vorlage-684/website-684/tokens.css").read_text())}
# Benannte Ausnahmen (Korrektur 684c, Kevin 22.10.2026): Schatten und Zustaende der Segmentleiste wie in 5d382dd,
# keine Creme. Nichts anderes.
AUSNAHMEN = {"rgba(0,0,0,.08)": "--leiste-schatten", "rgba(0,0,0,.12)": "--segment-schatten", "rgba(0,0,0,.04)": "--segment-schatten",
             "rgba(0,0,0,.05)": ".segment:hover"}
tokens |= set(AUSNAHMEN)
rot = 0
for s in (sys.argv[1:] or SEITEN):
    t = pathlib.Path(s).read_text(encoding="utf-8")
    # ld+json und URLs tragen keine Farben; Anker wie href="#pro" sind keine Hex-Farben (kein Treffer, da kein Hex)
    for m in FARBE.finditer(t):
        f = m.group(0).lower().replace(" ", "")
        if f not in tokens:
            zeile = t.count("\n", 0, m.start()) + 1
            print(f"ROT  {s}:{zeile}  {m.group(0)}  nicht in tokens.css"); rot += 1
    print(f"{'ROT' if rot else 'GRUEN'}  {s}: {len(FARBE.findall(t))} Farbstellen")
sys.exit(1 if rot else 0)
