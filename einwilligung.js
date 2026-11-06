/* satzwerk.app, Einwilligung fuer Google Analytics. Das einzige Skript der Seite.
   Stand 6.11.2026, nach doku/prompts/WEBSITE.md Abschnitt 7.

   Vor einem Ja laedt nichts von Google. Ablehnen steht gleichwertig auf der
   ersten Ebene (BayLDA, Informationsblatt Consentbanner; § 25 TDDDG).
   Den Tag Manager bindet laden() nach Googles Anleitung ein:
   https://support.google.com/tagmanager/answer/14847097
   Das noscript-iframe aus der Anleitung fehlt mit Absicht: es wuerde ohne
   Einwilligung laden. */
(function () {
  "use strict";

  var SCHLUESSEL = "satzwerk-einwilligung";
  var CONTAINER = "GTM-K6KFSMKQ";

  var speicher = null;
  try {
    speicher = window.localStorage;
    speicher.getItem(SCHLUESSEL);
  } catch (fehler) {
    speicher = null;
  }

  // Alte Eintraege der frueheren Seite: Sprachwahl und hell oder dunkel.
  if (speicher) {
    try {
      speicher.removeItem("satzwerk-modus");
      speicher.removeItem("satzwerk-sprache");
    } catch (fehler) { /* nichts zu tun */ }
  }

  var englisch = (document.documentElement.getAttribute("lang") || "de").slice(0, 2) === "en";
  var T = englisch ? {
    titel: "May this site use Google Analytics?",
    vor: "It shows Satzwerk how visitors find the site. Google sets cookies for this, and data may go to the USA. Without your yes, nothing from Google loads. More in the ",
    link: "privacy policy",
    href: "/datenschutz/#en",
    nach: ".",
    nein: "Decline",
    ja: "Accept",
    einstellungen: "Cookie settings"
  } : {
    titel: "Darf diese Seite Google Analytics nutzen?",
    vor: "Damit sieht Satzwerk, wie Besucher die Seite finden. Google setzt dafür Cookies, und Daten können in die USA gehen. Ohne dein Ja lädt nichts von Google. Mehr im ",
    link: "Datenschutz",
    href: "/datenschutz/",
    nach: ".",
    nein: "Ablehnen",
    ja: "Annehmen",
    einstellungen: "Cookie-Einstellungen"
  };

  function lesen() {
    if (!speicher) return null;
    try {
      var wert = JSON.parse(speicher.getItem(SCHLUESSEL));
      if (wert && typeof wert.ga === "boolean") return wert;
    } catch (fehler) { /* kaputter Eintrag zaehlt wie keiner */ }
    return null;
  }

  function schreiben(ga) {
    if (!speicher) return;
    try {
      speicher.setItem(SCHLUESSEL, JSON.stringify({ ga: ga, zeit: new Date().toISOString() }));
    } catch (fehler) { /* dann kommt die Frage beim naechsten Aufruf wieder */ }
  }

  var geladen = false;
  function laden() {
    if (geladen) return;
    geladen = true;
    window.dataLayer = window.dataLayer || [];
    function gtag() { window.dataLayer.push(arguments); }
    window.gtag = gtag;
    gtag("consent", "default", {
      ad_storage: "denied",
      ad_user_data: "denied",
      ad_personalization: "denied",
      analytics_storage: "denied"
    });
    gtag("consent", "update", { analytics_storage: "granted" });
    // Google Tag Manager, Schnipsel aus Googles Anleitung, nur die Container-ID eingesetzt.
    (function (w, d, s, l, i) {
      w[l] = w[l] || [];
      w[l].push({ "gtm.start": new Date().getTime(), event: "gtm.js" });
      var f = d.getElementsByTagName(s)[0],
        j = d.createElement(s),
        dl = l != "dataLayer" ? "&l=" + l : "";
      j.async = true;
      j.src = "https://www.googletagmanager.com/gtm.js?id=" + i + dl;
      f.parentNode.insertBefore(j, f);
    })(window, document, "script", "dataLayer", CONTAINER);
  }

  function gaCookiesLoeschen() {
    var namen = [];
    document.cookie.split(";").forEach(function (teil) {
      var name = teil.split("=")[0].trim();
      if (name.indexOf("_ga") === 0) namen.push(name);
    });
    var host = window.location.hostname;
    var domains = ["", host, "." + host];
    var stuecke = host.split(".");
    if (stuecke.length > 2) {
      var basis = stuecke.slice(-2).join(".");
      domains.push(basis, "." + basis);
    }
    namen.forEach(function (name) {
      domains.forEach(function (domain) {
        document.cookie = name + "=; Max-Age=0; path=/" + (domain ? "; domain=" + domain : "");
      });
    });
  }

  var banner = null;

  function schliessen() {
    if (banner && banner.parentNode) banner.parentNode.removeChild(banner);
    banner = null;
    document.body.style.paddingBottom = "";
  }

  function polsterSetzen() {
    if (!banner) return;
    document.body.style.paddingBottom = (banner.offsetHeight + 24) + "px";
  }

  function antwort(ga) {
    var vorher = lesen();
    schreiben(ga);
    schliessen();
    if (ga) {
      laden();
    } else if ((vorher && vorher.ga) || geladen) {
      // Widerruf: Cookies von Google loeschen und ohne Google neu laden.
      gaCookiesLoeschen();
      window.location.reload();
    }
  }

  function zeigen() {
    if (banner) return;
    banner = document.createElement("div");
    banner.className = "einwilligung";
    banner.setAttribute("role", "region");
    banner.setAttribute("aria-label", "Google Analytics");

    var titel = document.createElement("p");
    titel.className = "einwilligung-titel";
    titel.textContent = T.titel;

    var text = document.createElement("p");
    text.className = "einwilligung-text";
    text.appendChild(document.createTextNode(T.vor));
    var link = document.createElement("a");
    link.href = T.href;
    link.textContent = T.link;
    text.appendChild(link);
    text.appendChild(document.createTextNode(T.nach));

    var knoepfe = document.createElement("div");
    knoepfe.className = "einwilligung-knoepfe";
    [[T.nein, false], [T.ja, true]].forEach(function (paar) {
      var knopf = document.createElement("button");
      knopf.type = "button";
      knopf.textContent = paar[0];
      knopf.setAttribute("data-antwort", paar[1] ? "ja" : "nein");
      knopf.addEventListener("click", function () { antwort(paar[1]); });
      knoepfe.appendChild(knopf);
    });

    banner.appendChild(titel);
    banner.appendChild(text);
    banner.appendChild(knoepfe);
    document.body.appendChild(banner);
    polsterSetzen();
  }

  function einstellungenEinsetzen() {
    var liste = document.getElementById("rechtliches");
    if (!liste) return;
    var li = document.createElement("li");
    var knopf = document.createElement("button");
    knopf.type = "button";
    knopf.className = "fuss-knopf";
    knopf.textContent = T.einstellungen;
    knopf.addEventListener("click", zeigen);
    li.appendChild(knopf);
    liste.appendChild(li);
  }

  function start() {
    einstellungenEinsetzen();
    var gespeichert = lesen();
    if (gespeichert === null) {
      zeigen();
    } else if (gespeichert.ga) {
      laden();
    }
    window.addEventListener("resize", polsterSetzen);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
})();
