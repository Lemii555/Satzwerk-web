#!/usr/bin/env python3
"""Wortprüfung 684c (DE und EN) über die sechs Seiten. Exit 1 bei einem Treffer."""
import re, sys, pathlib
W = pathlib.Path(__file__).resolve().parents[2]
SEITEN = ["index.html", "auswertung/index.html", "ueber/index.html", "datenschutz/index.html", "impressum/index.html", "404.html"]
MUSTER = [r"kostenlos", r"gratis", r"umsonst", r"kein Abo", r"keine Cloud", r"keine fertigen Pl", r"nur schreibend", r"für immer",
          r"\bfor free\b", r"\bis free\b", r"\bare free\b", r"\bfree of charge\b", r"\bfree version\b", r"\bfree app\b", r"\bfree forever\b",
          r"\bforever\b", r"\bno subscription", r"\bno cloud\b", r"\bno ready-made plans\b", r"\bwrite-only\b", r"\bonly writes\b"]
treffer = 0
for s in SEITEN:
    for i, zeile in enumerate((W / s).read_text(encoding="utf-8").splitlines(), 1):
        for m in MUSTER:
            if re.search(m, zeile, re.I):
                print(f"TREFFER {s}:{i} [{m}] {zeile.strip()[:120]}"); treffer += 1
print("GRUEN: kein Treffer" if not treffer else f"ROT: {treffer} Treffer")
sys.exit(1 if treffer else 0)
