---
layout: post
title:  Pakete für Fedora erzeugen - leicht gemacht
author: Richard Bäck
---

Jeder Linux Benutzer kennt das: man sucht/findet eine super klasse Applikation, möchte sie gerne installieren, es gibt nur leider kein Paket im Distro eigenen Repository.

Nun kann man mehrere Wege beschreiten:
1. Nach Repositories in [COPR](https://copr.fedorainfracloud.org/) oder beim Hersteller der Applikation suchen.
2. Den [Tarball](https://de.wikipedia.org/wiki/Tar_(Packprogramm)) vom Hersteller herunterladen und per `make install` im eigenen System installieren.

Die 1. Option ist natürlich angenehmer, da man alle Vornehmlichkeiten der Paketverwaltung weiter genießen kann. Aber was ist, wenn nur die 2. Option über bleibt? Was wenn man selber ein kleines Skript oder Skripte-Sammlung installieren möchte? Tarballs sind da nicht unbedingt die besten Helfer. Denn zur Löschung der zuvor installierten Dateien wird das Makefile der Installation benötigt um ein `make uninstall` absetzen zu können.

Doch für genau solche Problemstellungen gibt es die Applikation [fpm](https://github.com/jordansissel/fpm). Mit der kann man für Debian, Fedora und weitere Distros aus Verzeichnissen (und andere Quellformate) sehr einfach Pakete erzeugen.

# Installation

Um auf Fedora fpm benutzen zu können, müssen zuerst die Abhängigkeiten systemweit installiert werden:

    sudo dnf install -y ruby ruby-devel gem rpm-build

fpm selbst wird danch über Gem im Heimverzeichnis installiert:

    gem install fpm


# Paket erzeugen

Ich gehe hier nur auf das einfachste Quellenformat ein: das Verzeichnis. Bei diesem Quellenformat werden beliebige Verzeichnisse und Dateien in ein Paket gestopft und können später installiert (und auch wieder gelöscht!) werden. Dabei werden die beliebigen Verzeichnisse und Dateien später unter der Wurzel `/` platziert.

Das benötigte Kommando lautet:

    fpm -s dir -t rpm -n <Paketname> -v <Version> -d <AbhängigesPaket1> -d <AbhängigesPaket2> <Verzeichnis1> <Datei1> ...

## Paket aus Tarball erstellen

Je nach Applikation könnte die Installation aus einem Tarball variieren. Wie die Installation genau stattfindet ist meistens ohnehin in der beigelegten README beschrieben. Als Beispiel dient hier [GNU hello](https://ftp.gnu.org/gnu/hello/hello-2.10.tar.gz). Das verwendet die [GNU autotools](https://de.wikipedia.org/wiki/GNU_Build_System), bei dem das Installationsprozedere standardisiert ist.

Zuerst den Tarball entpacken und hinein wechseln:

    cd ~/ # Ins Heimverzeichnis wechseln
    wget https://ftp.gnu.org/gnu/hello/hello-2.10.tar.gz # GNU Hello herunterladen
    tar xf hello-2.10.tar.gz
    cd hello-2.10

Danach kompilieren und installieren:

    mkdir -p wurzel/usr # Dient als Installationsziel
    ./configure --prefix=$HOME/wurzel/usr # Die Applikation soll später im Userland landen
    make install

Somit wurde GNU hello in `~/wurzel/usr` installiert. Um nun ein Paket für Fedora zu erzeugen muss folgendes Kommando abgesetzt werden:

    cd ~/wurzel
    fpm -s dir -t rpm -n hello -v 2.10 usr

Das Paket wird im gleichen Verzeichnis erstellt und kann sofort installiert werden:

    sudo dnf install -y hello-2.10-1.*.rpm
    hello # sollte nun mit 'Hello, world!' antworten
    man hello # auch das GNU hello Handbuch sollte installiert worden sein

## Paket für eigenes Skript erstellen

Nehmen wir an, wir haben unter `~/helloworld` folgenden Verzeichnisbaum:

    usr
      bin
        helloworld.sh
      share
        helloworld
	  helloworld.sh


Die Datei `usr/bin/hellworld.sh` ist eigentlich ein symbolischer Link, der auf die Datei `../share/helloworld/helloworld.sh` zeigt. Hier ist die Angabe des relativen Pfads wichtig, da später die Dateien/Verzeichnisse unter `/` landen. Daher würde später ein Link nach `~/helloworld/usr/share/helloworld/helloworld.sh` ins Leere zeigen und somit nicht für jeden Benutzer korrekt sein (Datei wurde ja wo anders hin installiert).

Die Datei `/usr/share/helloworld/helloworld.sh` hat die Berechtigungsmaske 755. Außerdem ist nachfolgend ihr Inhalt:

    #!/bin/bash

    echo "Hello world!"

Wenn man sich nun mit `cd` in das Verzeichnis `~/helloworld` hinein begibt, erhält man folgendermaßen ein RPM Paket für Fedora:

    fpm -s dir -t rpm -n hellworld -v 0.1 -d bash usr

Das Paket wird im gleichen Verzeichnis erstellt und kann ohne weiteres verteilt und installiert werden.


