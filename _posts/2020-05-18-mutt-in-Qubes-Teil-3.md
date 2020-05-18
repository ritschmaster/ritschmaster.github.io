---
layout: post
title:  mutt in Qubes - Teil 3 - abook
author: Richard Bäck
---

In Teil 2 habe ich gezeigt, wie einfach man in Qubes bestimmte Applikationen auf bestimmte Tastenkürzel vorbelegen kann. In diesem Teil betrachten wir die Applikation [abook](https://abook.sourceforge.net/) genauer und wie wir sie für unsere Zwecke nutzen können.

# Was ist abook

abook ist eine Applikation zur Kontakt-Verwaltung. Das ist Thunderbird und Outlook unter anderem auch. Allerdings hat abook keine grafische Oberfläche. Nein, es hat eine Curses-Oberfläche. Das bedeutet, dass die gesamte Applikation mit Tastenkombinationen über das Terminal bedienbar ist. Hier ein paar Eigenschaften/Vorteile:

1. Kontakte können gesucht und gepflegt werden ohne die Maus zu bedienen. Das ist nicht nur in der Bedienung selbst angenehm, das erlaubt es auch "kurz einmal" das Kontaktbuch aufzuschlagen. Nicht wie in Thunderbird wo mehrere Mausklicks benötigt werden und man somit mehr Zeit benötigt.
2. Eine unschlagbare Startzeit. Eine kurze Überprüfung ob bestimmte Kontaktdaten bereits gepflegt sind geht somit blitzschnell. Wie jede Terminalapplikation kann man eine Tastenkombination für den Window Manager hinterlegen und somit sofort in die Suche springen.
3. Eine unschlagbare Reaktionszeit. Bei über 300 Kontakten geht man die Liste trotzdem so schnell durch, als wären es 5 Kontakte.
4. Die Kontakte sind im Klartext gehalten. Somit können auch andere (Terminal-)Applikationen sehr einfach die gesammelten Kontaktdaten verwerten.

# Ich verwende schon was anderes

Kein Problem. Wenn das andere Thunderbird ist, dann ist es möglich sehr einfach zu wechseln. Ich hab dafür diesen [Blog-Eintrag](/2019/12/28/Thunderbird-Kontakte-zu-abook-konvertieren.html) geschrieben.

Sollte das andere Outlook usw sein, dann kann Thunderbird als Migrationsplattform verwendet werden. Einfach nach Thunderbird migrieren und von dort dann die oben genannte Anleitung durchführen. Schon ist man auch in abook!

# Das Applikationsprinzip

Beim Einstieg in die Applikation werden einem alle Kontakte in einer Liste präsentiert. Auf dieser Ebene kann man verschiedene Aktionen durchführen:

* Kontakte suchen
* Neue Kontakte hinzufügen
* Bestehenden Kontakt editieren
* Kontakte exportieren

Je nach Aktion verbleibt man in der Liste (zB bei der Suche) oder wechselt in eine andere Maske (zB um den bestehenden Kontakt zu editieren).

Jeder Kontakt hat verschiedene Datenfelder. Diese können zeichenartig (zB der Nachname), E-Mail, Liste (mehrere Zeichenketten) und Datum. Die einzelnen Datenfelder wiederum werden zusammengefasst auf Sichten.

# Die Konfiguration

abook kommt mit einigen Standardfeldern innerhalb der Applikation. Diese sind umfassen die wichtigsten Felder und sind schon fast ausreichend. Zur Vollständigkeit fehlen aber der Geburtstag und eine Unterscheidung zwischen Arbeitsadresse und Privatadresse. Glücklicherweise können die Datenfelder und auch Sichten innerhalb von abook über eine Konfigurationsdatei angepasst werden.

Um sich an die [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html) zu halten, legen wir die Konfiguration folgendermaßen an:

    mkdir ~/.config/abook # eigentliches Konfigurationsverzeichnis
    ln -s ~/.config/abook ~/.abook # Symbolischer Link, wird von abook benötigt
    touch ~/.config/abook/abookrc # Die Konfiguration
    touch ~/.config/abook/addressbook # Das Adressbuch mit den Kontakten im Klartext

Weiter gehts mit der Konfiguration selbst:

* Felder werden wiefolgt definiert: <br>
  `field <Interner Feldname> = <Externer Feldname>, <Datentyp>` <br>
  Der interne Feldname wird in der `addressbook` Datei verwendet. Der externe Feldname in der Darstellung innerhalb der Applikation.
* Sichten werden wiefolgt definiert: <br>
  `view <Sichtname> = <Interner Feldname 1>, ..., <Interner Feldname n>` <br>
  Die Sichten haben keine Bedeutung für die `addressbook` Datei und sind rein nur für die Anzeige/Pflege gedacht.

## Meine Konfiguration

Ich selber verwende eine Konfiguration angelehnt an Thunderbird. Diese habe ich bereits in dem bereits erwähnten, älteren [Blog-Eintrag](/2019/12/28/Thunderbird-Kontakte-zu-abook-konvertieren.html) gelistet. Eben diese schlage ich auch Neulingen vor, da sie bereits alles notwendige aus - wahrscheinlich - bekannten Umfeldern beinhaltet.

# Das Adressbuch

Das Adressbuch ist sehr simpel. Es wird im Klartext gehalten und jeder Kontakt erhält eine eindeutige, fortlaufende Identifikationsnummer. Hinter dieser werden dann einfach die Datenfelder zusammengehalten. Neue Kontaktdaten können im Prinzip auch direkt in der `addressbook` Datei mit einem Texteditor hinterlegt werden.

Der Aufbau ist wiefolgt:

    [<Identifkationsnummer 1>]
    <Interer Feldname 1> = <Wert 1>

    ...

    [<Identifkationsnummer n>]
    <Interer Feldname n> = <Wert n>

Wer nur nach Namen suchen möchte, braucht jetzt keine Pipes mit grep usw. legen. Das geht auch einfacher mit abook selbst:

    abook --mutt-query Richard

Wie man schon sieht ist die Anbindung an [mutt](https://neomutt.org) eine eingebaute Idee.


# Bedienung

Die Bedienung ist sehr einfach und an die Tastenkürzel des [vi](https://en.wikipedia.org/wiki/Vi) angelehnt:

* <kbd>j</kbd> - (Übersicht, Kontaktbearbeitung) einen Kontakteintrag nach unten
* <kbd>k</kbd> - (Übersicht, Kontaktbearbeitung) einen Kontakteintrag nach oben
* <kbd>h</kbd> - (Kontaktbearbeitung) eine Sicht nach links
* <kbd>l</kbd> - (Kontaktbearbeitung) eine Sicht nach rechts
* <kbd>/</kbd> - (Übersicht) Suche nach Kontakten über Suchbegriff
* <kbd>Enter</kbd> - (Übersicht) in die Kontaktbearbeitung wechseln
* <kbd>q</kbd> - (Kontaktbearbeitung) in die Übersicht wechseln
* <kbd>w</kbd> - (Übersicht) die Kontaktliste speichern

Für mehr Information einfach <kbd>?</kbd> in der Übersicht tippen.

# Integration in xbindkeys

Nun darf natürlich die Integration in xbindkeys bzw. eigentlich die Integration in die tägliche Arbeit nicht fehlen. Dafür wird in dom0 am besten ein Tastenkürzel für die Applikation gewählt. Bei mir ist das `Mod4` + `F7` und somit lautet mein Eintrag in der `~/.xbindkeysrc` in dom0:

    "qvm-run email '/usr/bin/xterm -title "neomutt" -e neomutt'"
      Mod4 + F7

Wie die Integration in mutt selbst aussieht, werden wir in einem der nächsten Beiträge sehen.

# Weiterführendes

Die man Seite ist hervorragend gepflegt. Die meisten Dinge innerhalb dieses Blog-Eintrags stehen dort ebenso und natürlich noch genauer. Die eigentlichen Seiten:

    man abook # Handbuch zur Applikation
    man abookrc # Handbuch zur Konfiguration

Ich wünsche viel Spaß mit der schnellen Alternative zu Thunderbird & Co!

