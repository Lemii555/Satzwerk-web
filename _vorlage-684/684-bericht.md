# Ticket 684: Website neu, ruhig, im eigenen Ordner — Bericht

**21.10.2026.** Gebaut in `website-684/`. `website-satzwerk/` ist unberührt (keine Datei jünger als die Sicherung
`backup/2026-10-21_152629_684_website_neu`, mit `find -newer` nachgesehen). Kein `src/`, kein Swift, kein git, kein Push.
Geschrieben außerhalb von `website-684/` und `doku/`: drei Website-Prüfer in `tools/` (einer neu, zwei angepasst), das
Messwerkzeug `tools/website_webkit.cjs`, fünf Zeilen in `tools/check.sh`, ein Eintrag in `WEGE.md` (Bereich 8), dazu die
Ablage am Schluss (ARCHIV, BACKLOG_FEATURES, REIHENFOLGE).

**HALT geprüft, nicht ausgelöst:** die echten Bildschirme tragen am Handy. Auf 375 ist ein Bildschirm 341 × 478 px
breit, Maßstab 0,868 gegen 393 pt (gemessen in WebKit). Eine Schrift von 17 pt steht damit mit 14,8 px da, eine von
13 pt mit 11,3 px, eine von 11 pt mit 9,5 px. Bild: [bildschirme-375-de.jpg](684-bilder/bildschirme-375-de.jpg).
Der Grund dafür: die dunkle Karte ist der Grund der App im Dunkeln (#000), der Bildschirm liegt ohne Rahmen darin
und nimmt die ganze Kartenbreite.

## 1 · Aufbau (Vorbild 4, Punkt 8; Handy zuerst)

```
Kopf mit Bild     Wortmarke, Sprache, App Store. Kopfzeile in Fraunces, Vorspann, Knopf, Hinweis.
                  Darunter das Foto (Studio am Morgen), das oben in den weißen Grund ausläuft: kein Text auf dem Bild.
Was es tut        drei Punkte: Eintragen (Frei), Progression je Übung (Pro), Körper und Ziel (Frei, Pro)
Satz für Satz     das Satz-Protokoll in einer dunklen Karte, darunter drei echte Bildschirme in dunklen Karten
Atempause         „Befunde, keine Anweisungen.“ groß und zentriert, darunter Kevins Haltungsabsatz
Frei und Pro      Frei als weiße Karte, Pro als dunkle Karte wie die Pro-Karte der App nach 679c (Verlauf,
                  Schein, Scheibe, Ring), mit der hellen Wortmarke „Satzwerk Pro“
Fragen            14 Fragen in zwei Spalten, Zeilen mit Linie statt Kästen
Fuß mit Bild      dasselbe Studio am Abend, läuft unten in Schwarz aus; darunter Claim, Seiten, große Wortmarke
```

Dateien: `index.html`, `auswertung/`, `ueber/`, `datenschutz/`, `impressum/`, `404.html`, `llms.txt`, `sitemap.xml`,
`robots.txt`, `CNAME` (die vier letzten unverändert kopiert), dazu `tokens.css`, `seite.css`, `seite.js`,
`fonts/fraunces.woff2` (Public Sans fällt weg) und `img/`. Datenschutz und Impressum: `<main>` byte-gleich mit
`website-satzwerk/` (31 306 und 5 230 Zeichen, verglichen), Kopfdaten gleich. Auswertung und Über: `<main>`
gleich bis auf den Knopf im Text (der Fülleffekt `fuellen`/`fuell` fällt weg, der Text bleibt). ld+json, Titel,
Beschreibungen, canonical, og unverändert.

**Satz-Protokoll:** Werte aus den Demodaten vom 21.10.2026 (`exported` 2026-10-21), über die Funktionen der App
gezogen, nichts gerechnet: Namen über `anzeigeName`, Zahlen über `zahlText`, das Kürzel für den Aufwärmsatz
(`warmShort`) und die RIR-Wörter (`rirNamen`) aus `texte.js`, Format „Gewicht Einheit × Wdh“ wie die Live Activity
(`laHinweis`). DE: Einheit `s-d-legs-1` (15.10.2026), BEINE · Kraftwerk Nord, 67 min, Langhantel-Kniebeuge (A 77,5 ×
10, dann 142,5 × 8, 137,5 × 8, 137,5 × 8, 135 × 8 „Versagen“) und Rumänisches Kreuzheben (125, 120, 120, 117,5 × 9,
„Versagen“). EN: `s-d-lo-a-0` (20.10.2026), LOWER A · Harbor Strength, 68 min, Barbell Back Squat und Romanian
Deadlift in lb, „Failure“ und „2 left“. Das Datum steht nicht da: die Demodaten wandern jeden Tag mit.

**Bildschirme:** `node tools/audit-vermessung.cjs --bild S8,S12,R3 --dunkel [--en]`, 393 pt, Demodaten vom
21.10.2026: Progression mit den Pillen „Gleich“ und „Stärker“, Sätze je Muskel, Körper. Geschnitten von 55 bis 605 pt
(unter den Kopfknöpfen; über der Tableiste, die in WebKit die CSS-Rückfallleiste ist und nicht die des Geräts,
FEHLER.md Nr. 39), als JPEG in `img/app-{progression,muskeln,koerper}-{de,en}.jpg`, je 85 bis 119 KB. Unten läuft
das Bild in den Grund aus. Die Mockups vom 1.10. sind nicht mitgenommen.

## 2 · Bilder (`doku/pruefung/684-bilder/`, WebKit, Bewegung reduziert = Endzustand)

```
Startseite ganz    start-375-de, start-393-de, start-393-en, start-1440-de, start-1440-en
Startseite oben    start-430-de-oben, start-1280-de-oben
Unterseiten oben   auswertung, ueber, datenschutz, impressum, gibt-es-nicht (404) je 393 und 1440, DE und EN
Bewegung           protokoll-aufbau-393-de (0,8 s nach dem Reinscrollen), protokoll-ende-393-de
Lesbarkeit         bildschirme-375-de (HALT-Probe oben)
```

Gemessen wurden alle 120 Lagen (Abschnitt 6); Bilder gibt es von einer Auswahl, damit der Ordner klein bleibt (4,3 MB).

## 3 · Neue Sätze zum Abnehmen

Alles andere ist Wortlaut aus 699 (Startseite `TEXTE`, Unterseiten `<main>`), nur neu angeordnet.

| Schlüssel | Deutsch | Englisch |
|---|---|---|
| h2_werk | Satz für Satz. | Set by set. |
| werk_vorspann | Ein Training aus den Beispieldaten der App: Gewicht und Wiederholungen je Satz, am letzten Satz der RIR. Darunter drei Bildschirme aus Satzwerk Pro mit denselben Daten. | A workout from the app’s sample data: weight and reps per set, the RIR on the last set. Below it, three Satzwerk Pro screens with the same data. |
| werk_titel | Progression · Sätze je Muskel · Körper (Titel der App) | Progression · Sets per muscle · Body |
| werk_alt 1 | Satzwerk Pro, Seite Progression im Dunkelmodus: je Übung ein Urteil wie Gleich oder Stärker, darunter die Werte, die verglichen werden | Satzwerk Pro, Progression page in dark mode: one verdict per exercise such as Same or Stronger, with the values being compared below it |
| werk_alt 2 | Satzwerk Pro, Sätze je Muskel im Dunkelmodus: ein Balken je Muskelgruppe für die letzte Woche, mit dem Bereich von 10 bis 20 Sätzen | Satzwerk Pro, sets per muscle in dark mode: one bar per muscle group for last week, with the range of 10 to 20 sets |
| werk_alt 3 | Körperbereich von Satzwerk im Dunkelmodus: Befundsätze, das Ziel der Phase mit Kalorien am Tag und das Gewicht mit kleinem Verlauf | Satzwerk body section in dark mode: findings, the phase goal with calories per day and the weight with a small chart |
| store_kurz | App Store (Knopf in der Kopfleiste) | App Store |
| store_aria | Satzwerk im App Store (Vorlesetext) | Satzwerk on the App Store |
| 404 | (Deutsch wie bisher) | This page does not exist. · The link is old or has a typo. · To the home page |

Die Atempause „Befunde, keine Anweisungen.“ ist der Satz, der bisher über Kevins Haltungsabsatz stand (`h2_haltung`),
jetzt groß und zentriert. Der Absatz darunter ist unverändert. Die Wortprüfung (ZIEL.md 3) ist über alle Dateien grün.

## 4 · Selbst entschieden

1. **Am Handy steht „EN“ in der Kopfleiste**, neben Wortmarke und App Store (Vorbild: nur diese zwei). Ohne die Sprachwahl
   oben fände ein englischer Besucher sie erst im Fuß. Kein Menü mehr: Auswertung und Über stehen am Handy im Fuß, ab 900
   px oben. „Folge uns“ ist kein Ausklappmenü mehr, sondern steht im Fuß über den zwei Kreisen (Instagrams Bedingung bleibt).
2. **Knopf in der Kopfleiste „App Store“ statt „Im App Store“**: „On the App Store“ passte auf 375 nicht neben Wortmarke
   und Sprache. Der große Knopf im Kopf und in der Pro-Karte sagt weiter „Im App Store“.
3. **Protokoll in der Systemschrift mit tabular-nums, nicht in Mono** (Entscheidung 2: sonst Systemschrift). RIR-Wort in
   der Marke (dunkel #B07CFF), weil RIR Pro ist; der Aufwärmsatz leiser.
4. **Die dunklen Karten haben den Grund der App im Dunkeln (#000)**, nicht #1C1C1E: so liegen die Bildschirme ohne
   Rahmen im Rahmen.
5. **Pro sieht aus wie die Pro-Karte der App im Dunkeln** (679c, PROMPT_ANLEITUNG „Bewegung und Pro-Grafik“). Die
   Wortmarke ist am Handy 24 px hoch, damit „Pro“ nicht auf der violetten Scheibe liegt (vorher gemessen: überlappte).
6. **Die Atempause behält Kevins Haltungsabsatz** unter dem Satz (Vorbild: nur der Satz). Der Absatz ist der einzige
   Ort, an dem „kein Urteil über eine Entlastungswoche“ und der Bandscheibensatz stehen.
7. **Drei Punkte statt vier:** Eintragen, Progression, Körper. Der Text zu „Sätze je Muskelgruppe“ fällt auf der
   Startseite weg; die Sache steht in der Pro-Liste, in Frage 11, im ld+json und als Bildschirm.
8. **Ein Muster:** der Schrift-Auftritt der App (`tlTitelAuftritt`: aus 6 px Unschärfe, 1,5 s, Kurve der App) an den
   Überschriften, einmal beim Reinscrollen. Das Protokoll baut sich Zeile für Zeile auf, je Zeile 0,5 s
   (`--auftritt-zelle`), der Versatz auf 1,5 s begrenzt (UI_SYSTEM 7.1, 685): die letzte Zeile beginnt nach 1,5 s.
   Karten, Text, Bilder stehen. Keine Linie gezeichnet, kein Ziffernrad: erlaubt, aber nicht nötig.
9. **Kein versteckter Anfangszustand ohne Bewegungswunsch:** die Animation steht nur in `prefers-reduced-motion:
   no-preference`, dazu der Ruhe-Block für `reduce`. Ohne Skript steht alles.
10. **Sprache wie bisher:** Startseite auf Deutsch, außer es ist Englisch gespeichert (eine Suchmaschine mit englischem
    Browser liest sie weiter deutsch); Unterseiten nehmen ohne Wahl die Browsersprache.
11. **Fotos ohne Alt-Text** (`alt=""`, Stimmung, kein Inhalt). theme-color #FFFFFF.
12. **Prüfer:** `website_rahmencheck.py` verlangt eine helle Wortmarke nur mit `data-auf-dunkel` (auf der dunklen
    Karte gewollt, sonst Rest des Dunkelmodus) und die Mockups nur für Ansichten, die eine Seite zeigt, dazu die neuen
    Bildschirme in beiden Sprachen; für `website-satzwerk` verlangt er dasselbe wie vorher (Gegenproben B2, B3).
    `website_namecheck.py` liest auch die CSS- und JS-Dateien (deren Kommentare sind öffentlich). Er fand „Kevin“ in
    einem HTML-Kommentar der Startseite, mein grep danach drei in CSS-Kommentaren; alle vier sind weg.

**Vorschläge, nicht gebaut** (Vorbild 4, Punkt 3): Tinte #0D1B1E statt Schwarz und Grautöne aus einer Familie gibt
es in der App nicht. Wenn Kevin das will, kommt es zuerst in `src/stil.js`; die Website folgt über `tokens.css`. Ebenso
Schatten in Tinte getönt: die App trägt auf Karten keinen Schatten (WEGE.md, Audit Phase 2), die Website auch nicht.

## 5 · Spezifikation der Fotos (für den Kauf, Vorbild Abschnitt 6)

**ÜBERHOLT 21.10.2026 (684b):** Kevin, 17:05: „ohne Foto.“ Die sechs Platzhalter sind gelöscht, die Website hat
keine Fotos mehr. Die Spezifikation bleibt als Stand stehen, falls je wieder Fotos kommen. Neuer Stand: Abschnitt 12.

```
Bild    Motiv                                                Zuschnitt   Datei (fester Name, einfach ersetzen)       Pixel
Kopf    Studio am Morgen, leer, Fensterlicht, Stange oder    Desktop     img/foto-kopf-desktop.jpg  ab 1024 px      2560 x 1440 (16:9)
        Hantel am Boden                                      Tablet      img/foto-kopf-tablet.jpg   640 bis 1023    1600 x 1600 (1:1)
                                                             Handy       img/foto-kopf-handy.jpg    unter 640       1170 x 2080 (9:16)
Fuß     dasselbe Studio, dieselbe Serie am Abend,            Desktop     img/foto-fuss-desktop.jpg                  2560 x 1100 (21:9)
        gedämpftes Licht, Lichter an                         Tablet      img/foto-fuss-tablet.jpg                   1600 x 800  (2:1)
                                                             Handy       img/foto-fuss-handy.jpg                    1170 x 780  (3:2)
```

- **Bildaufbau Kopf:** das Bild steht als Band unter dem Text (Handy mindestens 360 px oder 56 % der Fensterhöhe, Tablet
  bis 620 px, Desktop bis 660 px hoch), die oberen 40 % laufen in Weiß aus. Also oben Ruhe (Wand, Fenster, Decke), das
  Motiv in der unteren Hälfte; das Bild hängt unten (`object-position` 50 % 100 %). Am Handy hochkant, Motiv unten.
- **Bildaufbau Fuß:** ein Band (240 bis 560 px hoch), das Bild läuft unten in Schwarz aus; Motiv in der Mitte, Mitte
  bei 60 % der Höhe.
- **Eine Serie, ein Fotograf:** sonst passt das Licht zwischen Morgen und Abend nicht (der wichtigste Punkt).
- **Auflösung des Originals:** mindestens 2080 px in der kurzen Seite, damit der Hochkant-Zuschnitt 1170 × 2080 aus einem
  Querformat geht (bei 3:2 also mindestens 3120 × 2080); mehr ist besser. Volle Auflösung kaufen, Luft um das Motiv.
- **Datei:** JPEG, sRGB, Qualität um 75. Richtwert: Desktop bis 450 KB, Tablet und Handy bis 300 KB, Fuß kleiner.
- **Inhalt:** keine Gesichter oder abgewandt, kein freier Oberkörper, kein Lächeln in die Kamera, keine bunten Geräte,
  keine fremden Marken. Gedämpfte Farben, natürliches Licht. FOTO_BRIEFING.md: kein Supplement-Katalog.
- **Lizenz:** Standardlizenz für Websites; „nur redaktionell“ (editorial use only) ausschließen; bei erkennbaren
  Personen Modellfreigabe. KI-Bilder ausschließen (Adobe Stock: Filter für generative KI je Suche setzen).
- **Einsetzen:** die sechs Dateien ersetzen, sonst nichts. Andere Maße schaden dem Layout nicht (die Flächen
  schneiden mit `object-fit: cover`), nur der Ausschnitt ändert sich. Danach `node tools/website_webkit.cjs
  website-684 --bilder doku/pruefung/684-bilder` und die Bilder ansehen.

## 6 · Prüfungen, je mit Exit-Code (Mac, node 24)

```
python3 tools/website_rahmencheck.py website-684        Exit 0   (website-satzwerk: Exit 0)
python3 tools/website_storeabgleich.py website-684      Exit 0   (website-satzwerk: Exit 0)
python3 tools/website_namecheck.py website-684          Exit 0   (website-satzwerk: Exit 0)
python3 tools/website_regelcheck.py website-684         Exit 0   NEU: Wörter ZIEL.md 3 über ALLE Dateien (html, txt, xml,
                                                                 css, js), keine Schleife, Ruhe-Block, Rechtslinks,
                                                                 nur eigene Quellen, nur Farben aus stil.js, Fraunces
                                                                 nur an .kopfzeile, HTML = TEXTE.de, Kurve = stil.js
node tools/website_webkit.cjs website-684              Exit 0   130 Lagen: 6 Seiten (mit 404) x 375/393/430/1280/1440
                                                                 x DE/EN x reduziert/bewegt; 0 Funde: kein waagerechtes
                                                                 Scrollen, nichts über der Kante, nichts abgeschnitten,
                                                                 kein Text ohne Rand, Endzustand im ersten Bild (reduziert)
                                                                 bzw. nach dem Auftritt (bewegt), Sprache, keine Fehler,
                                                                 kein fremder Server, Fraunces nur an der Kopfzeile;
                                                                 dazu 5 Seiten x 393/1440 per Doppelklick (file://):
                                                                 Stylesheets geladen, Skript gelaufen, Bilder da
node tools/totcheck.cjs                                 Exit 0
node tools/zitatcheck.cjs                               Exit 0
./tools/check.sh --schnell                              Exit 0   191 Prüfer, 1 ausgelassen ohne Bau
Volle Kette                                             offen, Kevin
```

**Gegenproben an einer Kopie im Scratch, Nullprobe zuerst (5 von 5 grün), dann 22 Mutanten, alle ROT:**

```
 1  „Kostenlos.“ im Hinweis (HTML und TEXTE)              regelcheck  verbotenes Wort »Kostenlos«          [Ticket]
 2  .punkt mit animation … infinite                       regelcheck  eine Endlosschleife                  [Ticket]
 2b setInterval in seite.js                                regelcheck  Bewegung per Skript in Schleife
 3  Ruhe-Block gelöscht                                    regelcheck  kein Block prefers-reduced-motion     [Ticket]
 3b Animation außerhalb von no-preference                  regelcheck  animiert außerhalb von …
 3c Ruhe-Block weg UND Auftritt für alle                   webkit      im ersten Bild nicht im Endzustand
 4  Link auf /datenschutz/ auf „Über uns“ gelöscht         regelcheck  kein Link auf /datenschutz/         [Ticket]
 5  color:#123456                                          regelcheck  steht nicht in src/stil.js
 6  Fraunces am Claim                                      regelcheck und webkit
 7  <script src="https://example.com/…"> im Impressum      regelcheck  laedt von einem fremden Server
 8  „Satzwerk erfasst gern“ nur im HTML                    regelcheck  steht im HTML anders als in TEXTE.de
 9  --kurve-bewegung in tokens.css verstellt               regelcheck  … src/stil.js sagt cubic-bezier(.33, 1, .68, 1)
10  transition: color .2s ease                             regelcheck  ohne die Kurve der App
11  perspective(900px) rotateY(-12deg) am Bildschirm       regelcheck  schräg gestellt
12  helle Wortmarke ohne data-auf-dunkel                   rahmencheck Rest gefunden: logo-hell.svg
13  img/app-koerper-en.jpg gelöscht                        rahmencheck app-koerper-en.jpg fehlt
14  „Kevin“ in einem Kommentar von seite.css               namecheck   seite.css Zeile 1
15  .drei min-width 520px                                  webkit      waagerecht scrollbar, 537 bei 375
16  404 mit padding:72px 0 (mein Fehler vor dem Fix)        webkit      Text ohne Rand
17  img/foto-fuss-handy.jpg gelöscht                       webkit      404
18  Pfade ab der Wurzel wie vor Kevins Fund                webkit      per Doppelklick: Stylesheet nicht geladen
```

3c war im ersten Anlauf grün: die Mutation (`.auftritt{opacity:0}` außerhalb des Bewegungsblocks) hob der Ruhe-Block
wieder auf, sie verließ den geschützten Fall nicht (FEHLER.md Nr. 30). Neu gefasst, dann rot.

**Gegenproben B (war die Änderung nötig?):** alter Rahmenprüfer auf website-684 Exit 1 (18 Funde: helle Wortmarke,
zwölf Mockups); neuer Rahmenprüfer auf einer Kopie von website-satzwerk ohne `mockup-live-en.webp` Exit 1 und mit einer
hellen Wortmarke ohne Kennung Exit 1 (er verlangt dort, was er vorher verlangte); alter Namensprüfer mit „Kevin“ in
seite.css Exit 0 (deshalb die Erweiterung).

Gefunden beim Ansehen, nicht vom Prüfer: die 404 hatte keinen Seitenrand (`.nichtda` setzte `padding:72px 0` nach
`.rahmen`), und „Pro“ der Wortmarke lag am Handy auf der violetten Scheibe. Beide behoben; für das erste misst
`website_webkit.cjs` seitdem „Text ohne Rand“ (Gegenprobe 16).

## 7 · Seitengrößen (WebKit, übertragene Bytes, mit den Platzhaltern)

**Stand vor 684b.** Ohne Foto: Abschnitt 12.

```
Seite           Datei   393: erster Aufruf / ganz gescrollt   1440: erster Aufruf / ganz gescrollt
/               55 KB        260 KB / 660 KB                       308 KB / 793 KB
/auswertung/    29 KB         73 KB / 149 KB                        73 KB / 234 KB
/ueber/         15 KB         58 KB / 135 KB                        58 KB / 219 KB
/datenschutz/   37 KB         81 KB / 157 KB                        81 KB / 242 KB
/impressum/     11 KB         55 KB / 131 KB                        55 KB / 216 KB
404              7 KB        127 KB                                212 KB
Gemeinsam: seite.css 21 KB, tokens.css 4 KB, seite.js 3 KB, fraunces.woff2 41 KB (nur Startseite)
Zum Vergleich website-satzwerk, Startseite: Datei 75 KB, 654 KB (393) / 888 KB (1440) beim ersten Aufruf, 906 KB ganz
```

Mit den gekauften Fotos wird die Startseite schwerer (Richtwerte oben: Kopf bis 450 KB, Fuß bis 300 KB). Das Kopfbild
lädt sofort, das Fußbild und die drei Bildschirme erst beim Scrollen.

## 8 · Tausch: wie website-684 zu website-satzwerk wird (erst auf Kevins Ja)

~~**Nicht mit Platzhaltern live gehen.** Auf den Platzhaltern steht „PLATZHALTER“. Erst die sechs Fotos einsetzen
(Abschnitt 5), dann:~~
**Überholt mit 684b (21.10.2026):** es gibt keine Platzhalter mehr, der Schritt „Fotos einsetzen“ entfällt. Der Tausch
wartet nur noch auf Kevins Abnahme der neuen Sätze (Abschnitt 3) und sein Ja. Die Schritte:

1. Sicherung (der Tausch fasst `website-satzwerk` an, und das steht in `PFADE`):

       cd "/Users/kevinschropp/Desktop/Satzwerk App" && ./backup.sh "684 tausch"

2. Ordner tauschen (der alte Stand liegt danach in `website-satzwerk-699` und in git):

       cd "/Users/kevinschropp/Desktop/Satzwerk App" && mv website-satzwerk website-satzwerk-699 && mv website-684 website-satzwerk

3. Claude Code stellt `tools/check.sh` um (`website_regelcheck.py` auf `website-satzwerk`, die vier `website-684`-Zeilen
   raus), dazu den Eintrag in WEGE.md Bereich 8, `lastmod` in `sitemap.xml` auf den Tag des Tauschs, und lässt
   rahmen-, storeabgleich-, name- und regelcheck sowie `node tools/website_webkit.cjs website-satzwerk` laufen.
4. Hochladen: der GANZE Inhalt von `website-satzwerk/` wird ersetzt, auch gelöschte Dateien müssen online verschwinden
   (`img/mockup-*`, `fonts/publicsans.woff2`, die `-dunkel.png`). Der Weg dahin steht in keiner aktuellen Datei
   (Bericht 699, Abschnitt 7); deshalb kein Befehl von mir.
5. Danach auf satzwerk.app: Startseite DE und EN, `/datenschutz/` (verlinkt die App), eine falsche Adresse (404).
6. `website-satzwerk-699` löschen, wenn der Stand committet ist.

## 9 · Worauf Kevin schaut (ohne Tausch, auf dem Mac)

Eine einzelne Seite geht per Doppelklick auf `website-684/index.html` (seit dem Nachtrag unten). Die Links zwischen
den Seiten (`/ueber/` usw.) und die 404 brauchen den Server. Im Terminal (hält an, bis Ctrl+C):

    cd "/Users/kevinschropp/Desktop/Satzwerk App/website-684" && python3 -m http.server 8684

Dann in Safari `http://localhost:8684/`. Am iPhone im selben WLAN `http://<Name des Macs>.local:8684/`.
Die Liste mit Ergebnisspalte steht in `doku/pruefung/684-geraet.md`.

## 10 · Nicht geprüft, offen

- Echte Fotos (Platzhalter), echtes Safari am iPhone (nur WebKit über Playwright), VoiceOver, Tastaturbedienung im
  Ganzen (Fokusrahmen gesetzt, nicht durchgetabbt), Glas der Kopfleiste (Playwright-WebKit zeichnet den Weichzeichner
  nicht; über den dunklen Karten wird die Leiste grau, „EN“ hat dort gerechnet 4,6:1 gegen Schwarz unter 72 % Weiß).
- Volle Kette (Kevin). Die App ist nicht angefasst; der Schnellgang ist grün.
- **Nebenbei gesehen, nachgezogen auf Kevins Ja (21.10.2026):** `backup.sh` sicherte `website-684` nicht. Jetzt steht
  es in `PFADE`. Probe: `bash -n` ok, die Sicherung `2026-10-21_163507_684_probe_pfade` enthält `website-684`
  vollständig (`diff -rq` ohne Unterschied), die Sicherung davor mit dem alten Skript enthielt es nicht. Nach dem Tausch
  wird der Eintrag still übersprungen. `doku/` sichert `backup.sh` weiter nicht.

## 11 · Nachtrag 21.10.2026: Kevins Fund, die Seite ohne Stil

**Kevin, mit Bildschirmfoto:** „da ist ein fehler drin“. Auf dem Bild: Links ohne Gestaltung, die Wortmarke als
Platzhalterkasten, ein riesiger schwarzer Pfeil.

**Nachgestellt, bevor ich etwas geändert habe:** `website-684/index.html` per `file://` in WebKit geöffnet ergab genau
dieses Bild: kein Stylesheet geladen, `seite.js` nicht gelaufen, jedes Bild mit Breite 0. **Ursache:** alle Dateien der
Website standen ab der Wurzel (`/seite.css`, `/img/…`). Über einen Server stimmt das, per Doppelklick zeigt `/` auf die
Wurzel der Festplatte. Der Pfeil ist das SVG im Knopf, das ohne Stil die ganze Breite nimmt. Meine Messung lief nur über
einen Server und konnte das nicht sehen.

**Behoben:** Stylesheets, Skript, Schrift und Bilder stehen relativ (`seite.css`, `../seite.css`, `img/…`), die Schrift
relativ zu `seite.css`; die Bildschirme wechseln die Sprache nur noch an der Endung. Die Links zwischen den Seiten bleiben
ab der Wurzel (`/ueber/` usw., die Prüfer verlangen sie so), ebenso die ganze 404 (der Server liefert sie unter jeder
Adresse aus). Die SVGs tragen `width` und `height`, damit ein Pfeil ohne Stil 18 px bleibt. **Riegel:**
`website_webkit.cjs` öffnet jede Seite zusätzlich per `file://` (Gegenprobe 18 mit den alten Pfaden: rot).

**Dabei gesehen und mit behoben:** in einem niedrigen Fenster (1000 × 540) lag der Vorspann auf dem Kopfbild. Das Foto
beginnt jetzt unter dem Text (Abschnitt 5 nachgezogen). Und an der Oberkante des Fotos blieb auf 1440 eine Bildzeile
sichtbar (#FAFAFC zwischen Weiß, an den Pixeln gemessen); die Blende reicht jetzt 1 px darüber, nachgemessen nur Weiß.

**Danach gelaufen, Exit 0:** die vier Website-Prüfer auf website-684 (drei davon auch auf website-satzwerk), WebKit 130
Lagen 0 Funde, Gegenproben 22 von 22 rot und 5 Nullproben grün, totcheck, zitatcheck, Schnellgang 191. Datenschutz und
Impressum weiter byte-gleich. Bilder in `684-bilder/` neu aufgenommen.

## 12 · Nachtrag 684b, 21.10.2026: ohne Foto

**Kevin, 17:05:** „ohne Foto.“ Die Klammer bleibt als Ton, oben hell, unten dunkel; im Kopf die Bildmarke groß; das
Produkt ist das Bild (BACKLOG_FEATURES.md 684). Gesetzt von Chat-Claude: kein neuer Text, kein neuer Farbwert, die
Bewegung bleibt. Gebaut nur in `website-684/` und im Rahmenprüfer; `website-satzwerk/` ist unberührt (`find -newer`
gegen die Sicherung: 0 Dateien).

```
Kopf      heller Grund --grund (#F2F2F7, tokens.css). Kopfzeile, Vorspann, Knopf und Hinweis wie gebaut. Die Bildmarke
          (img/bildmarke.svg, dieselbe wie das Seitensymbol) ist die einzige Grafik: am Handy unter dem Text (189 px
          auf 393), ab 900 px rechts daneben (360 px auf 1440). Unten 72 bzw. 120 px Luft wie jeder Abschnitt.
Fuß       dunkler Abschnitt --dunkel-grund (#000, die Fläche der dunklen Karten), darin „Handwerk am eigenen Körper.“,
          „Folge uns“, die Seiten und die große Wortmarke wie bisher. Oben 72 bzw. 120 px statt des Bildes.
Raus      die sechs img/foto-*.jpg; jedes <picture> mit seinen <source srcset> (Startseite Kopf und Fuß, der Fuß von
          Auswertung, Über uns, Datenschutz, Impressum und 404); fetchpriority="high" am Kopfbild (das war das
          Vorladen des Fotos); die Regeln .held-bild und .fuss-bild. Vorgeladen wird nur noch die Schrift Fraunces.
```

**Selbst entschieden, Kevin kann widersprechen:**

1. **„Heller Grund“ ist --grund (#F2F2F7), nicht Weiß.** So wechseln die Abschnitte grau, weiß, grau, weiß, grau, weiß,
   schwarz; mit Weiß ginge der Kopf ohne Kante in „Erfassen und auswerten“ über. Folge: die Kopfleiste (Glas über dem
   weißen Seitengrund) steht als weißer Streifen über dem grauen Kopf, Bild `684b-erster-bildschirm-393-de.jpg`. Soll
   das Grau bis unter die Leiste reichen, ist das eine Regel.
2. **„Die dunkle Fläche der App“ ist --dunkel-grund (#000)**, wie die dunklen Karten und der Fuß bisher (Abschnitt 4,
   Punkt 4). #2C2C2E bleibt den zwei Kreisen.
3. **Die Bildmarke hat `alt=""`:** sie ist Schmuck, der Name steht in der Leiste. Kein neuer Text.
4. **Der Rahmenprüfer liest jetzt auch `srcset`, `<link rel="preload">` und die 404.** Vorher sah er nur `<img src>`:
   ein Verweis auf ein gelöschtes Foto in einem `<source>` oder im Vorladen blieb grün (Gegenproben unten).

**Seitengröße** (WebKit, übertragene Bytes, Startseite DE, dieselbe Messung wie Abschnitt 7; vorher ist die Sicherung
`2026-10-21_195304_684b_und_f2-019`, sie trifft die Zahlen aus Abschnitt 7 genau):

```
                  393: erster Aufruf / ganz gescrollt       1440: erster Aufruf / ganz gescrollt
vorher (684)      260 KB / 660 KB, 15 Anfragen              308 KB / 793 KB, 15 Anfragen
nachher (684b)    139 KB / 483 KB, 14 Anfragen              139 KB / 483 KB, 14 Anfragen
Dateien           index.html 56 195 -> 55 648 Byte, seite.css 21 682 -> 21 067, img/ 1 404 -> 688 KB
```

Vorher ging je Breite eine Anfrage an `img/foto-kopf-*` und eine an `img/foto-fuss-*`. Nachher: keine Anfrage auf
`img/foto-*`, keine mit Status 400 oder höher.

**Prüfungen (Mac, node 24), je mit Exit-Code:**

```
python3 tools/website_rahmencheck.py website-684        Exit 0   (website-satzwerk: Exit 0)
python3 tools/website_storeabgleich.py website-684      Exit 0   (website-satzwerk: Exit 0)
python3 tools/website_namecheck.py website-684          Exit 0   (website-satzwerk: Exit 0)
python3 tools/website_regelcheck.py website-684         Exit 0
node tools/website_webkit.cjs website-684 --bilder doku/pruefung/684-bilder
                                                        Exit 0   130 Lagen, 0 Funde (alle sechs Seiten, 375 bis 1440,
                                                                 DE/EN, reduziert/bewegt, dazu per Doppelklick)
Startseite 393 und 1440 DE, Skript im Scratch           0 Funde: Kopf, Bildmarke (geladen), Fuß, Claim und Wortmarke
                                                                 im Fenster, nichts über der Kante, kein waagerechtes
                                                                 Scrollen, keine Anfrage auf img/foto-*, keine 404
node tools/totcheck.cjs, node tools/zitatcheck.cjs      Exit 0
./tools/check.sh --schnell                              Exit 0   191 Prüfer, 1 ausgelassen ohne Bau
Volle Kette                                             offen, Kevin
```

**Gegenproben am Rahmenprüfer** (Kopie von website-684 im Scratch, je frisch, eine Änderung; „alt“ ist der Prüfer aus
der Sicherung):

```
N   Nullprobe                                         neu Exit 0   alt Exit 0
G1  <source srcset> auf foto-kopf-desktop zurück       neu Exit 1   alt Exit 0   „Bild fehlt: img/foto-kopf-desktop.jpg“
G2  <img> auf foto-fuss-handy im Fuß zurück            neu Exit 1   alt Exit 1
G3  Vorladen von foto-kopf-handy zurück                neu Exit 1   alt Exit 0
G4  404: <img> auf foto-fuss-handy zurück              neu Exit 1   alt Exit 0
```

Alle vier Platzhalter-Verweise machen den Prüfer ROT; G1, G3 und G4 sah der alte nicht, die Erweiterung war also nötig.

**Bilder** (`684-bilder/`): neu `684b-kopf-393-de`, `684b-kopf-1440-de`, `684b-fuss-393-de`, `684b-fuss-1440-de`,
`684b-erster-bildschirm-393-de`, `684b-erster-bildschirm-1440-de`. Die Bilder aus Abschnitt 2 sind mit
`website_webkit.cjs` neu aufgenommen und zeigen den Stand ohne Foto; der Stand mit Platzhaltern liegt in git und in der
Sicherung. Unverändert geblieben: `bildschirme-375-de`, `protokoll-aufbau-393-de`, `protokoll-ende-393-de`.

**Überholt:** Abschnitt 5 (die Spezifikation), in Abschnitt 1 „Kopf mit Bild“ und „Fuß mit Bild“, in Abschnitt 8 der
Schritt „Fotos einsetzen“. **Nicht geprüft:** echtes Safari am iPhone, das Glas der Kopfleiste (Playwright zeichnet den
Weichzeichner nicht). Im selben Lauf: F2-019 (umbruchmessung), Ergebnis in `audit-release-2/FRAGEN.md`.
