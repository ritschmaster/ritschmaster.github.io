---
layout: post
title:  mutt in Qubes - Teil 2 - xbindkeys
author: Richard Bäck
---

In Teil 1 habe ich gezeigt was die Grundidee ist, wie die Architektur aussieht und wie man die benötigten Applikationen installiert. Bevor es weiter geht mit den einzelnen Applikationen ist noch ein weiteres wichtiges Helferlein an der Reihe: [xbindkeys](https://www.nongnu.org/xbindkeys/xbindkeys.html).

Diese Terminal-Applikation erlaubt es hinter beliebige Tastenkombinationen, beliebige Systemkommandos zu hinterlegen. Es arbeitet dabei komplett unabhängig zum eingesetzten Fensterverwalter. Das erlaubt es somit die Tastenkombinationen einmal zu pflegen und diese dann in den verschiedenstenen Umgebungen wiederzuverwenden: i3, GNOME, dwm, ...

Die einzige Abhängigkeit ist ein laufender X Org. Server, welchen zum Glück die meisten Linux-Desktop Benutzer ohnehin haben. Insbesondere, da Wayland (noch) nicht offiziell das X Window System obsolet gesetzt hat.

# Die Installation

In Qubes ist die Installation leicht erledigt. Tastenkombinationen sind in dom0 relavant, da nur dom0 jederzeit auf die Tastenkombinationen horchen kann. Daher in domß folgendes Kommando absetzen:

    sudo qubes-dom0-update xbindkeys

Und schon kann man loslegen!

# Die Konfiguration

Der Aufbau der Konfigurationsdatei ist sehr simpel gehalten. Das schwierigste daran ist sich zu merken, dass mit Mod1 die Alt-Taste und mit Mod4 die Super-/Windows-Taste gemeint ist. Der prinzipielle Aufbau lautet:

    # Kommentar
    "<Systemkommando>"
      <Kombination 1 Taste1> + ... + <Kombination 1 Taste n>
      <Kombination 2 Taste1> + ... + <Kombination 2 Taste n>

Die Konfiguration muss eigentlich in `~/.xbindkeysrc` platziert werden, aber um sich an die [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html) zu halten legen wir sie folgenermaßen an:

    mkdir ~/.config/xbindkeys
    xbindkeys -d > ~/.config/xbindkeys/xbindkeysrc # Befüllt die Datei mit einer Vorlage
    ln -s ~/.config/xbindkeys/xbindkeysrc ~/.xbindkeysrc

Es kann nun die Konfiguration nach seinen eigenen Bedürfnissen abgestimmt werden.

# Tastenkombinationen rausfinden

Wer sich keine Gedanken über Mod1, Mod4 und deren Freunde machen will, kann die Tastenkürzel einfach von xbindkeys aufzeichnen und ausgeben lassen. Dafür reicht das folgende im Terminal auf dom0:

    xbindkeys -mk

Damit geht ein neues Fenster auf in dem Tastenkombinationen abgesetzt werden können. Das Terminal spuckt dann die Auflistung für die Konfiguration an, die diese Tastenkombination repräsentiert.

# Beispiel

In dem Beispiel erfassen wir eine Tastenkombination, mit der wir ein Terminal in der AppVM öffnen, zu welcher das gerade fokusierte Fenster gehört. D.h. wenn wir zB gerade in mutt in der AppVM email tippen und die Tastenkombination drücken, geht ein Terminal in email auf.

Die Tastenkombination der Wahl ist `Super` + `Enter`. Die dafür benötigte Kombination ist wiefolgt:

    "qubes-i3-sensible-terminal"
        Mod4 + Return

Das abgesetzte Kommando macht alles für uns, da es von den Qubes-Entwicklern extra für die Verwendung innerhalb des i3-Fensterverwalters bereitgestellt wurde. Um die Tastenkombination erfolgreich absetzen zu können muss allerdings vorher folgendes in dom0 installiert werden:

    sudo qubes-dom0-update i3-settings-qubes

Und ab sofort kann beliebig ein Terminal geöffnet werden. Auch in XFCE!
