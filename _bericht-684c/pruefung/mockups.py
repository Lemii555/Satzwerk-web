#!/usr/bin/env python3
"""Mockups 684c: Kevins zwölf Bildschirmfotos in den Rahmen der heutigen Mockups setzen, als WebP in den heutigen Maßen.

Aufruf (aus der Wurzel des Zweigs):  python3 _bericht-684c/pruefung/mockups.py [_vorlage-684/iphone]
Erwartet dort start|training|live|verlauf|muskel|koerper je -de.png und -en.png (LIESMICH.md). Fehlt eines,
bricht das Skript ab, ohne etwas zu schreiben. Schreibt img/mockup-<platz>-<sprache>.webp.

Der Rahmen (mockup-rahmen/rahmen-800x1659.png, rahmen-640x1327.png) ist aus den heutigen Mockups gelöst:
der Bildschirm ist innerhalb des schwarzen Rings ausgestanzt. Das Foto wird auf die Bildschirmfläche
skaliert (Seitenverhältnis des iPhone-Fotos 1179 × 2556 passt bis auf ein Promille), mit runden Ecken
beschnitten und unter den Rahmen gelegt. start und training sind 800 × 1659, die anderen 640 × 1327."""
import sys, pathlib
from PIL import Image, ImageDraw
W = pathlib.Path(__file__).resolve().parents[2]
RAHMEN = W / "_bericht-684c/mockup-rahmen"
QUELLE = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else W / "_vorlage-684/iphone")
# Platz -> (Rahmendatei, Bildschirmfläche x0 y0 x1 y1, Eckradius), gemessen an den heutigen Mockups
PLAETZE = {"start": ("rahmen-800x1659.png", (35, 41, 763, 1632), 94), "training": ("rahmen-800x1659.png", (35, 41, 763, 1632), 94),
           "live": ("rahmen-640x1327.png", (28, 31, 610, 1294), 83), "verlauf": ("rahmen-640x1327.png", (28, 31, 610, 1294), 83),
           "muskel": ("rahmen-640x1327.png", (28, 31, 610, 1294), 83), "koerper": ("rahmen-640x1327.png", (28, 31, 610, 1294), 83)}
fehlt = [f"{p}-{s}.png" for p in PLAETZE for s in ("de", "en") if not (QUELLE / f"{p}-{s}.png").is_file()]
if fehlt: sys.exit("ABBRUCH, es fehlen in " + str(QUELLE) + ": " + ", ".join(fehlt))
for platz, (rahmen, (x0, y0, x1, y1), r) in PLAETZE.items():
    for sprache in ("de", "en"):
        rahmen_bild = Image.open(RAHMEN / rahmen).convert("RGBA")
        foto = Image.open(QUELLE / f"{platz}-{sprache}.png").convert("RGBA")
        bw, bh = x1 - x0 + 1, y1 - y0 + 1
        foto = foto.resize((bw, bh), Image.LANCZOS)
        maske = Image.new("L", (bw, bh), 0); ImageDraw.Draw(maske).rounded_rectangle((0, 0, bw - 1, bh - 1), radius=r, fill=255)
        aus = Image.new("RGBA", rahmen_bild.size, (0, 0, 0, 0)); aus.paste(foto, (x0, y0), maske); aus.alpha_composite(rahmen_bild)
        ziel = W / "img" / f"mockup-{platz}-{sprache}.webp"; aus.save(ziel, "WEBP", quality=82, method=6)
        print("geschrieben", ziel.relative_to(W), aus.size)
