#!/usr/bin/env python3
"""Fuelleffekt-Vergleich (Korrektur 684c): der .fuellen/.fuell-Block jeder Seite muss byte-gleich mit 5d382dd sein,
ebenso die Leisten-Schatten und .segment:hover. Aufruf: fuell.py [Datei ...]. Exit 1 = ROT."""
import re, sys, pathlib, subprocess
W = pathlib.Path(__file__).resolve().parents[2]
SEITEN = ["index.html", "auswertung/index.html", "ueber/index.html", "datenschutz/index.html", "impressum/index.html"]
alt = subprocess.run(["git", "-C", str(W), "show", "5d382dd:index.html"], capture_output=True, text=True, check=True).stdout
STUECKE = {
    "fuellen": r"\.fuellen\{ position:relative.*?\.fuellen:active \.nur-dunkel,\.fuellen:focus-visible \.nur-dunkel\{ display:block \}",
    "leiste-schatten": r"--leiste-schatten:[^\n]*", "segment-schatten": r"--segment-schatten:[^\n]*",
    "segment-hover": r"\.segment:hover\{[^}]*\}",
}
soll = {k: re.search(m, alt, re.S).group(0) for k, m in STUECKE.items()}
rot = 0
for s in (sys.argv[1:] or SEITEN):
    t = pathlib.Path(s).read_text(encoding="utf-8")
    for k, m in STUECKE.items():
        f = re.search(m, t, re.S)
        if not f or f.group(0) != soll[k]:
            print(f"ROT  {s}: '{k}' weicht von 5d382dd ab" + ("" if f else " (fehlt)")); rot += 1
    print(f"{'ROT' if rot else 'GRUEN'}  {s}")
sys.exit(1 if rot else 0)
