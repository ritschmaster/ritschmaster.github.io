---
layout: post
title:  Thunderbird Mails zu Maildir konvertieren
---

Thunderbird verwendet intern standardmäßig das [MBOX](https://de.wikipedia.org/wiki/Mbox). Das ist sehr unangenehm, wenn man von Thunderbird zu Terminal Programmen (wie zB mutt oder Emacs) wechseln möchte und die Vorteile von [Maildir](https://de.wikipedia.org/wiki/Maildir) genießen möchte. Denn dafür müssen zuerst die einzelnen Mailverzeichnisse in Thunderbird - die intern als MBOX gehalten werden - zu Maildirs konvertiert werden.

Glücklicherweise bietet Thunderbird die Einstellung an, dass die nächsten angelegten, neuen Konten mit Maildir verwaltet werden, anstatt mit MBOX. Diese Möglichkeit kann man ausnutzen um sehr einfach mit Thunderbird selbst die Konvertierung durchzuführen. Folgende Schritte führen hier zum Erfolg:

1. Thunderbird öffnen
2. Wechseln zu *![Optionen](/assets/thunderbird_optionen.jpg) > Einstellungen > Einstellungen > Erweitert > Allgemein*
3. Bei *Speichermethode für neue Konten* die Option *Eine Datei pro Nachricht (maildir)* auswählen
4. Wechseln zu *![Optionen](/assets/thunderbird_optionen.jpg) > Einstellungen > Konten-Einstellungen*
5. Über *Konten-Aktionen > Feed-Konto hinzufügen* ein neues Konto für RSS-Feed hinzufügen. Dieses Konto verwendet nun automatisch das Maildir-Format. Das Konto kann einen beliebigen Namen haben. Zur Nachvollziehbarkeit verwende ich hier nun den Namen **Konvertierung**.
6. Einen neuen Ordner namens **Konvertiert** innerhalb von **Konvertierung** erstellen.
7. Jetzt die Mails eines zu konvertierenden Verzeichnis in **Konvertiert** hineinschieben/kopieren.
8. Die Konvertierung ist in dem Moment abgeschlossen, in dem die Mails in dem Verzeichnis landen. Das Ergebnis kann nun im Dateiverzeichnis `~/.thunderbird/*.*/Mail/Feeds/Konvertiert` gefunden werden.
9. Bevor das in 8. genannte Verzeichnis verwendet werden kann, sollte noch in `~/.thunderbird/*.*/Mail/Feeds/Konvertiert` das Verzeichnis `new` angelegt werden. Damit wird es ein vollständiges Maildir und kann nun ohne Probleme in Programmen wie mutt verwendet werden.

