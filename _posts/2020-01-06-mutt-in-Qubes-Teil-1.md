---
layout: post
title:  mutt in Qubes - Teil 1
author: Richard Bäck
---

Schon einmal von [mutt](https://en.wikipedia.org/wiki/Mutt_(email_client)) gehört? mutt ist eine E-Mail Applikation die vollständig über eine Curses-Oberfläche im Terminal bedient wird. Hört sich befremdlich an, bietet aber viele Vorteile. Denn die gesamte Oberfläche kann mit der Tastatur allein bedient werden. Somit erspart man sich lästige Klicke. Doch was noch mehr ins Gewicht fällt - ins besondere in Qubes - ist der geringe Rechnerleistungsaufwand für mutt. Während beim Laden der Fenster in Thunderbird schon einige Sekunden vergehen können öffnet mutt sich selbst, die Mails und auch die verschiedenen Verzeichnisse blitzschnell.

Diese Geschwindigkeit und Mausfreiheit kostet allerdings. Und zwar Komfort und Funktinalität. Anders als Thunderbird ist mutt (eigentlich) nur eine Verwaltung einer [MBOX](https://de.wikipedia.org/wiki/Mbox) oder eines [Maildirs](https://de.wikipedia.org/wiki/Maildir). Mails empfangen (!), ein Kalendar oder gar eine Abarbeitungsliste sind nicht enthalten. Das ist kein Welteruntergang, denn dafür gibt es andere Applikationen - fein nach der [Unix-Philosophie](https://de.wikipedia.org/wiki/Unix-Philosophie).

In dieser Reihe von Blog-Einträgen erkläre ich wie man mutt erfolgreich unter Qubes verwenden kann. Allerdings sind die meisten Beschreibungen nicht Qubes spezifisch, sondern gelten für fast alle Distributionen. In diesem ersten Eintrag beschreibe ich die Architektur und die Installationen der einzelnen Applikationen. Die darauffolgenden Einträge werden jeweils die einzelnen Applikationen und deren Einrichtung beschreiben.

# Vorraussetzungen

Um diese Anleitungen und auch die nächsten erfolgreich bestreiten zu können, müssen folgende Vorraussetzunge erfüllt sein:
* Fertige Qubes Installation
* Basis-Wissen über Qubes
* Basis-Wissen über Linux
* Basis-Wissen über Bash
* Basis-Wissen über die E-Mail Architektur und Bedienung ([SMTP](https://de.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol), [IMAP](https://de.wikipedia.org/wiki/Internet_Message_Access_Protocol) und [POP](https://de.wikipedia.org/wiki/Post_Office_Protocol) sollten keine Fremdwörter sein)

# Die Architektur

Nachfolgend ist die Architektur dargestellt mit der mutt betrieben werden kann. Es werden folgende Programme benötigt:
* mutt
* [abook](https://abook.sourceforge.net/) - Eine Kontakt Verwaltung mit einer Curses-Oberfläche
* [calcurse](https://www.calcurse.org/) - Eine Kalendar-Applikation mit einer Curses-Oberfläche
* [msmtp](https://marlam.de/msmtp/) - Kommandozeilen SMTP Klient (versendet Mails)
* [getmail](http://pyropus.ca/software/getmail/) - Kommandozeilen IMAP und POP Klient (empfängt Mails)
* [split-gpg](https://www.qubes-os.org/doc/split-gpg/) - Qubes spezifische sichere Ablage der GPG-Schlüsseln in einer eigens dafür vorhergesehenen VM


![Architektur](/assets/mutt-architektur.png)

Alle Programme (außer der splig-gpg Server) laufen in einer einzigen VM, die auf [Whonix Workstation](https://www.whonix.org/) basiert und somit auf Debian.

# POP vs IMAP

Mit IMAP werden (zumindest Kopien) der E-Mails ständig am Mailserver gehalten. Wenn also am Mailserver Daten gestohlen werden, dann könnten auch die eigenen E-Mails betroffen sein.

Werden die E-Mails regelmäßig mit POP abgerufen und am Mailserver entfernt, dann gibt es nichts zu stehlen. Das ist vielleicht nicht so komfortabel mit mehreren Geräten, allerdings sicherer. Bitte bedenken: so lange das Qubes-Gerät die E-Mails nicht abruft liegen sie am Mailserver. Somit sind sie bis dahin auch auf mobilen Geräten vorhanden!

Wegen der Begründung oben wird in der Anleitung nur der POP-Weg erklärt.

# VMs einrichten

## Whonix installieren

Wenn Whonix nicht während der Qubes Neuinstallation mitinstalliert wurde, dann kann das jederzeit im nachhinein nachgeholt werden. Um keine Informationen zu duplizieren verweise ich hier nur auf die [offizielle Installationsanleitung](https://www.whonix.org/wiki/Qubes/Install#Installation).

## Split-GPG aktivieren

Auch für die Split-GPG Funktionalität gibt es eine ausführliche [offizielle Installationsanleitung](https://www.qubes-os.org/doc/split-gpg/#configuring-split-gpg).

## Calcurse

Die Version von calcurse in Debian 10.2 ist hoffnungslos veraltet. Um die neueste Version zu erhalten muss sie selbst kompiliert und ein Paket dafür erstellt werden. Die Beschreibungen der Vorgänge können in einer Fedora-basierten VM durchgeführt werden. Bevor fortgefahren werden kann, muss fpm installiert werden. Hierfür die [Anleitungen eines älteren Eintrags](/2019/12/23/Pakete-fuer-Fedora-erzeugen-leicht-gemacht.html#installation) befolgen.

Dem herunterladbaren Tarball ist eine Signatur hinterlegt, daher zuerst einmal den Schlüssel importieren:

    cd ~/
    wget https://pgp.key-server.io/download/0xA91764759326B440
    qubes-gpg-import-key 0xA91764759326B440 # Importiert den Schlüssel mit Split-GPG
    rm 0xA91764759326B440

Danach den Tarball herunterladen und verifizieren:

    wget https://www.calcurse.org/files/calcurse-4.5.1.tar.gz.asc
    wget https://www.calcurse.org/files/calcurse-4.5.1.tar.gz
    qubes-gpg-client --verify calcurse-4.5.1.tar.gz.asc calcurse-4.5.1.tar.gz # Verifiziert mit Split-GPG

calcurse benötigt die Bibliothek ncurses. Normalerweise ist diese am System vorhanden, allerdings nicht als Entwicklungspaket. Das kann man folgendermaßen nachholen:

    sudo dnf install -y ncurses-devel

Endlich kanns ans kompilieren gehen:

    tar xf calcurse-4.5.1.tar.gz
    cd calcurse-4.5.1.tar
    rm -rf ~/wurzel
    mkdir -p ~/wurzel/usr
    ./configure --prefix=$HOME/wurzel/usr
    make install
    cd ~/wurzel
    fpm -s dir -t deb -n calcurse -v 4.5.1 usr

Das erstellte Debian Paket kann nun in die Whonix-WS-Vorlage kopiert werden.

## Applikationen installieren

Nach der erfolgreichen Einrichtung von Whonix und Split-GPG können in einem Terminal der Whonix-WS-Vorlage die benötigten Applikationen installiert werden:

    sudo dpkg -i /Pfad/zu/calcurse_4.5.1_amd64.deb # Aus dem vorherigen Kapitel
    sudo apt install -y abook msmtp getmail


