# Ticket 699: Website gegen den Endstand 2.3, schmal — Bericht

**21.10.2026.** Geschrieben nur in `website-satzwerk/` und `doku/` (dazu die vier Ablagedateien am Schluss).
Kein `src/`, kein Swift, kein git, kein Push. Sicherung: `backup/2026-10-21_102319_699_website_schmal` (mit
`website-satzwerk`, seit 666 in PFADE); REIHENFOLGE.md, BACKLOG_FEATURES.md und ARCHIV.md zusätzlich im Scratch
kopiert, weil backup.sh REIHENFOLGE.md und doku/ nicht sichert (700, „Nebenbei gesehen“).

## 1 · Gemessene Fakten (aufgerufen, nicht aus dem ARCHIV)

Skript `fakten.mjs` im Scratch dieser Sitzung (importiert die Module aus `src/`, node 24, Exit 0).

```
Übungen                    223          LIB.length (src/bibliothek.js)
Vorlagen                   12           BASISPLAENE: Studio 2 Einstieg / 4 Fortgeschritten, Hanteln 2/2, ohne Geräte 1/1
Testmonat                  30 Tage      TEST_TAGE; Bestand bis 2027-10-31 (BESTAND_BIS), PAYWALL_BUILD 29
iCloud-Schalter            ohne Schlüssel AUS: schalterAn(null) false, nur "1" an (700)
iCloud-Frage               frageOffen(null, false) true; startSchritt neu → "einwilligung" (bis zum Ja keine Datei),
                           ohne iCloud → "fehlt" (keine Frage), leer + Sicherung → "frage" (Zurückholen)
                           Texte: icloudJaTitel „Sicherung in iCloud?“, Knöpfe „Sichern“ / „Nicht jetzt“ (texte.js 1051)
iCloud-Datei OHNE          AM_GERAET: :health, :health.trainings/.gewicht/.kfa/.umgewandelt, :healthlesen, :healthkcal,
                           :la, :icloud, :icloud.gefragt; dazu Gewichte mit src "health" (fuerIcloud)
Dateien                    7 (Montag.json … Sonntag.json)
Urteil je Übung            urteilVon: steigt → staerker, gleich → gleich, faellt → schwaecher, offen → kein Urteil
Fenster                    ERSTE_WOCHEN 2, FENSTER_WOCHEN 4: 2 und 3 Trainingswochen fenster 1, ab 4 fenster 2, 1 Woche null
R2                         105 × 10 gegen 107,5 × 9 ohne RIR → „gleich“ (kraftRichtung)
R3 direkt                  230 × 13 → 230 × 14: stärker; BW 15 = BW 15: gleich; 100 × 14 → 90 × 16: kein Urteil
Kraftgrenze                KRAFT_GRENZE 12 (Wdh + gemessener RIR), 100 × 10 ohne RIR = 133,3
Kurve                      MAXPUNKTE 35 Trainingswochen (kurvenReihe, progression.jsx)
Intensität                 RIR_LIMIT 0, 1, 2; RIR davor höchstens RIR_DECKEL 4
RIR-Eingabe                RIR_WERTE 0 bis 3 („Versagen“, „noch 1“ … „noch 3“)
Umfänge / Muskeln / Phasen waist chest hip arm leg / 8 Gruppen, Band 10–20 / cut maintain gain
Health lesen               Gewicht: alle Proben (P3-001); Kalorien: leseAb = Montag vor 12 Wochen oder Phasenbeginn,
                           falls früher (kalorientage.js 153); nur im Zustand, nie gespeichert (healthkalorien.js Kopf)
Feedback-Mail              mailto info@satzwerk.app, Betreff mit Version, Zeile: App, Sprache, Einheiten, Darstellung,
                           Leiste, ggf. Maße (TrainingsLog.jsx 2996–3012); nichts aus den Daten
Version                    APP_VERSION und MARKETING_VERSION 2.2, Build 33; die Seiten nennen 2.3 (wie 658)
```

## 2 · Abweichungsliste (VOR dem Ändern)

Zeilen wie vor dem Ändern, aus dem Trockenlauf von `aendern.py` (64 Ersetzungen, 2 Blöcke, jede mit
geprüfter Trefferzahl). Startseite: DE steht im HTML, in `TEXTE.de` und bei den FAQ im ld+json; EN nur in
`TEXTE.en`. Die Seiten Auswertung, Über und Datenschutz tragen DE- und EN-Block im HTML.

| Seite | Stelle (Zeile) | vorher | nachher | Quelle |
|---|---|---|---|---|
| Start | Hinweis 563, 800 / EN 967 | Daten auf dem iPhone und in deiner eigenen iCloud | … und, wenn du willst, in deiner eigenen iCloud | schalterAn, startSchritt (700) |
| Start | Haltung 615, 803 / EN 970 | kein „nimm mehr Gewicht“, kein „Deload empfohlen“ | keine Gewichtsvorgabe, kein Urteil über eine Entlastungswoche | ZIEL.md 3 (Wörter) |
| Start | Progression 594, 934 / EN 1101 | Wdh-Ziel, dazu Kraft (geschätzt) über vier Trainingswochen und Verlauf | je Übung ein Urteil stärker/gleich/schwächer ab der zweiten Trainingswoche, dazu das Wdh-Ziel | urteil.js, ERSTE_WOCHEN 2 (696) |
| Start | Pro-Liste 641, 820 / EN 987 | Wiederholungsziel und Kraft (geschätzt) | stärker, gleich oder schwächer, dazu das Wiederholungsziel | 696 |
| Start | Pro-Absatz 663, 833 / EN 1000 | wie sich die Kraft … über vier Trainingswochen entwickelt; EN „is free“ | ob du stärker, gleich stark oder schwächer bist; EN „needs no Pro“ | 696; F2-016 |
| Start | Karte 1 EN 1003 | 30 days as a gift | 30 days on us | F2-016 (App, Store 659) |
| Start | Karte 3 EN 1012 | part of the free version | part of Free | F2-016, Tarifname |
| Start | FAQ 3 Frage EN 1028 | What is free and what is Pro? | What is in Free, what is in Pro? | F2-016 |
| Start | FAQ 6 EN 1041 | Pro as a gift until … the free version applies | Pro is on us until … Free applies | proBText (App) |
| Start | FAQ 8 132, 710, 882 / EN 1049 | iCloud-Sicherung ist ab Werk an, lässt sich ausschalten | Satzwerk fragt einmal; ohne Ja keine Datei; im Profil umschalten | schalterAn, frageOffen (700) |
| Start | FAQ 9 EN 1053 | each at Beginner and Advanced level | each as an entry-level and an advanced version | ZIEL.md 3 („für Anfänger“), Selbst entschieden 4 |
| Start | Körper EN 1109 | weight … is free | is part of Free | F2-016 |
| Start | ld+json 48 | Kraft (geschätzt), zwei Trainingswochen gegen zwei davor | Ein Urteil je Übung, ab der zweiten Trainingswoche | 696 R1 |
| Auswertung | ld+json 27 | dateModified 2026-10-17 | 2026-10-21 | – |
| Auswertung | Stand 454 / 625 | 17. Oktober / October 17 | 21. Oktober / October 21 | – |
| Auswertung | Daten 471 / 642 | ab Werk an, abschaltbar / on by default | wenn du es erlaubst; Satzwerk fragt einmal | 700 |
| Auswertung | Modell EN 643 | Logging is free … 30 days of Pro as a gift | Logging needs no Pro … are on us | F2-016 |
| Auswertung | Progression 491–497 / 662–667 | zwei Trainingswochen gegen zwei davor, über 12 Wdh schätzt die App nicht | Urteil je Übung; R1 Fenster (2–3 Wochen jüngste gegen davor, ab 4 zwei gegen zwei); R2 feste Ordnung ohne RIR an beiden; R3 über 12 Wdh und reines Körpergewicht direkt; Kurve 35 Wochen | wochenvergleich.js, kraft.js, direktvergleich.js |
| Auswertung | Nicht rechnet 552 / 719 | Kein „mehr Gewicht“ / No “add weight” | Keine Gewichtsvorgabe / No weight target | ZIEL.md 3 |
| Auswertung | Testmonat EN 756 | You get 30 days of Pro as a gift | 30 days of Pro are on us | F2-016 |
| Über | ld+json 26, Stand 389 / 456 | 17.10. | 21.10. | – |
| Über | meta 7, og 12 | „, Wie …“, „Satzwerk wird“ | „. Wie …“, „Satzwerk wurde“ | Umbenennung 22.8. (Tippfehler, Zeitform) |
| Über | Liste 423 / 490 | Daten auf deinem iPhone und in deiner eigenen iCloud | …und, wenn du willst, in deiner eigenen iCloud | 700 |
| Über | Modell EN 509 | Logging is free | Logging needs no Pro | F2-016 |
| Datenschutz | Stand 329 / 638 | 17. Oktober | 21. Oktober | – |
| Datenschutz | 360 / 669 | keine Analysewerkzeuge, keine Tracking-Bibliotheken | dazu: keine Werkzeuge für Absturzberichte | PHASE3 4 (kein Sentry, Crashlytics, MetricKit …) |
| Datenschutz | 365 / 674 | Daten verlassen das Gerät nur auf zwei Wegen | Satzwerk selbst bringt sie auf zwei Wegen vom Gerät (iCloud nur mit Ja, Export); dazu das iOS-Gerätebackup | P3-004, Apple File System Programming Guide (Library im Backup) |
| Datenschutz | 372 / 681 | Daten und Pläne als Text ausgeben | Sicherungsdatei und CSV, Sicherungsdatei einlesen, Pläne als Text | PHASE3 4 Export |
| Datenschutz | iCloud 377–405 / 686–713 | „Die Sicherung ist ab Werk eingeschaltet.“ | „Ohne dein Ja legt Satzwerk keine Datei an.“ Frage einmal (neu nach dem Namen, Update nach „Was ist neu“), „Nicht jetzt“ = aus; Inhalt mit Größe und ohne die Antwort; Zurückholen schaltet an, Nicht-Zurückholen lässt aus; Rechtsgrundlage als Vorschlag | icloudsicherung.js Kopf 2, 3; AM_GERAET; texte.js 1049–1052 |
| Datenschutz | Health lesen 416 / 724 | Gewicht; Kalorien als Tagessumme | auch frühere Wiegungen; Kalorien rund drei Monate oder seit Phasenbeginn | P3-001, leseAb |
| Datenschutz | Health 423–426 / 731–734 | Apple Health ist ein lokaler Speicher; nichts verlässt das Gerät außer Gewicht im Export | Satzwerk tauscht auf dem Gerät aus, was Apple Health tut, regelt Apple; Gewicht in Sicherungsdatei, CSV und Gerätebackup | P3-004 (CSV aufgerufen) |
| Datenschutz | nach 455 / 762 | Feedback-Mail fehlt | neuer Abschnitt „Feedback aus der App“ | TrainingsLog.jsx 2996–3012 |
| Datenschutz | Pro 479 / 785 | liegen nur auf diesem Gerät / stay on this device only | sind an dieses Gerät gebunden / are tied to this device | kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly (Aussage stimmte, Wortlaut nach ZIEL.md 3-Muster) |
| llms.txt | 3 / 5 | Kraft über vier Trainingswochen; Daten in der eigenen iCloud; Logging is free; as a gift | ein Urteil je Übung; iCloud, wenn der Nutzer zustimmt; needs no Pro; on us | 696, 700, F2-016 |
| llms.txt | 21 | Progression zwei gegen zwei | Urteil, R1, R3 | 696 |
| llms.txt | 23 | iCloud ab Werk an, abschaltbar | nur mit Zustimmung, Satzwerk fragt einmal | 700 |
| sitemap.xml | 3, 4, 5, 7 | lastmod 2026-10-17 | 2026-10-21 | – |

**Nicht geändert, weil richtig (gemessen):** 223 Übungen und zwölf Vorlagen (alle Fassungen), Testmonat ab dem
ersten abgeschlossenen Training, Bestand bis 31.10.2027, RIR 0 bis 3, harte Sätze RIR 0 bis 2, Band 10 bis 20,
acht Muskelgruppen, fünf Umfänge, drei Phasen, drei Messarten, Kurve 35 Trainingswochen, Wochenraster rund ein
halbes Jahr (25 Wochen), Hell/Dunkel/Automatisch (681 ändert nur den Start, die Wahl bleibt), Health schreibend
und lesend, Studios in Pro (663 verschiebt nur die Seite), Live Activity, Bewertungsdialog, StoreKit-Absätze,
Kündigen, Konto. Die Alt-Texte der Startseitenbilder bleiben (sie beschreiben die Bilder, Abschnitt 5).
„Satzwerk liest keine Exporte aus anderen Apps wie Hevy oder Strong“ stimmt (planlesen.js liest Plantext, keine
Trainingsdaten).

**Nicht aufgenommen, obwohl neu seit 658 (schmal):** Trainingspause (661), Kachel Insgesamt (666), „So misst du
richtig“ (671), Was ist neu (631, 692). Keine Website-Aussage widerspricht ihnen; „Ø Trainingsdauer“ stand nie
auf der Website (die „Trainingsdauer“ im Datenschutz ist die der Live Activity). Kein Satz schließt Bewegung in
der App aus (gesucht: Animation, Bewegung, ruhig, motion).

**Nachgezogen beim Prüfen (Abschnitt 3):** meine neuen Progressionssätze auf der Auswertung trugen selbst
„mehr Gewicht“ / „more weight“ und „beste“ / „best“; jetzt „eine höhere Last“, „je Trainingswoche der höchste Wert“.

## 3 · Prüfungen, je mit Exit-Code

Skripte im Scratch dieser Sitzung (`699/`), einmalig, nicht in `tools/`: ein Prüfer dort bräuchte im selben Zug
einen Eintrag in `check.sh` (FEHLER.md Nr. 50), und `tools/` gehört nicht zu diesem Ticket.

```
Wortprüfung woerter.py, vorher                 Exit 1   43 Funde (index 24, auswertung 6, datenschutz 6, llms 5,
                                                        ueber 1, impressum 1); alle Website-Dateien .html/.txt/.xml,
                                                        im Fluss (Leerraum zusammengezogen), ld+json und TEXTE inklusive
  davon Fehltreffer, Muster geschärft            2       „liest keine Exporte“ (wahr; ZIEL.md 3 meint Health) →
                                                        „liest keine Daten“; Impressum „No guarantee“ → (?<!no )
Wortprüfung nachher                            Exit 0   0 Funde
Gegenprobe (Kopie: „Kostenlos.“ im Hinweis,    Exit 1   ROT, 2 Funde, auch der Mutant über einen Zeilenumbruch
  „ab Werk an“ über zwei Zeilen im Datenschutz)
Nullprobe derselben Kopie vor der Mutation     Exit 0
python3 tools/website_rahmencheck.py           Exit 0   OK
python3 tools/website_storeabgleich.py         Exit 0   OK (31. Oktober 2027 in faq[5] bleibt)
python3 tools/website_namecheck.py             Exit 0   OK
htmlcheck.cjs (parse5, onParseError)           Exit 0   0 Parserfehler auf 6 Seiten; ld+json 5/5 gültig; Inline-
                                                        Skripte 15/15 übersetzen; TEXTE DE = EN (113 / 5 × 28 Schlüssel)
webkit393.cjs, WebKit 393 × 852, dunkel        Exit 0   12 Lagen (6 Seiten × DE/EN): Breite 393, 0 Text über der
  emuliert, alle FAQ aufgeklappt                        Kante, 0 abgeschnitten, gewählte Sprache sichtbar, andere aus,
                                                        Startseite DE jedes data-t = TEXTE.de, keine Skript- oder
                                                        Konsolenfehler, die neuen Sätze da, „ab Werk“/„on by default“ weg
Gegenprobe WebKit (Kopie, 3 Mutanten: langes   Exit 1   ROT an allen drei Stellen (Querlauf 638 / 614, EIGEN FEHLT)
  Wort Datenschutz, langes Wort Pro-Liste EN,
  EN-Block der Über-Seite umbenannt)
Gegenprobe WebKit 4 (.pro li max-height 40,    Exit 1   ROT, 25 Funde „abgeschnitten“ (der Zweig war in Gegenprobe 1
  overflow hidden)                                      nicht ausgelöst: das Wort verbreiterte das Raster)
./tools/check.sh --schnell                     Exit 0   191 Prüfer, 1 ausgelassen ohne Bau (prüft die Website nicht;
                                                        gelaufen, weil nichts lief: pgrep leer)
Volle Kette                                    offen, Kevin
```

**Zur Farbe:** die Website kennt nur Hell (30.9.2026, `color-scheme: light`, website_rahmencheck verbietet
Dunkel). „Dunkel emuliert“ heißt: WebKit meldet `prefers-color-scheme: dark`, die Seite bleibt hell, wie sie soll.

Selbst angesehen, 393 hell, Bilder in `doku/pruefung/699-bilder/`: Datenschutz iCloud DE/EN, Feedback DE,
Auswertung Progression DE/EN, Startseite Pro und FAQ „Wo liegen meine Daten?“ DE/EN. Nichts ragt über den Rand.
In den Ausschnitten von „Satzwerk Pro“ liegt die feste Kopfleiste über dem Abschnittsanfang: das ist die
Aufnahme (Element-Bild mit Sticky-Kopf), nicht die Seite.

## 4 · Selbst entschieden

1. **Negationen ohne die Wörter aus ZIEL.md 3.** Startseite „kein „nimm mehr Gewicht“, kein „Deload empfohlen““ →
   „keine Gewichtsvorgabe, kein Urteil über eine Entlastungswoche“; Auswertung „Kein „mehr Gewicht““ → „Keine
   Gewichtsvorgabe“. Die Sätze verneinten, sagten aber die Wörter, die ZIEL.md 3 nie sagen will. Bitte ansehen:
   die Haltung war Kevins Text.
2. **EN „free“:** wo es ein Geschenk ist „on us“ (wie App und Store), wo es der Tarif ist „Free“ („part of Free“,
   „Free applies“, „What is in Free, what is in Pro?“), und „Logging is free“ → „Logging needs no Pro“ (Store 2.3:
   „Included without Pro“). Dazu „as a gift“ → „on us“, damit App, Store und Website dasselbe Wort tragen.
3. **iCloud nach 700 in jeder Fassung „wenn du willst / if you want / wenn der Nutzer zustimmt“**, auch dort, wo
   ZIEL.md 3 „Daten auf dem iPhone und in der eigenen iCloud“ ausdrücklich erlaubt: ohne Ja liegt dort nichts.
4. **EN „Beginner and Advanced level“ → „an entry-level and an advanced version“.** Der Stufenname der App ist
   „Beginner“ (PHASE3 6: kein Verstoß), aber ein Leser oder eine KI liest „for beginners“ als Zielgruppe.
5. **Datenschutz, Gerätebackup und Apple Health.** „Apple Health ist ein lokaler Speicher des iPhones“ ist eine
   Aussage über Apple, die ich nicht belegen kann → „Was Apple Health selbst mit ihnen tut, regelt Apple.“ Neu der
   Satz zum iOS-Gerätebackup (Library-Kopie mit Health-Gewichten, P3-004; Apple: „The contents of the Library
   directory … are backed up by iTunes and iCloud.“) und die Körper-CSV als Ort eines gelesenen Gewichts.
6. **Schlüsselbund-Satz** „liegen nur auf diesem Gerät“ → „sind an dieses Gerät gebunden“: war wahr, aber genau
   das Muster absoluter Datensätze, das die Wortprüfung hält.
7. **„Keine Werkzeuge für Absturzberichte“** aufgenommen (PHASE3 4: kein Sentry, Crashlytics, TelemetryDeck,
   MetricKit). Was Apple bei „Mit App-Entwicklern teilen“ weitergibt, steht nicht da: nicht gemessen.
8. **Über-Seite:** Tippfehler „iPhone, Wie“ und „aus gymLog Satzwerk wird“ → „wurde“ in meta/og.
9. **Wettbewerbernamen:** „Hevy oder Strong“ bleibt auf Auswertung und in llms.txt. ZIEL.md 3 verbietet sie „in
   Store und Shop“, nicht auf der Website, und die Antwort ist eine Frage, die Leute stellen.

## 5 · Vor dem Push von Kevin abzunehmen

- **a) Rechtsgrundlage iCloud (658 5 a): ABGENOMMEN, Kevin 21.10.2026** („Die Rechtsgrundlage iCloud bleibt wie
  vorgeschlagen auf der Datenschutzseite.“). Steht DE und EN unter „iCloud-Sicherung“, der HTML-Kommentar sagt es:

  > Körperdaten können Gesundheitsdaten sein. Rechtsgrundlage ist deine Einwilligung nach Art. 6 Abs. 1 lit. a
  > und Art. 9 Abs. 2 lit. a DSGVO. Du gibst sie mit „Sichern“ oder indem du eine Sicherung zurückholst, und du
  > widerrufst sie jederzeit mit dem Schalter im Profil.

  Was der Code trägt: ohne „Sichern“ (oder Zurückholen) keine Datei, der Schalter widerruft. Ob eine
  Einwilligung die richtige Grundlage ist, ob Kevin für eine Datei in der iCloud des Nutzers überhaupt
  Verantwortlicher ist und ob der Text der Frage („Sicherung in iCloud?“) als Einwilligung reicht, ist
  Rechtsfrage (545). Passt der Vorschlag nicht: die zwei `<p class="klein">` unter dem iCloud-Abschnitt löschen.
- **b) Die Negationen (Abschnitt 4, Punkt 1)**: Kevins Haltungssatz ist umformuliert.
- **c) Empfänger und Drittland für iCloud (658 5 b)** bleiben, wie sie waren: „nach den Bestimmungen von Apple“.
- **d) Die Seiten nennen Version 2.3** (Auswertung „Stand: Version 2.3“, llms.txt); im Projekt steht 2.2 Build 33.
  Wie 658 5 c: die Website beschreibt 2.3 ab dem Push. Push deshalb am Tag des Einreichens.

## 6 · Mockups mit veralteter Aussage (bleiben, Kandidaten für 684)

Angesehen: alle sechs DE und `verlauf-en`; die übrigen EN nicht einzeln (Annahme, dass sie dieselbe Ansicht
zeigen, nicht geprüft).

```
mockup-verlauf-de   „gleich gegen Vorwoche“, „Ein Punkt je Monat, schwerster Satz“, Kurve des schwersten Satzes.
                    Seit 558/616/696: Urteil-Pille, Kraft (geschätzt), 35 Trainingswochen je Woche.
mockup-verlauf-en   „+5 lb vs. previous week“, „unchanged vs. previous week“, „One point per month, heaviest set“
                    (Stand vor 558: Gewicht gegen Vorwoche).
mockup-start-de/en  Beendeter Tag mit „Gegen Vorwoche +2,5 kg / +5 kg / +5:00“ und „Erneut trainieren“; der
                    beendete Tag ist seit 657 neu gebaut (Verdacht, nicht gegen den Code verglichen).
mockup-training-de  „1 Übung daneben · Zu leicht“: den Text gibt es weiter (bandSumOut, texte.js 294). Kein Befund.
Alle                Violett als Akzent und der Creme-Grund (seit 701 in der App Apples Grau). Gestaltung, 684.
```

Die Alt-Texte beschreiben weiter die Bilder („Vergleich mit der Vorwoche und Kurve des schwersten Satzes“) und
bleiben, wie in 658.

## 7 · Push und worauf Kevin danach schaut

**Der Push-Weg steht in keiner aktuellen Datei.** Das Projekt hat kein Remote (`.git/config` gelesen, nicht git
ausgeführt) und keinen Workflow; `doku/anleitung/ANLEITUNG_GITHUB.md` ist vom 10.8. (gymLog, Upload im
Browser). Deshalb kein Befehl von mir. Hochzuladen sind die sechs geänderten Dateien aus `website-satzwerk/`:

    index.html  auswertung/index.html  ueber/index.html  datenschutz/index.html  llms.txt  sitemap.xml

Seit 658 nicht gepusht (Bericht 658, 5 c), also gehen die Änderungen aus 658 mit. Wie dort: am Tag des
Einreichens von 2.3, zusammen mit den Store-Texten aus 659.

```
1  satzwerk.app/datenschutz/  DE: unter „iCloud-Sicherung“ fett „Ohne dein Ja legt Satzwerk keine Datei an.“
   „ab Werk eingeschaltet“ steht nirgends. Darunter „Feedback aus der App“ nach „Bewertungsdialog“.
2  Dieselbe Seite, „EN“: „Without your yes, Satzwerk creates no file.“, Stand 21 October 2026.
3  Startseite, Fragen, „Wo liegen meine Daten?“: „Satzwerk fragt einmal, ob es sie zusätzlich …“.
4  Startseite, „Erfassen und auswerten“, Progression: „Je Übung ein Urteil: stärker, gleich oder schwächer, ab der
   zweiten Trainingswoche.“ Pro-Liste: „Progression je Übung: stärker, gleich oder schwächer, …“
5  Startseite EN, Pro: Karte „30 days on us“; Hinweis oben „… and, if you want, in your own iCloud.“
6  satzwerk.app/auswertung/: „Stand: Version 2.3, 21. Oktober 2026“, Progression in vier Absätzen.
7  satzwerk.app/llms.txt: „ein Urteil je Übung“, iCloud „nur mit Zustimmung“.
```
