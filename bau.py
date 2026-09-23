# -*- coding: utf-8 -*-
import json, html, sys
OUT = sys.argv[1]
STORE_URL = "https://apps.apple.com/app/id6786720640"
# Dieselben Adressen wie in der App, src/bauteile/ueberdieapp.jsx
IG_URL = "https://www.instagram.com/satzwerktraining"
LI_URL = "https://www.linkedin.com/company/satzwerk-app"

DE = {
  "skip": "Zum Inhalt",
  "marke": "Satzwerk",
  "lang": "EN",
  "lang_aria": "Switch to English",
  "store": "Im App Store",
  "h1": "Tracken. Nicht scrollen.",
  "lead": "Satzwerk erfasst dein Training und wertet es aus. Für Leute, die ihren Plan schon haben.",
  "hinweis": "Für iPhone. Keine Werbung, kein Konto nötig, deine Daten bleiben auf dem Gerät.",
  "alt_vorn": "Bildschirm von Satzwerk während des Trainings: Sätze mit Gewicht, Wiederholungen und Haken",
  "alt_hinten": "Startbildschirm von Satzwerk: Wochenkalender, aktiver Plan und der nächste Trainingstag mit Übungen und Gewichten",
  "p1": "Eintragen, ohne den Satz zu unterbrechen. Gewicht und Wiederholungen tippen, abhaken, weiter. Der nächste Satz übernimmt den Wert als grauen Vorschlag. Aufwärmsätze sind eigene Zeilen und zählen in der Auswertung nie mit. Am letzten Satz trägst du den RIR ein, daraus rechnet die App die Intensität.",
  "p2": "Ausgewertet wird, was eine Entscheidung trägt: harte Sätze je Muskelgruppe, diese Woche gegen die Vorwoche. Der Anteil der Sätze nahe am Limit. Der Verlauf je Übung über die Zeit. Dazu der Körperbereich mit Gewicht und Wochenrate, Körperfett aus Hautfalten, fettfreier Masse und Kalorienziel.",
  "p3": "Satzwerk zeigt, wo du stehst. Es sagt dir nicht, was du tun sollst. Keine Handlungsempfehlungen, kein „nimm mehr Gewicht“, kein „Deload empfohlen“. Ein Onboarding kennt deinen Bandscheibenvorfall nicht, deinen Blutdruck nicht und dein Sprunggelenk nicht. Pläne kommen von Menschen, die dich kennen. Die Zahlen kommen von hier.",
  "h2_drin": "Was drin ist",
  "liste": [
    "170 Übungen, eigene frei anlegbar","RIR je Satz","Harte Sätze je Muskelgruppe","Verlauf je Übung",
    "Mehrere Studios getrennt","Körperfett aus Hautfalten","Kalorienbedarf und Zielrate",
    "Live Activity am Sperrbildschirm","Export und Wiedereinlesen","Deutsch und Englisch",
    "Metrisch und imperial","Hell, dunkel oder automatisch","Apple Health (schreibend)",
  ],
  "nicht": "Keine fertigen Trainingspläne, kein Feed, kein Kalorienzählen.",
  "h2_laden": "Für das nächste Training.",
  "h2_faq": "Fragen und Antworten",
  "faq": [
    ["Was ist Satzwerk?",
     "Satzwerk ist ein Trainingstagebuch für das iPhone. Du trägst Gewicht, Wiederholungen und RIR je Satz ein, und Satzwerk wertet daraus harte Sätze je Muskelgruppe, Intensität und den Verlauf je Übung aus. Dazu kommt ein Körperbereich mit Gewicht, Körperfett aus Hautfalten und Kalorienziel."],
    ["Für wen ist die App gedacht?",
     "Satzwerk ist für Leute gedacht, die ihren Trainingsplan schon haben und ihn nur noch erfassen und auswerten wollen. Die App gibt keine Handlungsempfehlungen und enthält keine fertigen Pläne. Wer einen Plan sucht, ist bei einem Trainer oder einer Trainerin richtig."],
    ["Brauche ich ein Konto?",
     "Nein, für Satzwerk ist kein Konto nötig. Die App läuft ohne Anmeldung, ohne E-Mail-Adresse und ohne Passwort. Du installierst sie und trägst dein erstes Training ein."],
    ["Wo liegen meine Daten?",
     "Alle Daten von Satzwerk liegen auf deinem iPhone. Es gibt keinen Server, an den Trainings oder Körperwerte übertragen werden. Ein Export als Datei ist jederzeit möglich, und die Historie hat keine Zeitgrenze."],
    ["Gibt es fertige Trainingspläne?",
     "Nein, Satzwerk enthält keine fertigen Trainingspläne. Du legst deinen eigenen Plan an, mit Trainingstagen, Übungen und Sollsätzen. Die App erfasst und wertet aus, sie gibt keine Vorgaben."],
    ["Was ist RIR und wie wird er erfasst?",
     "RIR steht für Reps in Reserve, also die Wiederholungen, die am Ende eines Satzes noch möglich gewesen wären. In Satzwerk trägst du den RIR am letzten Satz einer Übung ein, mit einem Tipp auf einen Wert von 0 bis 3. Daraus berechnet Satzwerk, welcher Anteil deiner Sätze nahe am Limit lag."],
    ["Was sind harte Sätze je Muskelgruppe?",
     "Ein harter Satz ist in Satzwerk ein Arbeitssatz mit RIR 0 bis 2, also nahe am Limit. Satzwerk zählt diese Sätze je Muskelgruppe für die laufende Woche von Montag bis Sonntag und stellt die Vorwoche daneben. Aufwärmsätze zählen nie mit."],
    ["Kann ich meine Daten exportieren?",
     "Ja, Satzwerk exportiert alle Trainings und Körperwerte als Datei, die du sichern oder auf ein neues iPhone übertragen kannst. Dieselbe Datei liest Satzwerk auch wieder ein. Trainings und Körperwerte lassen sich zusätzlich als CSV ausgeben."],
    ["Gibt es die App für Android oder die Apple Watch?",
     "Nein. Satzwerk gibt es nur für das iPhone, nicht für Android und nicht für die Apple Watch. Die Live Activity am Sperrbildschirm läuft auf dem iPhone."],
    ["Warum heißt die App Satzwerk?",
     "Der Name setzt sich aus Satz und Werk zusammen. Satz steht für den Trainingssatz, die kleinste Einheit im Krafttraining. Werk steht für Handwerk, für die eigene Arbeit am eigenen Körper."],
  ],
  "claim": "Handwerk am eigenen Körper.",
  "fuss2": "Satz für den Trainingssatz, Werk für Handwerk.",
  "folgen": "Folge uns",
  "rechtliches": "Rechtliches",
  "fuss_iphone": "Für iPhone.",
  "marken": "Apple, App Store, Apple Watch und iPhone sind Marken der Apple Inc., eingetragen in den USA und weiteren Ländern.",
  "ig_label": "Satzwerk auf Instagram",
  "li_label": "Satzwerk auf LinkedIn",
  "impressum": "Impressum",
  "datenschutz": "Datenschutz",
}

EN = {
  "skip": "Skip to content",
  "marke": "Satzwerk",
  "lang": "DE",
  "lang_aria": "Auf Deutsch wechseln",
  "store": "On the App Store",
  "h1": "Track. Don’t scroll.",
  "lead": "Satzwerk records your training and evaluates it. For people who already have their plan.",
  "hinweis": "For iPhone. No ads, no account needed, your data stays on the device.",
  "alt_vorn": "Satzwerk screen during a workout: sets with weight, reps and check marks",
  "alt_hinten": "Satzwerk home screen: week calendar, active plan and the next training day with exercises and weights",
  "p1": "Log without breaking the set. Type weight and reps, check it off, move on. The next set takes the value as a grey suggestion. Warm-up sets are their own rows and never count in the analysis. On the last set you enter the RIR, and the app calculates intensity from it.",
  "p2": "What gets evaluated is what carries a decision: hard sets per muscle group, this week against last week. The share of sets close to the limit. The trend per exercise over time. Plus the body section with weight and weekly rate, body fat from skinfolds, lean mass and calorie target.",
  "p3": "Satzwerk shows you where you stand. It does not tell you what to do. No recommendations, no “add more weight”, no “deload suggested”. An onboarding does not know about your herniated disc, your blood pressure or your ankle. Plans come from people who know you. The numbers come from here.",
  "h2_drin": "What is in it",
  "liste": [
    "170 exercises, add your own","RIR per set","Hard sets per muscle group","Trend per exercise",
    "Several gyms kept apart","Body fat from skinfolds","Calorie needs and target rate",
    "Live Activity on the lock screen","Export and re-import","German and English",
    "Metric and imperial","Light, dark or automatic","Apple Health (write only)",
  ],
  "nicht": "No ready-made training plans, no feed, no calorie counting.",
  "h2_laden": "For the next session.",
  "h2_faq": "Questions and answers",
  "faq": [
    ["What is Satzwerk?",
     "Satzwerk is a training log for the iPhone. You enter weight, reps and RIR per set, and Satzwerk turns that into hard sets per muscle group, intensity and the trend per exercise. There is also a body section with weight, body fat from skinfolds and a calorie target."],
    ["Who is the app for?",
     "Satzwerk is for people who already have a training plan and only want to record and evaluate it. The app gives no recommendations and contains no ready-made plans. If you are looking for a plan, a coach is the right place."],
    ["Do I need an account?",
     "No, Satzwerk needs no account. The app runs without sign-up, without an e-mail address and without a password. You install it and log your first workout."],
    ["Where is my data stored?",
     "All Satzwerk data stays on your iPhone. There is no server that workouts or body values are sent to. You can export a file at any time, and the history has no time limit."],
    ["Are there ready-made training plans?",
     "No, Satzwerk contains no ready-made training plans. You create your own plan with training days, exercises and target sets. The app records and evaluates, it does not prescribe."],
    ["What is RIR and how is it recorded?",
     "RIR stands for reps in reserve, the repetitions you could still have done at the end of a set. In Satzwerk you enter the RIR on the last set of an exercise with one tap on a value from 0 to 3. From that, Satzwerk calculates the share of your sets that were close to the limit."],
    ["What are hard sets per muscle group?",
     "In Satzwerk a hard set is a working set with RIR 0 to 2, so close to the limit. Satzwerk counts these sets per muscle group for the current week from Monday to Sunday and shows last week next to it. Warm-up sets never count."],
    ["Can I export my data?",
     "Yes, Satzwerk exports all workouts and body values as a file that you can back up or move to a new iPhone. Satzwerk reads the same file back in. Workouts and body values can also be exported as CSV."],
    ["Is there an Android or Apple Watch version?",
     "No. Satzwerk is available for the iPhone only, not for Android and not for the Apple Watch. The Live Activity on the lock screen runs on the iPhone."],
    ["Why is the app called Satzwerk?",
     "The name is made of the German words Satz and Werk. Satz means set, the smallest unit in strength training. Werk means craft, the work you do on your own body."],
  ],
  "claim": "Handwerk am eigenen Körper.",
  "fuss2": "Satz for the training set, Werk for craft.",
  "folgen": "Follow us",
  "rechtliches": "Legal",
  "fuss_iphone": "For iPhone.",
  "marken": "Apple, App Store, Apple Watch and iPhone are trademarks of Apple Inc., registered in the U.S. and other countries.",
  "ig_label": "Satzwerk on Instagram",
  "li_label": "Satzwerk on LinkedIn",
  "impressum": "Legal notice",
  "datenschutz": "Privacy",
}
assert len(DE["faq"]) == 10 and len(EN["faq"]) == 10 and set(DE) == set(EN)
e = html.escape

faq_ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
  {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in DE["faq"]]}
app_ld = {"@context":"https://schema.org","@type":"SoftwareApplication","name":"Satzwerk",
  "applicationCategory":"HealthApplication","operatingSystem":"iOS","url":STORE_URL,
  "description":DE["lead"],"author":{"@type":"Person","name":"Kevin Schropp"}}
ld = lambda o: json.dumps(o, ensure_ascii=False, indent=1)

liste_html = "\n".join(f'      <li data-t="liste.{i}">{e(x)}</li>' for i,x in enumerate(DE["liste"]))
faq_html = "\n".join(f'''    <details class="faq">
      <summary data-t="faq.{i}.0">{e(q)}</summary>
      <p data-t="faq.{i}.1">{e(a)}</p>
    </details>''' for i,(q,a) in enumerate(DE["faq"]))
texte_js = json.dumps({"de":DE,"en":EN}, ensure_ascii=False, indent=1)

page = open("/sessions/determined-funny-newton/mnt/outputs/satzwerk-web/vorlage.html", encoding="utf-8").read()
def storeknopf(zusatz):
    # Ein Knopf, vier Groessen. Text statt Abzeichen, kein Apple-Logo; der
    # Pfeil ist lucide/arrow-up-right (ISC, wie die Symbole der App).
    return ('<a class="glas glas-store' + zusatz + '" href="' + STORE_URL + '">'
            '<span class="glas-filter"></span><span class="glas-toenung"></span><span class="glas-fuell"></span><span class="glas-glanz"></span>'
            '<span class="glas-inhalt"><span data-t="store">' + e(DE["store"]) + '</span>'
            '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 7h10v10"/><path d="M7 17 17 7"/></svg>'
            '</span></a>')

ersatz = {
  "%%APP_LD%%": ld(app_ld), "%%FAQ_LD%%": ld(faq_ld), "%%LISTE%%": liste_html,
  "%%FAQ%%": faq_html, "%%TEXTE%%": texte_js, "%%STORE%%": STORE_URL,
  "%%IG%%": IG_URL, "%%LI%%": LI_URL,
  "%%STOREKNOPF%%": storeknopf(""),
  "%%STOREKNOPF_GROSS%%": storeknopf(" glas-store-gross"),
  "%%STOREKNOPF_KLEIN%%": storeknopf(" glas-store-klein"),
  "%%STOREKNOPF_FUSS%%": storeknopf(""),
}
for k in DE:
    if isinstance(DE[k], str): ersatz["%%"+k+"%%"] = e(DE[k])
for k,v in ersatz.items():
    page = page.replace(k, v)
assert "%%" not in page, [l for l in page.splitlines() if "%%" in l][:5]

# Selbstpruefung
low = page.lower()
import re
for w in ["kostenlos","gratis","abo","abos","free","hevy","strong","jefit","fitbod","lorem","georgia","revolutionär","einfach"]:
    m = re.search(r"\b"+w+r"\b", low)
    assert not m, (w, low[m.start()-40:m.end()+40])
sichtbar = json.dumps({"de":DE,"en":EN}, ensure_ascii=False).lower()
for w in ["!","jetzt"]:
    assert w not in sichtbar, w
assert page.count("<h1") == 1 and page.count("@font-face") == 2
assert 'href="/impressum/"' in page and 'href="/datenschutz/"' in page
for q,a in DE["faq"]:
    assert page.count(a) >= 2  # sichtbar + JSON-LD
open(OUT,"w",encoding="utf-8").write(page)
print("ok", len(page))
