# Ticket 684c: Website 2.3 in den Farben der App, mit der Bewegung aus 684 — Bericht

**22.10.2026.** Zweig `website-2-3`, Basis Commit `5d382dd` (Stand 699, Texte vom 21.10.2026). Nichts auf `main`,
kein Merge, kein Pull Request. Geändert sind nur die sechs Seiten `index.html`, `auswertung/index.html`,
`ueber/index.html`, `datenschutz/index.html`, `impressum/index.html`, `404.html`; dazu neu der Ordner
`_bericht-684c/` (dieser Bericht, Bilder, Prüfskripte, Rahmen-Vorlagen). Alte Dateien im Repo nicht angefasst,
`img/` nicht angefasst (Mockups offen, Abschnitt 4).

Aufbau, Abschnitte, Navigation, Texte, Schrift und Adressen sind unverändert (Textvergleich Wort für Wort, Abschnitt 5).
Geändert haben sich nur die Farben, die Bewegung und die Dateigröße, die mit den Kommentaren leicht wächst.

## 1 · Ersetzte Farben (vorher → nachher)

Jede Farbe steht in jeder Seite nur einmal, im `:root`-Block. Alle Werte stehen wörtlich in
`_vorlage-684/website-684/tokens.css`; eine Farbe, die dort fehlt, gibt es nicht mehr (Prüfung `farben.py`, Abschnitt 5).

| Variable | vorher (Creme) | nachher | Name in tokens.css | wo sie steht |
|---|---|---|---|---|
| `--grund` | #F4F2EE | **#F2F2F7** | `--grund`, systemGray6 | Seitengrund (`body`), Handymenü |
| `--band` | #EDEAE5 | **#E5E5EA** | `--linie-leise`, systemGray5 | Spur der Segmentleiste, Abschnitte „Befunde, keine Anweisungen“ und „Satzwerk Pro“, Fußkarte |
| `--karte` | #FFFFFF | #FFFFFF | `--weiss` | Karten, gewähltes Segment, Kreise im Fuß |
| `--tinte` | #000000 | #000000 | `--tinte` | Text |
| `--leise` | #5C5C5E | #5C5C5E | `--tinte-leiser` | leiser Text |
| `--kante` | #DCD8D2 | **#D1D1D6** | `--linie`, systemGray4 | Rand der Segmentleiste und der „Folge uns“-Karte, Linien in den Listen, Rand der Frei/Pro-Kapseln, `hr` im Rechtstext |
| `--akzent`, `--marke-voll` | #8116E0 | #8116E0 | `--marke` | Marke, Links, Pro |
| `--auf-marke` | #FFFFFF | #FFFFFF | `--weiss` | Schrift auf dem Store-Knopf |
| `--store-voll` | #000000 | #000000 | `--tinte` | Store-Knopf |
| `--schatten` | 0 1px 3px rgba(0,0,0,.06) | **none** | – | Karten (Frei/Pro-Listen, Pro-Karten, FAQ, Rechtstext-Karten, Sprunglink) |
| `--leiste-schatten` | 0 4px 16px rgba(0,0,0,.08) | ~~none~~ **wieder 0 4px 16px rgba(0,0,0,.08)** (Nachtrag) | Ausnahme | Segmentleiste, „Folge uns“-Karte |
| `--segment-schatten` | 0 3px 8px rgba(0,0,0,.12), 0 3px 1px rgba(0,0,0,.04) | ~~none~~ **wieder wie vorher** (Nachtrag) | Ausnahme | gewähltes Segment |
| `.segment:hover` | background rgba(0,0,0,.05) | ~~weg~~ **wieder rgba(0,0,0,.05)** (Nachtrag) | Ausnahme | Segmente beim Zeigen |
| `theme-color` (meta) | #F4F2EE | **#F2F2F7** | `--grund` | alle sechs Seiten |
| 404: `--grund` | #F4F2EE | **#F2F2F7** | `--grund` | Grund der 404 |

**Selbst entschieden (Kevin kann widersprechen):**

1. **Band → #E5E5EA (systemGray5).** tokens.css hat unter dem Grund #F2F2F7 nur diesen Grauton. Weiß als Band hätte die
   weißen Karten im Pro-Abschnitt und die weißen Kreise im Fuß unsichtbar gemacht. Grau #5C5C5E auf #E5E5EA liegt bei
   5,3:1 (vorher 5,6:1 auf Creme).
2. **Keine Schatten mehr.** rgba(0,0,0,…) steht nicht in tokens.css, und die App trägt auf Karten keinen Schatten
   (684-Bericht, Abschnitt 4). Die Karten stehen weiß auf #F2F2F7, wie in der App; das gewählte Segment weiß auf der
   Spur #E5E5EA mit dem Rand #D1D1D6.
3. **Die Bildmarken (`img/*.svg`) bleiben**, wie die Mockups: ihre Werte (#18191A, #A6A6A6 in den Store-Abzeichen) sind
   Bilddateien, kein Code. Die Prüfung gilt für HTML, CSS und JS der sechs Seiten.

## 2 · Die Bewegung, je Stelle

Ein Muster, aus 684: der Schrift-Auftritt der App (`tlTitelAuftritt`) aus 6 px Unschärfe, 1,5 s, Kurve
`cubic-bezier(.33,1,.68,1)`, einmal beim Reinscrollen. `tokens.css` liefert die Werte (`--kurve-bewegung`,
`--dauer-auftritt` 1,5 s, `--dauer-bewegung` 0,5 s, `--auftritt-blur` 6 px) in jedem `:root`. Der Beobachter aus
`seite.js` (684) setzt beim Reinscrollen die Klasse `.da`; `.js` kommt im Kopfskript vor dem ersten Zeichnen. Die
Animation steht nur unter `prefers-reduced-motion: no-preference`; der Ruhe-Block aus 684 schaltet bei `reduce` jede
Animation und jeden Übergang ab und setzt `.auftritt` auf den Endzustand. Ohne Skript steht alles.

| Seite | Stelle | vorher | nachher |
|---|---|---|---|
| Start | Kopf: h1, Vorspann, Store-Knopf, Hinweis (`.blende`, `.blende-2`, `.blende-3`) | Einblenden von unten beim Laden, 600 ms, Kurve (0.16,1,0.3,1), gestaffelt 0/120/240 ms | `.auftritt`: aus der Unschärfe, 1,5 s, Kurve der App, ohne Staffelung, wenn es ins Bild kommt |
| Start | die zwei Mockups (`.mockups`) | Einblenden beim Laden + **Endlosschleife** `schweben` (6,0 s und 7,4 s, auf und ab) | `.auftritt` wie der Kopf; kein Schweben mehr, die Mockups stehen |
| Start | h2 „Erfassen und auswerten“, „Befunde, keine Anweisungen.“, „Was drin ist“, Wortmarke „Satzwerk Pro“, „Fragen und Antworten“ | keine | `.auftritt`, einmal beim Reinscrollen |
| Start | FAQ-Pfeil (`summary::after`) | transform 200 ms ease | transform 0,5 s, Kurve der App |
| alle fünf | Store-Knopf, Kreise, „Folge uns“-Links, Menüzeilen (`.fuellen`) | Marke läuft von links hinein (clip-path, 475 ms ease), Farbe wechselt auf Weiß, weiße Logos erscheinen | ~~nur Deckkraft 0,8~~ **wieder wie vorher, byte-gleich mit 5d382dd** (Nachtrag) |
| alle fünf | Segmente der Leiste | background-color und color 0,2 s ease, Grau beim Zeigen | ~~nur color~~ **wieder wie vorher** (Nachtrag) |
| Auswertung, Über, Datenschutz, Impressum | h1 (DE- und EN-Block) | keine | `.auftritt` |
| alle fünf | `prefers-reduced-motion: reduce` | `*{animation:none; transition:none}`, `.blende` sichtbar | Ruhe-Block aus 684: auch `::before`/`::after`, `.auftritt` auf Deckkraft 1 ohne Filter |
| 404 | – | keine | keine (die 404 hat kein Skript; nur Farben) |

Gemessen: in keiner der 120 Lagen läuft nach dem Laden eine Endlosanimation (`document.getAnimations()`,
Abschnitt 5). Bild mitten im Auftritt: `bilder/start-393-de-auftritt-0,4s.jpg`.

## 3 · Alt-Texte

**Unverändert.** In `_vorlage-684/iphone/` liegt nur `LIESMICH.md`, keine Bildschirmfotos. Die heutigen Mockups bleiben,
also beschreiben die heutigen Alt-Texte weiter das, was zu sehen ist (hell, Vorwochen-Vergleich). Der Textvergleich
meldet 0 Abweichungen, auch bei den Alt-Texten.

Vorbereitet für die neuen Mockups (nicht eingefügt; Schlüssel in `TEXTE.de`/`TEXTE.en` und im HTML der Startseite):

| Schlüssel | Deutsch | Englisch |
|---|---|---|
| alt_hinten (start) | Startbildschirm von Satzwerk im Dunkelmodus: Wochenkalender, Plan und ein beendeter Trainingstag | Satzwerk home screen in dark mode: week calendar, plan and a finished training day |
| alt_vorn (training) | Bildschirm von Satzwerk während des Trainings im Dunkelmodus: eine Übung offen, Sätze mit Gewicht, Wiederholungen und Haken | Satzwerk screen during a workout in dark mode: one exercise open, sets with weight, reps and check marks |
| alt_live | Sperrbildschirm mit der Live Activity von Satzwerk: die nächste Übung mit Gewicht und Wiederholungen | Lock screen with the Satzwerk Live Activity: the next exercise with weight and reps |
| alt_verlauf | Satzwerk Pro, Seite einer Übung im Dunkelmodus: eine Pille Stärker, Gleich oder Schwächer, darunter die zwei verglichenen Sätze und der Verlauf | Satzwerk Pro, exercise page in dark mode: a pill reading Stronger, Same or Weaker, below it the two sets being compared and the history |
| alt_muskel | Satzwerk Pro, Sätze je Muskel im Dunkelmodus: ein Balken je Muskelgruppe für die letzte Woche, mit dem Bereich von 10 bis 20 Sätzen | Satzwerk Pro, sets per muscle in dark mode: one bar per muscle group for last week, with the range of 10 to 20 sets |
| alt_koerper | Körperbereich von Satzwerk im Dunkelmodus: Ziel der Phase mit Kalorien am Tag, gemessenes und geplantes Tempo, darunter das Gewicht | Satzwerk body section in dark mode: phase goal with calories per day, measured and planned pace, weight below |

## 4 · Mockups: offen

`_vorlage-684/iphone/` enthält keine der zwölf Dateien aus `LIESMICH.md`. `img/` ist unverändert, die Seiten laden
weiter die heutigen WebP (start/training 800 × 1659, die anderen 640 × 1327, heller Modus, iPhone-Rahmen).

Vorbereitet, damit es nach dem Ablegen der Fotos ein Befehl ist:

- `_bericht-684c/mockup-rahmen/rahmen-800x1659.png` und `rahmen-640x1327.png`: der Rahmen der heutigen Mockups mit
  ausgestanztem Bildschirm (innerhalb des schwarzen Rings, gemessen: 729 × 1592 ab 35/41, Eckradius 94; 583 × 1264 ab
  28/31, Eckradius 83). Das Seitenverhältnis eines iPhone-Fotos (1179 × 2556) passt bis auf ein Promille.
- `_bericht-684c/pruefung/mockups.py`: setzt die zwölf Fotos in die Rahmen und schreibt `img/mockup-<platz>-<sprache>.webp`
  in den heutigen Maßen. Bricht ab, wenn eine Datei fehlt. Trockenlauf mit schwarzen Platzhaltern außerhalb des Repos:
  zwölf Dateien, richtige Maße, Rahmen sitzt (Bild: der dunkle Bildschirm liegt bündig im Ring).
- Danach: Alt-Texte aus Abschnitt 3 einsetzen (Startseite: HTML `alt=` und `TEXTE.de`/`TEXTE.en`), die Prüfungen aus
  Abschnitt 5 noch einmal laufen lassen.

## 5 · Prüfungen (alle in `_bericht-684c/pruefung/`, alle grün)

| Prüfung | Werkzeug | Ergebnis |
|---|---|---|
| Farben: jede Farbe in den sechs Seiten wörtlich in tokens.css | `farben.py` | GRÜN, 11 Farbstellen je Seite (404: 5). **Gegenprobe:** Kopie der Startseite mit `--grund:#F4F2EE` → ROT, Exit 1, Zeile und Wert genannt |
| Creme-Werte #F4F2EE, #EDEAE5, #DCD8D2, #E6E3DD | `grep -i` über die sechs Seiten | kein Treffer (auch nicht in Kommentaren) |
| Texte Wort für Wort gegen den Stand vorher (Textknoten außer script/style, alt, aria-label, title, meta content, `TEXTE`-Objekt DE und EN) | `texte.py VORHER NACHHER` | GRÜN: Start 1 327 Wörter, Auswertung 2 580, Über 889, Datenschutz 4 261, Impressum 650, 404 20; alle Attribute und `TEXTE` gleich |
| Wortprüfung DE und EN (kostenlos, gratis, umsonst, kein Abo, keine Cloud, keine fertigen Pläne, nur schreibend, für immer; for free, is free, free of charge, free version, free app, forever, no subscription, no cloud, write-only …) | `woerter.py` | GRÜN, Exit 0. „Free“ als Tarifname (`Free applies`) ist erlaubt und kein Treffer |
| Chromium: sechs Seiten × 375, 393, 430, 1280, 1440 × DE/EN × Bewegung an/aus = 120 Lagen: scrollWidth ≤ clientWidth, kein Element über der Kante, Sprache gesetzt, Grund rgb(242,242,247), keine Endlosschleife, jeder sichtbare `.auftritt` nach dem Durchscrollen bei Deckkraft 1 ohne Filter, keine Skriptfehler | `browser.mjs` (Playwright 1.56, Chromium 1194) | GRÜN, 120 Lagen, Tabelle in `browser-ergebnis.md` |
| Interne Links und Bilder | `browser.mjs` | 21 Adressen, alle 200, dazu die sechs EN-Mockups per curl 200; `/datenschutz/` 200 |
| Systemschriften | – | Chromium hier hat kein SF; Fraunces und Public Sans kommen aus `/fonts/` (selbst gehostet, geladen, 200). Keine Abweichung gesehen |

Lokal gedient mit `python3 -m http.server` aus der Wurzel (wie GitHub Pages: `/datenschutz/` → `datenschutz/index.html`).

## 6 · Seitengrößen (Bytes)

| Seite | vorher | nachher | Differenz |
|---|---|---|---|
| index.html | 76 600 | 77 738 | +1 138 |
| auswertung/index.html | 52 948 | 54 532 | +1 584 |
| ueber/index.html | 37 975 | 39 559 | +1 584 |
| datenschutz/index.html | 59 996 | 61 580 | +1 584 |
| impressum/index.html | 33 579 | 35 163 | +1 584 |
| 404.html | 2 123 | 2 194 | +71 |

Das Plus sind die Kommentare im `:root`, der Bewegungsblock und der Beobachter (14 Zeilen). `img/` und `fonts/` unverändert.

## 7 · Bilder (`_bericht-684c/bilder/`, 43 JPEG, 8,5 MB)

```
ganze Seite, Bewegung an, Endzustand   <seite>-393-de, <seite>-393-en, <seite>-1440-de, <seite>-1440-en   (24)
nur oben, Bewegung aus, DE             <seite>-375-de-ruhe-oben, <seite>-430-de-ruhe-oben, <seite>-1280-de-ruhe-oben   (18)
mitten im Auftritt                     start-393-de-auftritt-0,4s
```
`<seite>` = start, auswertung, ueber, datenschutz, impressum, 404.

## 8 · Alte Dateien: lädt eine Seite sie?

Geprüft per grep über die sechs Seiten und über die 21 geladenen Adressen in Chromium.

| Datei | von einer Seite geladen? |
|---|---|
| `bau.py`, `unterseiten.py`, `vorlage.html` | nein |
| `quellen/datenschutz.html`, `quellen/impressum.html` | nein |
| `datenschutz.html`, `impressum.html` (Wurzel) | nein (die Seiten verlinken `/datenschutz/` und `/impressum/`) |
| `Fraunces-VariableFont_…woff2`, `PublicSans-VariableFont_wght.woff2` (Wurzel) und dieselben in `fonts/` | nein; geladen werden `fonts/fraunces.woff2` und `fonts/publicsans.woff2` |
| `mockup-*.png` (Wurzel) und `img/mockup-*.png` | nein; geladen werden nur `img/mockup-*.webp` |
| Google Fonts (`fonts.googleapis.com`, nur Startseite) | ja, unverändert (Schrift bleibt, nicht Teil des Tickets) |

## 9 · Offen

1. **Mockups:** zwölf dunkle Bildschirmfotos nach `_vorlage-684/iphone/` (Namen in `LIESMICH.md`), dann
   `python3 _bericht-684c/pruefung/mockups.py`, Alt-Texte aus Abschnitt 3 einsetzen, Prüfungen wiederholen.
2. **Band #E5E5EA** (Abschnitt 1, Entscheidung 1): wenn Kevin das Band lieber weiß will, müssen Pro-Karten und Fußkreise
   einen Rand (`--kante`) bekommen; sonst nichts.
3. ~~`.fuell`-Spannen stehen leer im HTML~~ Erledigt durch den Nachtrag: der Fülleffekt ist zurück, die Spannen tragen ihn wieder.
4. **Chromium ohne SF Pro:** die Bilder zeigen Fraunces und Public Sans aus `fonts/`, die Systemschrift-Rückfälle greifen
   nicht. Am iPhone unverändert gegenüber heute.

---

# Nachtrag (Korrektur 684c, Kevin 22.10.2026, 09:19)

Kevin: Pillen in der Navigation, Hover und Violett der CTAs und der Instagram-/LinkedIn-Kreise fehlen; die Leiste soll so
breit sein wie die Fußzeile. Skript `pruefung/korrektur.py`, jede Ersetzung genau einmal je Seite.

## N1 · Zurück wie in 5d382dd (fünf Seiten; die 404 hat weder Leiste noch Knöpfe)

| Stelle | Stand nach 684c | jetzt |
|---|---|---|
| `.fuellen` / `.fuell` (App-Store-Knöpfe, Menüzeilen, „Folge uns“, Instagram- und LinkedIn-Kreise) | nur Deckkraft 0,8 | der Block aus 5d382dd, byte-gleich (Prüfung `fuell.py`): die Marke läuft von links hinein (clip-path, 475 ms ease), Schrift weiß, weiße Logos erscheinen; mit Zeiger bei `:hover`, sonst bei `:active` und `:focus-visible` |
| `--leiste-schatten` | none | `0 4px 16px rgba(0,0,0,.08)` |
| `--segment-schatten` | none | `0 3px 8px rgba(0,0,0,.12), 0 3px 1px rgba(0,0,0,.04)`: das gewählte Segment ist wieder die weiße Pille |
| `.segment:hover` | nur Farbe | `color:var(--tinte); background:rgba(0,0,0,.05)`, Übergang wie vorher (`background-color .2s ease, color .2s ease`) |
| `--schatten` (Karten) | none | **bleibt none** (dazu hat Kevin nichts gesagt) |
| Auftritt beim Reinscrollen | aus 684 | **bleibt** |

**Ausnahmen in der Farbprüfung** (`farben.py`, `AUSNAHMEN`, mit Namen): `rgba(0,0,0,.08)` = `--leiste-schatten`,
`rgba(0,0,0,.12)` und `rgba(0,0,0,.04)` = `--segment-schatten`, `rgba(0,0,0,.05)` = `.segment:hover`. Schatten und
Zustände, keine Creme. Sonst nichts; die Gegenprobe mit `--grund:#F4F2EE` bleibt ROT.

## N2 · Neu: die Leiste so breit wie die Fußkarte (ab 900 px)

Block `@media (min-width:900px)` im Kopf jeder der fünf Seiten: `.kopf{ padding:12px 24px }`, `.kopf-innen{ width:100%;
max-width:1072px }` (1120 minus zweimal 24 wie `.rahmen`), `.segment-marke{ margin-right:auto }`,
`.kopf-innen .leiste .store{ margin-left:auto }` (schlägt `.leiste .store{ margin-left:4px }`). Wortmarke links, App Store
rechts, die Segmente dazwischen, mittig im Zwischenraum. Unter 900 px (Handy) alles wie vorher: Kapsel so breit wie ihr
Inhalt, mittig, das Handymenü unverändert.

Gemessen in Chromium (`browser.mjs`, Spalte „Leiste / Fusskarte“), DE und EN, Bewegung an und aus:

| Breite | Leiste | Fußkarte | Abweichung |
|---|---|---|---|
| 1280 | 104–1176 | 104–1176 | 0 px |
| 1440 | 184–1256 | 184–1256 | 0 px |

Gleich auf allen fünf Seiten (die 404 hat keine Leiste). Toleranz 1 px, Exit 0.

## N3 · Prüfungen (alle grün, Stand nach der Korrektur)

| Prüfung | Ergebnis |
|---|---|
| `fuell.py`: `.fuellen`-Block, Leisten-Schatten und `.segment:hover` byte-gleich mit 5d382dd, fünf Seiten | GRÜN. **Gegenprobe:** Kopie der Startseite mit Deckkraft statt Fülleffekt → ROT, Exit 1 |
| `farben.py` (mit den vier Ausnahmen) | GRÜN, 15 Farbstellen je Seite (404: 5); Gegenprobe Creme → ROT |
| Creme-grep (#F4F2EE, #EDEAE5, #DCD8D2, #E6E3DD) | kein Treffer |
| `texte.py` gegen 5d382dd | GRÜN, alle sechs Seiten Wort für Wort gleich, Alt-Texte und `TEXTE` gleich |
| `woerter.py` | GRÜN, Exit 0 |
| `browser.mjs`: 120 Lagen, kein waagerechtes Scrollen, nichts über der Kante, keine Endlosschleife, reduced motion = Endzustand, Kanten der Leiste | GRÜN, 21 Adressen 200 |

**Bilder** (`bilder/`, 1440, echter Zeiger per Playwright `hover`):

```
hover-store-1440.jpg                   App-Store-Knopf in der Leiste beim Zeigen: violett gefüllt, Schrift weiß
hover-store-gross-1440.jpg             der große Knopf im Kopf der Startseite beim Zeigen
hover-segment-1440.jpg                 Segment „Auswertung“ beim Zeigen: grau, Schrift Tinte
gewaehltes-segment-auswertung-1440.jpg Seite Auswertung: das gewählte Segment als weiße Pille mit Schatten
hover-instagram-kreis-1440.jpg         Instagram-Kreis im Fuß beim Zeigen: violett, weißes Logo
leiste-1440.jpg, leiste-1280.jpg       die Leiste in voller Breite der Fußkarte
```
Dazu die 43 Bilder der Lagen wie vorher, neu aufgenommen (50 JPEG, 8,6 MB).

## N4 · Seitengrößen nach der Korrektur (Bytes)

| Seite | 5d382dd | nach 684c | jetzt |
|---|---|---|---|
| index.html | 76 600 | 77 738 | 78 951 |
| auswertung/index.html | 52 948 | 54 532 | 55 745 |
| ueber/index.html | 37 975 | 39 559 | 40 772 |
| datenschutz/index.html | 59 996 | 61 580 | 62 793 |
| impressum/index.html | 33 579 | 35 163 | 36 376 |
| 404.html | 2 123 | 2 194 | 2 172 |
