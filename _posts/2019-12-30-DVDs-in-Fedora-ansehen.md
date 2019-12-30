---
layout: post
title:  DVDs in Fedora ansehen
author: Richard Bäck
---

Letzte Woche wollte ich zu den Feiertagen eine gute alte DVD ansehen. Leider bin ich wieder einmal angestanden, da der letzte DVD-Abend schon länger als die letzte Fedora-Installation her ist. Diesmal löse ich das Problem ein für alle mal und vor allem auch sauber mit fpm!

# Hintergrund

Um unter Linux gekaufte DVDs ansehen zu können wird eine eigene Applikation/Bibliothek benötigt und zwar [libdvdcss](https://de.wikipedia.org/wiki/Libdvdcss). Diese Applikation umgeht den Kopierschutz um die DVD lesen zu können. Die Umgehung des Kopierschutzes ist allerdings ein patentrechtlich geschützter Algorithmus. Dieser Umstand hatte dazu geführt, dass die meisten Distributionen (inkl. Fedora und Debian) die Applikation nicht offiziell als Paket anbieten. Ärgerlich, insbesondere für Linux-Neulinge.

# Distanzierung

Wenngleich ich das Urheberrecht und auch Patente als ein Meme befinde, bin ich mir sehr wohl über die ernsten Folgen von deren Bruch bewusst. Deshalb distanziere ich mich klarerweise von jeder kriminellen Nutzung von libdvdcss und beschränke mich rein darauf wie man selbst **gekaufte** DVDs unter Linux ansehen kann.

# libdvdcss in Debian installieren

Obwohl Debian libdvdcss nicht offiziell anbietet kann es dort sehr einfach installiert werden, denn [deb-multimedia](https://deb-multimedia.org/) bietet das Paket an. Wer der dortigen Installationsanleitung für das Repository folgt und danach ein `apt install lidvdcss` absetzt hat das Problem bereits gelöst.

# libdvdcss in Fedora installieren

## livna

Die einfache Option ist die Installation über das Repository von [livna](https://rpm.livna.org).

Es gibt allerdings zwei Probleme:
1. Zum Datum der Erstellung dieses Blog-Eintrags bietet livna nur libdvdcss 1.4.0 (vom 2015-12-16) an. Die aktuelle ist 1.4.3 (vom 2019-10-13).
2. Ich hab nirgendwo eine offizielle Aussage über den verwendeten GPG Schlüssel von livna gefunden. Da das Repository kein HTTPS anbietet, ist das auf jeden Fall ein Sicherheitsrisiko.

## Manuell

Die schwierige Option ist die Kompilierung der aktuellsten libdvdcss Version und die Erstellung eines Pakets daraus. Dafür werden zwei Verzeichnisse benötigt: `~/wurzel` und `~/libdvdcss`.

### Vorbereitungen

Bevor man überhaupt irgendwas machen kann müssen die Abhängigkeiten zur Kompilierung installiert werden:

    sudo dnf install -y git gcc make autoconf automake libtool

Danach können die Abhängigkeiten zur Paketerstellung installiert werden. Bitte dafür den [Installationsteil dieses Blog-Eintrags](/2019/12/23/Pakete-fuer-Fedora-erzeugen-leicht-gemacht.html#installation) befolgen.

### Kompilierung

Um den aktuellsten Quellcode von libdvdcss zu bekommen kann folgendes Kommando abgesetzt werden:

    git clone https://code.videolan.org/videolan/libdvdcss.git ~/libdvdcss

Nun mit Hilfe von git zum Commit der letzten Version wechseln:

    cd ~/libdvdcss
    git checkout $(git tag | grep v -v | tail -n 1)

Endlich kann man kompilieren (und installieren):

    mkdir -p ~/wurzel/usr
    autoreconf -i
    ./configure --prefix=$HOME/wurzel/usr
    make
    make install

### Paket erstellen

Die installierten Dateien liegen in `~/wurzel` bereit. Wichtig: das Paket hat eine Abhängigkeit auf libdvdread, da diese Applikation/Bibliothek libdvdcss in VLC und andere Video-Spieler einbindet. Somit bringt libdvdcss ohne libdvdread nichts.

Wenn das Zielsystem für das Paket eine [x64](https://de.wikipedia.org/wiki/X64) Maschine ist, dann muss
1. die [Kompilierung](#kompilierung) natürlich auch für x64 durchgeführt werden
2. das Kommando `mv ~/wurzel/usr/lib ~/wurzel/usr/lib64` nach der Installation abgesetzt werden, damit die installierten Bibliotheken verwendet werden können.

Das Paket kann mit dem folgenden Kommandos erstellt werden:

    cd ~/wurzel
    fpm -s dir -t rpm -n libdvdcss -v $(cd ~/libdvdcss && git tag | grep v -v | tail -n 1) -d libdvdread usr

Das Paket wurde in `~/wurzel` erstellt und kann nun am System mit `dnf install` installiert werden!
