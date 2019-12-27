---
layout: post
title:  Thunderbird Kontakte zu abook konvertieren
author: Richard Bäck
---

Mit [abook](https://abook.sourceforge.net/) erhält man die Möglichkeit seine Kontakte mit einer Curses-Oberfläche im Terminal zu pflegen. abook alleine ist schon Klasse, da man auf jeden Fall ohne Ladezeiten in einem Fluss seine Kontakte suchen und pflegen kann. Noch besser allerdings abook kann in [mutt](http://www.mutt.org/) als Anbieter für E-Mail Adressen eingebunden werden!

Doch was hilft das einem, wenn man bereits Thunderbird verwendet? In erster Linie nichts und wenn man wechseln möchte, dann wäre es natürlich mehr als super, wenn man die Kontakte von Thunderbird auch in abook verwenden kann. Das ist möglich!

# Die Konfiguration

abook lebt in `~/.abook`. Dort legt es die folgenden Dateien ab:
* `abookrc` - Die Konfiguration
* `addressbook` - Die eigentlichen Kontakte im Klartext

In der `abookrc` kann man neben generellen Applikationseinstellungen auch zusätzliche Felder definieren und angeben auf welchem Reiter die Felder platziert werden.

Sollte man abook bereits im Einsatz haben, dann bitte die bestehende Konfiguration sichern (am besten mit `mv ~/.abook ~/.abook.bak`).

In `~/.abook/abookrc` folgende Zeilen einfügen, damit man zumindest genau so viele Felder hat, wie Thunderbird:

    field birthday = Birthday, date
    field firstname = Firstname, string
    field lastname = Lastname, string
    field pager = Pager, string
    field url2 = URL2, string
    field workcountry = WorkCountry, string
    field workstate = WorkState, string
    field workzip = WorkZIP, string
    field workcity = WorkCity, string
    field workaddress = WorkAddress, string
    field workaddress2 = WorkAddress2, string
    field lists = Lists, list


    view CONTACT = name, lastname, firstname, email, lists
    view ADDRESS = country, state, zip, city, address, address2, workcountry, workstate, workzip, workcity, workaddress, workaddress2
    view PHONE = phone, workphone, mobile, fax, pager
    view OTHER = birthday, nick, url, url2, notes, anniversary

    set use_colors = true

# Das Konvertierungsskript

abook hat nun die benötigten Felder. Was fehlt sind die Kontakte. Dafür habe ich das Python-Skript [tbcsv2abook.py](/assets/tbcsv2abook.py) geschrieben. Um es zu benutzen muss Python 3 installiert sein. Unter Fedora geht das sehr einfach:

    sudo dnf install -y python3

Die Installation des Skripts kann im Heimverzeichnis erfolgen:

    mkdir -p ~/.local/bin
    wget -O ~/.local/bin/tbcsv2abook.py https://ritschmaster.github.io/assets/tbcsv2abook.py
    chmod u+x ~/.local/bin/tbcsv2abook.py
    echo 'export PATH="~/.local/bin:$PATH"' >> ~/.bashrc # Optional sollte ~/.local/bin noch nicht im Pfad sein

# Die Konvertierung

Nachdem nun abook eingerichtet und tbcsv2abook.py installiert ist, kann nun die Konvertierung erfolgen.

Dafür werden zuerst die Kontakte in eine CSV exportiert:

1. Thunderbird öffnen
2. Zuerst die Sprache in *English (United States)* ändern unter *![Optionen](/assets/thunderbird_optionen.jpg) > Einstellungen > Einstellungen > Erweitert > Allgemein*
3. Thunderbird neustarten
4. Ins *Address book* wechseln
3. Das zu exportierende Adressbuch auswählen (z.B. *All Address Books*)
4. *Tools > Export...*
5. Als Speicheroption *Comma Seperated (UTF-8)* auswählen und als `~/tbaddresses.csv` speichern

Und nun kann konvertiert werden:

    cat ~/tbaddresses.csv | tbcsv2abook.py > ~/.abook/addressbook
