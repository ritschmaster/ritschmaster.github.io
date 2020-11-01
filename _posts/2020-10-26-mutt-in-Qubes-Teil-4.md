---
layout: post
title:  mutt in Qubes - Teil 4 - pass
author: Richard Bäck
---

Bevor es weiter geht brauchen wir noch einen sehr wichtigen Helfer: [pass](https://en.wikipedia.org/wiki/Pass_(software)). Dieser wird benötigt um den weiteren Applikationen eine Möglichkeit zu geben ein Passwort für das E-Mail Konto zu hinterlegen und zu verwenden.

# Das Prinzip von pass

pass ist sehr simpel. Es gibt Verzeichnisse und Passwörter. Verzeichnisse sind gewöhnliche Verzeichnisse und Passwörter gewöhnliche Dateien im Dateisystem. Die Passwörter werden mit GPG verschlüsselt abgelegt. Das Wurzelverzeichnis von pass ist standardmäßig `~/.password-store`.

Die Passwortdateien erlauben es nicht nur das Passwort selbst, sondern auch weitere Daten zu speichern. Diese zusätzlichen (Meta)-Daten zu dem Passwort sind ebenso verschlüsselt, allerdings wenn das Passwort in die Zwischenablage kopiert wird, dann wird nur das Passwort selbst und nicht die (Meta)-Daten kopiert.

Ein weiterer Vorteil von pass ist, dass seine Existenz es anbietet Passwörter vollautomatisch in Shell-Skripten zu verwenden. D.h. keine lästigen Passwortaufforderungen mehr oder gar das Passwort ungeschützt in eine Klartext-Datei hinterlegen. Das ist um so komfortabler, da viele Terminal-Applikationen auch in deren Konfigurationen eine Syntax anbieten um ein Passwort über eine andere Applikation zu bekommen. Diese Funktionalität werden wir in den nachfolgenden Teilen sehen.

# Installation

Einmal kurz die Whonix-WS-Vorlage starten und dort in einem Terminal das folgende eintippen:

    sudo apt install -y pass
    
und schon ist pass installiert!


# Die wichtigsten Befehle

1. `pass insert <Pfad zum Passwort>` - Einfügen eines neues Passworts. Das Passwort wird explizit abgefragt.
2. `pass -c <Pfad zum Passwort>` - Kopieren des Passworts in die Zwischenablage. Es kann danach zB in den Browser eingefügt werden.
1. `pass edit <Pfad zum Passwort>` - Editierung des Passworts mit Hilfe eines Texteditors.
1. `pass show <Pfad zum Passwort>` - Ausgabe des Passworts als Klartext im Terminal

# Meine Kategorisierungsstrategie

Um meine Passwörter wieder zu finden gibt es mehrere Strategien. Meine ist sehr Verzeichnis- und Buchstaben-hungrig, dafür muss ich beim Suchen der Passwörter weniger nachdenken. Die Strategie ist ein Baum. Jede Ebene ist ein Verzeichnis und die Blätter die tatsächlichen Passwörter. Meta-Daten werden auch als "Passwörter" in eigenen Blättern gehalten. Die verschiedenen Ebenen des Baums:

1. Grobe Kategorie des Passworts (zB Banking oder IT)
2. Der Dienst (zB Github)
3. Ein leicht erkennbares Pseudonym des Benutzers (zB Richard Bäck). Das ist sinnvoll, wenn auch Passwörter für Familienmitglieder gespeichert werden sollen.
4. Das eigentliche Passwort in der Datei "pass". Der Benutzer in der Datei "user". Der Link (falls vorhanden) zu dem Dienst in "url". Jeweils verschlüsselt. Das erlaubt ein einfaches Kopieren der Information direkt mit `pass -c`.

Somit erhalte ich z.B. meinen Github Benutzer unter `pass -c IT/Github/Richard\ Bäck/user`. Neben dem Vorteil sich leichter an die Passwörter zu erinnern ist, erhält man auch wesentlich schneller das Passwort zu einem Benutzer. Es reicht der folgende Bash-Trick: `^user^pass`. Dieser ersetzt alle "user" Zeichenketten des letzten Kommandos mit der Zeichenkette "pass" und führt das generierte Kommando sofort aus. Somit erhält man automatisch `pass -c IT/Github/Richard\ Bäck/pass`.



