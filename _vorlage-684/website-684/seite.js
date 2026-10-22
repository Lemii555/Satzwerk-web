/* website-684/seite.js — Sprache und Auftritt, fuer alle Seiten (Ticket 684, 21.10.2026)

   SPRACHE. Jede Seite traegt ihre Texte als var TEXTE im HTML (Deutsch steht
   ausserdem im HTML selbst, fuer Suchmaschinen und ohne Skript). Die Startseite
   wechselt nur auf eine gespeicherte Wahl; die Unterseiten nehmen ohne Wahl die
   Browsersprache (<html data-sprachwahl="browser">). So war es vor 684, und so
   bleibt es: eine Suchmaschine mit englischem Browser liest die Startseite
   weiter auf Deutsch.

   AUFTRITT. Was .auftritt traegt, tritt einmal auf, wenn es ins Bild kommt;
   das Protokoll baut sich einmal Zeile fuer Zeile auf. Das Skript setzt nur
   die Klasse .da, die Bewegung selbst steht in seite.css. Ohne
   IntersectionObserver steht alles sofort. */
(function () {
  var html = document.documentElement;
  html.classList.add("js");
  /* Die Website gibt es nur hell (30.9.2026). Eine frueher gespeicherte Wahl wird geloescht. */
  try { localStorage.removeItem("satzwerk-modus"); } catch (e) {}

  var TEXTE = window.TEXTE || {};
  function hole(obj, pfad) {
    return pfad.split(".").reduce(function (o, k) { return o == null ? o : o[k]; }, obj);
  }
  function setzeSprache(sprache) {
    var t = TEXTE[sprache] || TEXTE.de || {};
    [["data-t", null], ["data-t-aria", "aria-label"], ["data-t-alt", "alt"]].forEach(function (paar) {
      document.querySelectorAll("[" + paar[0] + "]").forEach(function (el) {
        var v = hole(t, el.getAttribute(paar[0]));
        if (typeof v !== "string") return;
        if (paar[1]) el.setAttribute(paar[1], v); else el.textContent = v;
      });
    });
    html.setAttribute("lang", sprache);
    html.setAttribute("data-lang", sprache);
    /* Ein Bildschirm der App je Sprache (Demodaten DE und EN). Nur die Endung wechselt, der Pfad bleibt
       relativ wie im HTML (Doppelklick, Ticket 684). */
    document.querySelectorAll("[data-bildschirm]").forEach(function (el) {
      el.setAttribute("src", el.getAttribute("src").replace(/-(de|en)\.jpg$/, "-" + sprache + ".jpg"));
    });
    try { localStorage.setItem("satzwerk-sprache", sprache); } catch (e) {}
  }

  var gespeichert = null;
  try { gespeichert = localStorage.getItem("satzwerk-sprache"); } catch (e) {}
  if (html.getAttribute("data-sprachwahl") === "browser") {
    setzeSprache(gespeichert === "de" || gespeichert === "en" ? gespeichert
      : ((navigator.language || "de").slice(0, 2) === "de" ? "de" : "en"));
  } else if (gespeichert === "en") {
    setzeSprache("en");
  }
  document.querySelectorAll("[data-sprachknopf]").forEach(function (k) {
    k.addEventListener("click", function () {
      setzeSprache(html.getAttribute("lang") === "en" ? "de" : "en");
    });
  });

  /* Einmal, beim Reinscrollen. Das Protokoll erst, wenn ein Drittel davon im Bild ist. */
  function beobachte(auswahl, schwelle) {
    var ziele = Array.prototype.slice.call(document.querySelectorAll(auswahl));
    if (!("IntersectionObserver" in window)) { ziele.forEach(function (el) { el.classList.add("da"); }); return; }
    var io = new IntersectionObserver(function (eintraege) {
      eintraege.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add("da");
        io.unobserve(e.target);
      });
    }, { threshold: schwelle });
    ziele.forEach(function (el) { io.observe(el); });
  }
  beobachte(".auftritt", 0);
  beobachte(".protokoll", 0.3);
})();
