---
layout: post
title:  Firefox Profile für externe IT Berater
author: Richard Bäck
---

Externe IT-Berater haben ein sehr interessantes Leben. Zumindest meiner Meinung nach. Man kann viele verschiedene Branchen, Unternehmen und deren Produkte entdecken und mithelfen großartige Produkte noch weiter zu verbesseren. Meist lebt man von Herausforderung zu Herausforderung. Das ist zwar anstrengend, dennoch immer sehr spannend.

Zwischen all diesen wechselnden Kulissen bleibt allerdings eine Konstante: der Zugang zu dem Kundensystem ist immer verschieden. Doch das schlimmste ist meiner Erfahrung nach, wenn sich Kunden die Technologie des Microsoft-Kontos teilen. Warum: verschiedene Konten werden gespeichert und manchmal bleibt man angemeldet und manchmal nicht. Oder man muss sich zuerst exta abmelden, damit man sich dann mit den anderen Konto wieder anmelden kann. Das ist sehr mühselig.

Aber es gibt eine einfache Lösung: die Firefox-Profile! Diese ermöglichen es mehrere Firefox-Instanzen laufen zu lassen. Der positive Haken daran ist, dass die einzelnen Instanzen sich nicht ihre Daten teilen können. Somit ist es möglich in jeder Instanz eine andere Identität bei Microsoft zu verwenden. Das gleiche gilt natürlich auch für andere Online-Dienste.

Die ist einfach: für jeden Kunden ein Firefox-Profil anlegen. Gestartet wird das Firefox-Profil eines Kundens mittels einer speziellen Firefox-Verknüpfung am Desktop. In diesen Profil können dann alle wichtigen Webseiten als Lesezeichen (zB für die Kontoverwaltung) hinterlegt werden. Und natürlich können dort auch die Anmeldungen bei den verschiedenen Webseiten gespeichert werden.

Doch wie bekommt man das hin? Unter Windows 10 ist das sehr einfach. In den folgenden Schritten beschreibe ich, wie ich für den Kunden _Kunde1_ ein Profil anlege:

1. Der Speicherort der _Firefox.exe_ muss gefunden werden. Diese kann über eine einfache Windows-Suche mittels <kbd>Win</kbd> und der Eingabe _Firefox_ gefunden werden. Mit _Datei Speicherort öffnen_ geht das Verzeichnis der Verknüpfung im Startmenü auf.<br>
![Schritt 1: Speicherort finden](2022-11-30-Firefox-Profile-fuer-externe-IT-Berater/Schritt_01.png)
2. Mittels <kbd>Alt</kbd>+<kbd>Enter</kbd> können die Eigenschaften der Verknüpfung betrachtet werden. Aus diesen kann der Pfad der _Firefox.exe_ entnommen werden. Diesen mittels <kbd>Strg</kbd>+<kbd>C</kbd> in die Zwischenablage kopieren.<br>
![Schritt 2: Pfad kopieren](2022-11-30-Firefox-Profile-fuer-externe-IT-Berater/Schritt_02.png)
3. Nun einen _cmd_ Kommandoprompt mit der Windows-Suche öffnen.<br>
![Schritt 3: _cmd_ öffnen](2022-11-30-Firefox-Profile-fuer-externe-IT-Berater/Schritt_03.png)
4. In den Kommandoprompt mit <kbd>Strg</kbd>+<kbd>V</kbd> den Pfad zur _Firefox.exe_ einfügen und mittels den Parameter `--ProfileManager` den Profil-Verwalter starten.<br>
![Schritt 4: Firefox Profil-Verwalter öffnen](2022-11-30-Firefox-Profile-fuer-externe-IT-Berater/Schritt_04.png)
5. Im geöffnten Firefox Profil-Verwalter ist nun das Standard-Profil vorausgewählt. Falls sich die Markierung ändert, diese wieder zurückändern. Mit Profil erstellen führt ein Wizard durch die Profilanlage. Dort beim Profilnamen _Kunde1_ eingeben. Mit der alten Belegung _Firefox starten_, damit jedenfalls das bestehende Standard-Profil als Vorbelegung erhalten bleibt.<br>
![Schritt 5: Profil anlegen](2022-11-30-Firefox-Profile-fuer-externe-IT-Berater/Schritt_05.png)
6. Im noch geöffneten Kommandoprompt kann nun mit dem Pfad aus 2. und dem Parameter `--profile Kunde1` das neu angelegte Profil getestet werden. Es muss ein neues Firefox Fenster aufgehen, in dem keine Einstellung oder Lesezeichen des Standardprofils vorhanden ist, da es ja ein neues Profil ist.<br>
![Schritt 6: Neues Profil test](2022-11-30-Firefox-Profile-fuer-externe-IT-Berater/Schritt_06.png)
7. Nun die Verknüpfung aus 1. kopieren und auf dem Desktop platzieren. Der Name kann natürlich beliebig gewählt werden. Ich hab _Firefox @ Kunde1_ gewählt.<br>
![Schritt 7: Verknüpfung für neues Profil anlegen](2022-11-30-Firefox-Profile-fuer-externe-IT-Berater/Schritt_07.png)
8. Natürlich muss die neue Verknüpfung dahingehend angepasst werden, dass diese auch den neuen Parameter `--profile Kunde1` verwendet. Dies kann im Reiter _Verknüpfung_ erledigt werden.<br>
![Schritt 8: Verknüpfung anpassen](2022-11-30-Firefox-Profile-fuer-externe-IT-Berater/Schritt_08.png)
9. **Bonus:** Mit mehreren Firefox-Instanzen kann man den Überblick verlieren, welche Instanz was beinhaltet. Ich persönlich verwende dazu die Lesezeichen-Leiste. Aber die Instanz selbst kann das auch über _Hilfe_ > _Weitere Informationen zur Fehlerbehebung_ > _Profilordner_ preisgeben.<br>
![Schritt 9.1: Profil herausfinden 1](2022-11-30-Firefox-Profile-fuer-externe-IT-Berater/Schritt_09.01.png)<br>
![Schritt 9.2: Profil herausfinden 2](2022-11-30-Firefox-Profile-fuer-externe-IT-Berater/Schritt_09.02.png)

Ich hoffe, dass ich dir, lieber Leser, damit eine Idee geben konnte, wie du deine Konten besser organisieren kannst. Die Idee der Firefox-Profile ist natürlich auch in anderen Szenarien anwendbar!