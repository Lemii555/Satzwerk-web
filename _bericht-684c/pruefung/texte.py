#!/usr/bin/env python3
"""Textvergleich 684c: alle sichtbaren Texte (Textknoten ausser script/style), die Attribute alt, aria-label, title,
content (meta) und die TEXTE-Objekte (DE und EN) jeder Seite, Wort für Wort gegen den Stand vorher.
Aufruf: texte.py VORHER-ORDNER NACHHER-ORDNER. Exit 1 bei einer Abweichung."""
import sys, re, json, pathlib, subprocess
from html.parser import HTMLParser
SEITEN = ["index.html", "auswertung/index.html", "ueber/index.html", "datenschutz/index.html", "impressum/index.html", "404.html"]
class P(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True); s.still = 0; s.texte = []; s.attr = []
    def handle_starttag(s, tag, attrs):
        if tag in ("script", "style"): s.still += 1
        for k, v in attrs:
            if k in ("alt", "aria-label", "title", "content", "placeholder") and v and not re.fullmatch(r"#[0-9A-Fa-f]{6}", v): s.attr.append(f"{tag}[{k}]={v}")
    def handle_endtag(s, tag):
        if tag in ("script", "style"): s.still -= 1
    def handle_data(s, d):
        if not s.still and d.strip(): s.texte.append(" ".join(d.split()))
def texte_obj(html):
    m = re.search(r"var TEXTE = (\{.*?\n\});", html, re.S)
    if not m: return None
    out = subprocess.run(["node", "-e", "var TEXTE=" + m.group(1) + ";process.stdout.write(JSON.stringify(TEXTE))"], capture_output=True, text=True, check=True)
    return json.loads(out.stdout)
def lese(pfad):
    h = pathlib.Path(pfad).read_text(encoding="utf-8"); p = P(); p.feed(h)
    return " ".join(p.texte), p.attr, texte_obj(h)
vorher, nachher = sys.argv[1], sys.argv[2]; rot = 0
for s in SEITEN:
    r0 = rot
    tv, av, ov = lese(f"{vorher}/{s}"); tn, an, on = lese(f"{nachher}/{s}")
    wv, wn = tv.split(), tn.split()
    if wv != wn:
        rot += 1; import difflib
        print(f"ROT {s}: sichtbarer Text weicht ab"); print("\n".join(list(difflib.unified_diff(wv, wn, lineterm="", n=2))[:40]))
    if av != an:
        rot += 1; print(f"ROT {s}: Attribute weichen ab"); print(set(av) ^ set(an))
    if ov != on:
        rot += 1; print(f"ROT {s}: TEXTE-Objekt weicht ab")
    print(f"{'ROT' if rot > r0 else 'GRUEN'} {s}: {len(wv)} Wörter, {len(av)} Attribute, TEXTE {'gleich' if ov == on else 'ANDERS'}")
sys.exit(1 if rot else 0)
