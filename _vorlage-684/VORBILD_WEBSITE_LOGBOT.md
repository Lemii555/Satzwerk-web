# Vorbild für Ticket 684: log-bot.com

**Stand 21.10.2026, Chat-Claude.** Kevin: „Ignoriere den Inhalt, schau dir Aufbau und Animationen und
Branding an, sehr ruhig, sehr hochwertig. Wie können wir das für Satzwerk homepage nutzen. … wo man scrollt
auf dem handy und pc und sich denkt das hat niemals eine typische KI gemacht.“

Gemessen in Kevins Chrome am Desktop (Fenster 2174 px breit), Seite https://log-bot.com/de. Die Handyansicht
ließ sich nicht rendern: die Fenstergröße war fest, Einbetten sperrt die Seite. Was unten zum Handy steht,
kommt aus dem Code der Seite (Bildquellen je Breite), nicht aus einem Bildschirmfoto.

---

## 1 · Gemessen

```
Technik       Next.js und Tailwind, Bewegung über eine Motion-Bibliothek (Inline-Stile opacity und
              transform). 15 Abschnitte, rund 11.900 px hoch am Desktop.
Bildklammer   Kopf: Video hero-dawn-loop (Morgendämmerung, Nebel). Fuß: Foto footer-dusk (Abend,
              Lichter an), derselbe Ort. Dazwischen kein einziges Foto.
              Je drei Zuschnitte: Desktop ab 1024 px, Tablet ab 640 px, Handy darunter.
Video         Erst steht das Foto. Das Video blendet in 1,2 s darüber ein (opacity, ease-out).
              Kein Ladebalken, kein leerer Moment.
Schrift       Systemschrift (-apple-system, auf Apple-Geräten SF). Mono: Fira Code für Zahlen,
              Uhrzeiten, kleine Etiketten. Kopfzeile 72 px, Gewicht 500. H2 36 px, Gewicht 600,
              Laufweite -0,9 px. Fließtext 18 px, Zeilenhöhe 29 px, Textbreite 768 px,
              Inhalt 1000 px breit.
Farbe         Kein Schwarz. Tinte #0D1B1E, Text #1E3A42, alle Grautöne aus einer Familie
              (#2F545F, #3F6A76, #6E97A0, #8FA8AD, #B7CBCF). Flächen weiß, #F0F7F5, #EAF5F9.
              EIN Akzent: Amber #F59E0B, nur für Zahlen, „Live“ und Ebene 3. Grün #2F855A nur
              für Status.
Flächen       Tonleiter: Ebene 1 weiße Karte, Ebene 2 hellblaue Karte, Ebene 3 dunkle Tintenkarte.
              Die Abschnitte wechseln weiß, hellblau, dunkle Karte. Rhythmus statt Dekoration.
Ecken         24, 18, 10, 8 px und Kapsel.
Schatten      in Tinte getönt, negativer Spread, kaum sichtbar
              (Beispiel: 0 10px 30px -18px rgba(13,27,30,.18)).
Glas          nur die schwebende Navigation (blur 20 px). Sonst nirgends.
Bewegung      Inhalte blenden beim Reinscrollen einmal weich ein. Hover 150 bis 200 ms. Genau eine
              Dauerschleife: ein pulsierender Live-Punkt. prefers-reduced-motion steht im CSS.
Produkt       Statt Bildschirmfoto ein Live-Protokoll in Mono mit Uhrzeiten
              („08:14 Auftrag angelegt“), die Zeilen kommen nacheinander.
Atempause     Ein Abschnitt nur mit einem großen, zentrierten Satz. Keine Karte, kein Bild.
```

**Schwächen, damit es kein Altar wird:** Die Kartenansicht zeigt das Wasserzeichen „API KEY REQUIRED“. Die
Mitte ist kartenlastig. Kopf- und Fußbild wirken generiert, belegen lässt sich das nicht. Es fällt kaum
auf, weil die Bildregie stimmt.

**Gegenprobe philsmedia.de (20.10.2026):** 22 Dauerschleifen, gespielter Ladebalken, 3D-Kugel mit 948 KB
Lichtdatei. LogBot: eine Schleife, kein Ladebalken, Foto vor Video.

## 2 · Warum es ruhig wirkt

Nicht durch Effekte, sondern durch Weglassen:

```
1  Fotos nur zweimal, dafür groß und als Klammer.
2  Eine Akzentfarbe, sparsam.
3  Bewegung nur beim ersten Erscheinen.
4  Rhythmus über die Flächenfarbe, nicht über Rahmen und Schmuck.
5  Systemschrift: wirkt wie Apple, weil sie es ist.
```

## 3 · satzwerk.app heute (21.10.2026)

Creme #F4F2EE, Text reines Schwarz, Fraunces fett (Kopfzeile 60 px) für die Überschriften, Public Sans im Text,
Kapsel-Navigation, zwei schräge Handys im Kopf, vier Spalten mit Handys, graues Band, Frei/Pro-Liste.
Sauber gebaut. Das Problem: Creme, fette Serifenschrift, Kapsel-Navigation und schräge Handys sind 2026 der
Look, den KI-Baukästen ausgeben. Und es gibt keinen Menschen, keinen Ort, keine Stimmung. Alles ist
Bildschirm.

## 4 · Was Satzwerk übernimmt, nach Wirkung

**Punkt 1 überholt, Kevin 21.10.2026, 17:05: ohne Foto** (gebaut in 684b, Bericht 684 Abschnitt 12). Die Klammer
bleibt als Ton: oben hell mit der Bildmarke, unten dunkel.

```
1  BILDKLAMMER     Die Werkstatt am Morgen, die Werkstatt am Abend. Kopf: leeres Studio früh,
                   Fensterlicht, Stange am Boden. Fuß: dasselbe Studio abends, gedämpftes Licht,
                   Handtuch über der Bank. Passt zu „Handwerk am eigenen Körper“.
                   STANDBILD, kein Video: Loops sind seit 298 ausgeschlossen, und LogBot zeigt,
                   dass das Foto allein trägt.
2  TONLEITER       Frei als helle Karte, Pro als dunkle Karte mit Violett, wie Ebene 1 bis 3.
                   Die dunklen Karten tragen die Dunkelmodus-Bildschirme aus dem Store. So passen
                   die helle Website (30.9.2026) und die dunklen Store-Bilder (19.10.2026)
                   zusammen, ohne eine der beiden Entscheidungen zu kippen.
3  FARBE           Tinte statt reinem Schwarz. Violett nur für Pro und einen Akzent.
                   Grautöne aus einer Familie.
4  SCHRIFT         Fraunces nur für die Wortmarke und höchstens die eine Kopfzeile. Sonst
                   Systemschrift wie die App. Zahlen in Mono oder tabular-nums (684 verlangt
                   tabular-nums ohnehin).
5  PRODUKT LEBT    Statt vier Bildschirmfotos ein Satz-Protokoll in Mono, Zeilen kommen einmal
                   nacheinander, z. B. „Langhantel-Kniebeuge · 142,5 kg × 8“. Werte nur aus den
                   Demodaten der App (erlaubt seit 13.10.2026), nichts erfunden.
6  BEWEGUNG        Ein Muster, einmal beim Reinscrollen, mit der Kurve der App (.33,1,.68,1).
                   Dazu höchstens Linie zeichnen und Ziffernrad aus 683. Keine Schleife, kein
                   Federn, reduced motion.
7  ATEMPAUSE       „Befunde, keine Anweisungen.“ als großer, zentrierter Satz, ohne Spalten.
8  KURZ BLEIBEN    Heute sechs Abschnitte, das bleibt die Größe (LogBot hat 15, weil B2B).
                   Neu ist die Folge: Kopf mit Bild, was es tut (drei statt vier), Satz-Protokoll,
                   Atempause, Frei und Pro, Fragen, Fuß mit Bild.
```

**Handy zuerst:** Kopfbild hochkant mit dem Motiv unten, Text oben. Navigation auf Wortmarke und
App-Store-Knopf. Raster wird eine Spalte. Jedes Bild in drei Zuschnitten wie bei LogBot.

## 5 · Was Satzwerk NICHT übernimmt

```
Video-Loop im Kopf        Regel aus 298
Amber und Teal            Satzwerk hat Violett
Kartenwüste in der Mitte  B2B-Funktionslisten, nicht unser Fall
Live-Punkt als Schmuck    nur, wo wirklich etwas läuft (das Protokoll)
```

## 6 · Bilder

Gebraucht: zwei, höchstens drei. Kevin kauft sie (21.10.2026).

```
1  Kopf     Studio am Morgen, leer, Fensterlicht, Stange oder Hantel am Boden
2  Fuß      dasselbe Studio oder dieselbe Serie am Abend, gedämpftes Licht
3  Detail   optional: Hände, Kreide, Griff. Kein Gesicht
```

- **Aus EINER Serie desselben Fotografen.** Sonst passt das Licht zwischen Kopf und Fuß nicht. Das ist der
  wichtigste Punkt.
- Keine Gesichter oder abgewandt. Kein freier Oberkörper, kein Lächeln in die Kamera, keine bunten
  Kettlebells. FOTO_BRIEFING.md: „Wenn ein Bild aussieht, als könnte es in einem Supplement-Katalog
  stehen, ist es falsch.“
- Gedämpfte Farben, natürliches Licht, viel Ruhe im Bild.
- KI-Bilder ausschließen. Adobe Stock hat laut Adobe-Community einen Suchfilter für generative KI, der je
  Suche gesetzt wird.
- Lizenz: Standardlizenz für die Website. „Nur redaktionell“ (editorial use only) ausschließen.
  Sind Personen erkennbar, braucht es eine Modellfreigabe.
- Ein Bild muss drei Zuschnitte tragen (quer, Tablet, hochkant). Also volle Auflösung und Luft um das
  Motiv.
- Eigene Fotos in fremden Studios gehen nur mit Einwilligung aller Erkennbaren und des Betreibers. Stock
  löst das.

## 7 · Offen, Kevin entscheidet beim Start von 684

```
1  Website hell mit dunklen Produktkarten, oder ganz dunkel?
2  Fraunces nur für die Wortmarke, oder auch für die Kopfzeile?
3  Satz-Protokoll statt Bildschirmfotos, oder beides?
4  Bilder: welche Stock-Serie, oder doch ein eigenes Shooting mit Erlaubnis?
```
