---
layout: post
title:  org-mode für Emacs Dummys
author: Richard Bäck
---

org-mode ist das perfekte Werkzeug für Entwickler um deren täglichen Aufgaben zu erfassen. Warum? Jede Aufgabe wird als Klartext verfasst. Kein XML. Keine GUI. Nichts zwischen einem selbst und der Notiz/der Aufgabe. Das ist gerade in der Entwicklungsbranche ein Segen. Da großartiger Formattierungs-Schnick-Schnack mehr Zeit frisst als Vorteile bringt. Und wenn dann ein Umzug eines Konto notwendig ist, dann sind die Notizen entweder weg oder müssen im schlimmsten Fall mit einem Einmal-Werkzeug nach einer Google-Runde migriert werden.

So etwas macht keinen Spaß. Einfach seine Aufgaben erfassen, diese immer mit sich haben und dann durchstreichen - das macht Spaß. Fast wie mit Zettel.

Tatsächlich habe ich noch bis vor 1,5 Jahren alles auf Zettel nieder geschrieben. Die warteten brav jeden Tag im Büro auf mich. Als dann die Ausgangssperren verhängt wurden, stand ich auf einmal ohne meine Zettel da, da die ja noch im Büro waren. Deshalb zwang ich mich tatsächlich alles am Laptop mitzuschreiben. Das Ergebnis hat mich selbst positiv überrascht. Es macht nicht nur mehr Freude Tätigkeiten zu erfassen, ich hab auch die Vorteile eines Erinnerungsassistenten und die Möglichkeit einer Zeittafel.

Doch ich hab bereits viel Erfahrung mit Emacs gehabt. Und org-mode hab ich auch schon sporadisch in der Vergangenheit benutzt. Ist org-mode für Emacs Dummys überhaupt was? Meiner Meinung nach schon. Lies weiter und entscheide für dich selbst.

In den nächsten paar Schritten erkläre ich, wie du Emacs zum Laufen bekommst und wie du org-mode bedienst. Es ist das absolute Minimum um zu Wissen, wie's geht.

Wenn dir die Schritte nicht schwer fallen, dann empfehle ich das Resultat für eine Woche in ein tägliches Leben einzubauen. Nur diese Anleitung zu lesen, wird dich höchst wahrscheinlich nicht überzeugen. Es auszuprobieren jedoch schon!

# Installation von Emacs

Du bist wahrscheinlich in Windows gefangen. Aber fürchte dich nicht! Emacs kann sehr einfach unter Windows verwendet werden. Sogar mit fast all seinen Vorteilen (Linux Shells!). Wie du Emacs unter Windows installieren kannst hab ich in [einem meiner führeren Einträge](/2021/06/13/Using-telga-in-Windows-10.html) bereits beschrieben.

# Emacs öffnen

Im Startmenü nach __Msys2 MinGW 64-bit__ suchen und öffnen. Das öffnet ein Terminal. Dort kann mit

    emacs

Emacs gestartet werden. Wenn dir das offene Terminal genauso am Keks geht wie mir, dann nimm lieber

    emacs & disown
    
Das startet Emacs als separaten Prozess. Damit kann das Terminal mit Tastenkombination <kbd>Ctrl-D</kbd> [geschlossen werden](https://en.wikipedia.org/wiki/End-of-Transmission_character#Meaning_in_Unix).

Schlussendlich lacht uns Emacs an.

![Lachendes Emacs](/assets/org-mode_fuer_emacs_dummys/1_open_emacs.png)


# CUA für Emacs (Optional)

Da diese Anleitung ja nicht für Emacs Puristen, sondern für absolute Dummys ist, kann es durch sein, dass die Sandard Tastenbelegungen etwas befremdlich wirken. Das gilt es zu vermeiden!

Als nächstes schaltest du nun also den [CUA](https://de.wikipedia.org/wiki/Common_User_Access)-Mode ein. Damit funktionieren dann die allseits bekannten Tastenkürzel <kbd>Ctrl-c</kbd>, <kbd>Ctrl-x</kbd> und <kbd>Ctrl-v</kbd> wie sie aus anderen Applikationen bekannt sind. In Standard Emacs wäre sonst das Kopieren eins Selektierten Texts zB <kbd>Alt-w</kbd>.

Dafür klickst du auf den Menü-Eintrag _Options > Customize Emacs > Specific Option_. Danach folgendes eingeben:

![CUA Customizing](/assets/org-mode_fuer_emacs_dummys/2_customize_cua.png)

Mit einem Klick auf "Toggle" wird der CUA-Mode eingeschaltet. Damit das auch so bleibt nun auf "State" klicken und "Save for Future Sessions" auswählen.


# org-mode Customizing

Bevor du loslegen kannst mit dem Erstellen von ToDos musst du die Agenda konfigurieren. Das absolute Minimum des Agenda Customizings ist die Bekanntgabe, welche Dateien gelesen und in der Agenda dargestellt werden.

Um das festzulegen klicken wir als Ersters auf den Menü-Eintrag _File > Visit New File_ und wählen `~/.emacs`. An der obersten Stelle der Datei fügst du 

    (require 'org)
    
ein. Damit wird beim Start von Emacs auch der org-mode geladen. Nach einem Neustart von Emacs ist nun der org-mode geladen.

Somit kannst du nun wieder mit *Options > Customize Emacs > Specific Option* ein bestimmtes Customizing setzen. Dieses Mal ist es `org-agenda-directory`. Diesemal wird allerdings nicht ge-"toggle"d, sondern hier gibst du ein Verzeichnis an. Und zwar das Verzeichnis in dem du normalerweise deine Agenda Dateien versteckst. Natürlich musst du dieses Verzeichnis vorher auch anlegen! Absschluss wieder *State > Save for Future Sessions* klicken.

Nun gibst du Emacs bekannt, welche Dateien tatsächlich auch in der Agenda platziert werden. Dafür wählst du *Options > Customize Emacs > Specific Option* mit `org-agenda-files`. Wieder ist eine andere Eingabemaske da. Die ist aber sehr einfach. Mit einem Klick auf *INS* wird eine Zeile für eine Datei hinzugefügt und mit *DEL* wieder gelöscht. 

![Agenda Dateien setzen](/assets/org-mode_fuer_emacs_dummys/4_set_agenda_files.png)

Beispielsweise kannst du hier die folgende Struktur verwenden:
1. `~/Documents/org-mode/tasks.org` für ToDos
2. `~/Documents/org-mode/appointments.org` für Termine
3. `~/Documents/org-mode/notes.org` für Notizen

Nun ein letztes Mal *State > Save for Future Sessions* klicken.

Damit es später keine Probleme gibt, erstellen wir die angegebenen Dateien vorsichtshalber. Dafür verwendest du am einfachsten die in Emacs eingebaute Schnittstelle zur Shell über *Tools > Shell Commands > Shell Command...*

Hier einfach den folgenden Befehl eintippen:

    touch ~/Documents/org-mode/tasks.org ~/Documents/org-mode/appointments.org ~/Documents/org-mode/notes.org
    
![Agenda Dateien anlegen](/assets/org-mode_fuer_emacs_dummys/5_create_agenda_files.png)

# Erste ToDos

Jetzt geht es endlich los mit dem Erstellen von ToDos und so weiter. Mittels *File > Visit New File* öffnest du die Datei `~/Documents/org-mode/tasks.org` und kannst dir deine aufgenommen ToDos ansehen. 

Offensichtlich gibt es noch keine. Das änderst du am besten jetzt in dem du den folgenden Text hinzufügst:

    * TODO Emacs org-mode ausprobieren
    
So weit so gut. Mit einem Eintrag weißt du, was du zu tun hast. Aber was ist, wenn die Anzahl der Einträge wächst? Dafür gibt es die Agenda!

Wenn eine Datei mit der Endung `.org` offen ist, dann gibt es den Menü-Eintrag *Org*. Diesen verwendest du nun mit *Org > Agenda Command...*. 

![Mögliche Agenda-Views](/assets/org-mode_fuer_emacs_dummys/6_agenda_views.png)

Es öffnet sich eine Auswahl der möglichen Agenda-Sichten. Der einfachste View ist *Agenda and all TODOs*. Diesen wählst du aus, in dem du die Taste <kbd>n</kbd> drückst.

![Anzeige von Agenda and all TODOs](/assets/org-mode_fuer_emacs_dummys/7_agenda_and_all_todos.png)

Hurra! Du hast eine automatisch generierte Liste erhalten. Dennoch etwas zu wenig um dich tatsächlich zu organsiseren. Was ist wenn du gerne Zeitpunkte setzten möchtest, bis etwas erledigt sein soll? Dafür gibt es die verschiedenen Zeittypen!


# Zeittypen

Es gibt verschiedene Zeittypen. Ich liste alle auf und du kannst sie alle ausprobieren.

Du kannst das Resultat sofort betrachten, in dem du die Agenda aktualisierst. Wenn du in das Fenster (Emacs nennt Fenster-artige Teile innerhalb von Emacs Fenster!) der Agenda reinklickst und danach auf den Menü-Eintrag *Agenda > Rebuild buffer* klickt.

1. Ohne weitere Angabe. Ist gleichbedeutend wie ein fixer Termin. Wird erzeugt
   über *Org > Dates and Scheduling > Timestamp*, wenn der Cursor auf einem Gegenstand ist.

    ![Zeittyp: Timestamp](/assets/org-mode_fuer_emacs_dummys/8_timestamp.png)
2. Geplant. Wird erzeugt über *Org > Dates and Scheduling > Schedule Item*, wenn der Cursor auf einem Gegenstand ist.

    ![Zeittyp: Scheduled Item](/assets/org-mode_fuer_emacs_dummys/9_schedule_item.png)
3. Deadline. Wird erzeugt über *Org > Dates and Scheduling > Deadline*, wenn der Cursor auf einem Gegenstand ist.

    ![Zeittyp: Deadline](/assets/org-mode_fuer_emacs_dummys/10_deadline.png)


Du fragst dich vielleicht, wie du ein Datum eingeben kannst. Das ist sehr einfach. Es gibt zwei Möglichkeiten:
1. Mit dem Kalendar, der aufgeht
2. Mit der Tastatur
   1. Mit +\<Zahl\> kannst du den Gegenstand um \<Zahl\> Tage in die Zukunft schieben
   2. Mit -\<Zahl\> kannst du den Gegenstand um \<Zahl\> Tage in die Vergangenheit schieben

Den Zeitpunkt musst du immer mit der Tastatur im 24-Stunden Format angeben. Beispiel:
* 0:00
* 20:00
* 2:00-14:00

Die Zeitangaben sind ziemlich mächtig. Auch Wiederholungen sind damit möglich. Aber das darfst du dir dann selber raussuchen. :-)

# Tags

Soweit so gut. Um den org-mode für rein organisationelle Zwecke abzurunden erkäre ich dir noch kurz, wie du Tags verwenden kannst.

Tags dienen dir um Aufgaben, Notizen, Termine zu gruppieren. Das bringt nicht nur in der Agenda Übersicht viel, sondern auch, wenn du sehr viele Ideen einfach nur herumliegen hast. Damit kannst du nämlich sehr gut lose Ideen tatsächlichen Themen zuordnen.

Platziere den Cursor auf einen Gegestand und dann wähle im Menü *Tags Org > TAGS and Properties > Set Tags* aus. Dann gib zB `:PRIVAT:` ein.

![Tag setzen](/assets/org-mode_fuer_emacs_dummys/11_enter_tag.png)

Wenn du deine Agenda nun aktualisierst, dann sieht das so aus:

![Tag in Agenda](/assets/org-mode_fuer_emacs_dummys/12_tag_in_agenda.png)

Es können auch mehrere Tags verwendet werden. ZB `:PRIVAT:ARBEIT:`

# So könnte deine Agenda aussehen

Du hast nun alles was du benötigst um dein Leben in org-mode abzubilden. Am besten erstellst du nun selbst noch ein paar Dummy Einträge um zu sehen, was alles möglich ist. Wenn du das 5 bis 15 Minuten lang gemacht hast, dann probiers doch morgen einmal im Alltag aus. :-)

Hier noch ein Beispiel für eine Agenda mit vielen Einträgen:

![Beispiel für eine Agenda mit vielen Einträgen I](/assets/org-mode_fuer_emacs_dummys/13_multiple_1.png)

![Beispiel für eine Agenda mit vielen Einträgen II](/assets/org-mode_fuer_emacs_dummys/14_multiple_2.png)

Um zwischen den Wochen in der Agenda zu wechseln kannst du folgendes machen:
* Menü *Agenda > Agenda Dates > Next Dates*
* Menü *Agenda > Agenda Dates > Previous Dates*

Außerdem kannst du auch in der Kalendar herauszommen mittels *Agenda > View > Month View*

![Zoom auf Monat](/assets/org-mode_fuer_emacs_dummys/15_multiple_month_view.png)
