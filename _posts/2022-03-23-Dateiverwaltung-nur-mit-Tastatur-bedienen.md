---
layout: post
title:  Dateiverwaltung nur mit Tastatur bedienen
author: Richard Bäck
---

Dateiverwalter wie der GNOME Nautilus, KDE Dolphin, XFCE Thunar, aber auch der Windows Explorer, können allesamt mit der Tastatur alleine bedient werden. Anders als vielleicht vermutet wird dafür nicht die [Tastaturmaus](https://de.wikipedia.org/wiki/Tastaturmaus) benötigt. Dies funktioniert alleine durch Tastenkürzel.

Im näheren gehe ich auf Tastenkürzel ein, die jedenfalls in GNOME Nautilus funktionieren. Größtenteils funktionieren diese aber auch in anderen bekannten Dateiverwaltern. Da ich beruflich leider sehr oft den Windows Explorer verwenden muss, gebe ich auch abweichende Tastenkürzel für diesen bekannt, denn größtenteils decken sich die wichtigsten Tastenkürzel mit Nautilus.

# Dateien kopieren/ausschneiden/einfügen

Das Minimum um überhaupt einen Computer <s>sinnvoll</s> angenehm bedienen zu können:
* <kbd>Strg+a</kbd> - alle Dateien auswählen
* <kbd>Strg+x</kbd> - alle Dateien ausschneiden
* <kbd>Strg+c</kbd> - alle Dateien kopieren
* <kbd>Strg+v</kbd> - alle Dateien einfügen

# Navigation im Dateiverwalter selbst

Die verschiedenen Bereiche innerhalb des Dateiverwalters können mittels <kbd>Alt-F6</kbd> (vorwärts) und <kbd>Umschalttaste-Alt-F6</kbd> (rückwärts) erreicht werden.

Am Anfang ist dies ziemlich gewöhnungsbedürftig, da besonders meistens auf Bereiche gewechselt wird, auf die man gar nicht wechseln wollte. Aber nach einigen Tagen strikter Verwendung dieser Tastenkombinationen gewöhnt man sich daran und fängt es an lieber zu verwenden als die Mausnavigation innerhalb des Fensters.

Als Beispiel: ein neu geöffentes Fenster von Nautilus hat immer den Fokus auf das gerade betrachtete Dateiverzeichnis (normalerweise das Heimverzeichnis). Das sieht man aber so nicht direkt. Erst mit 2-maliger Betätigung des Tastenkürzels <kbd>Pfeilunten</kbd> (siehe weiter unten) wird einem dies erst bewusst, da man dann tatsächlich auch die Dateiselektion sieht. Der Windows Explorer verhält sich hier gleich. Hat man dies noch nicht verinnerlicht, dann landet man mit <kbd>Alt-F6</kbd> allerdings (gerade beim Windows Explorer) schnell in Fensterbereiche, in die man nicht möchte. Das schafft, gerade am Anfang, großen Frust. Umso angenehmer ist es, wenn man diese initiale Position einmal verinnerlicht hat!

# Dateien suchen

Der Klassiker: man weiß Teile des Dateinamens, aber weder in welchem Verzeichnis die Datei liegt, noch wie sie genau heißt. Für solche Fälle gibt es das allgemein bekannte Tastenkürzel <kbd>Strg+F</kbd>. Im Suchergebnis kann wiederum mit den Pfeiltasten navigiert werden.

# Die Ansicht wechseln

Wer kennt das nicht. Man wechselt in einen Ordner hinein, doch die Ansicht ist nicht so eingestellt wie man es gerade braucht. Im Download Verzeichnis benötigt man oft die Listenansicht. Im Verzeichnis mit den Familienfotos wäre die Ansicht als Kacheln hilfreich.

* <kbd>Strg-1</kbd> wechselt auf die Listensicht
* <kbd>Strg-2</kbd> wechselt auf die Kachelsicht

## Anmerkung für Windows Explorer

Im Windows Explorer funktioniert das leider nicht so einfach. Dafür muss der Ansichtsreiter angesteuert werden. Allerdings kann das auch mittels Tastenkombinationen erfolgen. Die <kbd>Alt</kbd> Taste erlaubt es alle Funktionen in der Werkzeugleiste zu erreichen.

In meiner Windows Version kann ich somit mittels <kbd>Alt-V-L</kbd> das Layoutfeld in der Werkzeugleiste erreichen. Darin ist es möglich mittels den Pfeiltasten das gewünschte Layout auszuwählen. 

Im übrigen kann man mit <kbd>Esc</kbd> eine Ebene in der Werkzeugeleiste hinaufwechseln, wenn man im <kbd>Alt</kbd>-Modus ist.

# Dateien umbenennen

Wenn die Datei ausgewählt ist, dann kann sie mit <kbd>F2</kbd> umbenannt werden.

# Neuanlage eines Verzeichnisses

Verzeichnisse können sehr einfach mittels des Kürzels <kbd>Strg+Umschalttaste+N</kbd> angelegt werden.

# Navigation mittels Pfadleiste

Die Pfadleiste ist mächtiger als man glaubt. Mit ihr kann auf eine unglaublich präzise Art und Weise navigiert werden. Gerade Anwender, die schnell tippen, sind mit ihr wesentlich schneller als auf eine andere Art.

Aber auch langsame Tipper können dies zu ihren Vorteil verwenden.

Um überhaupt in die Pfadleiste zu wechseln, wird die Kombination <kbd>Strg+l</kbd> verwendet.

Einmal angelangt, stehen einem die bekannten Tastenkürzel für die Textbearbeitung zu Verfügung:
* Mit <kbd>Pos1</kbd> wird der Cursor zum Anfang des Pfads positioniert
* Mit <kbd>Ende</kbd> wird der Cursor zum Ende des Pfads positioniert
* Mit <kbd>Strg+Rücktaste</kbd> wird das Wort vor dem Cursor gelöscht (bis zum nächsten Pfadtrenner)
* Mit <kbd>Strg+Entf</kbd> wird das Wort nach dem Cursor gelöscht (bis zum nächsten Pfadtrenner)
* Mit <kbd>Strg+Pfeillinks</kbd> wird der Cursor um ein Wort nach links verschoben
* Mit <kbd>Strg+Pfeilrechts</kbd> wird der Cursor um ein Wort nach rechts verschoben

GNOME Nautilus vervollständigt automatisch den Pfad, wenn sich nur mehr eine Kombination möglich ist. D.h. die <kbd>Tabulatortaste</kbd> wird nicht benötigt. Gerade diese Funktion ermöglicht es sehr schnell in ein Verzeichnis zu wechseln. Wer sein System gut kennt, der kann die Vorteile dieser Navigationsart meist ausnutzen.

Ein wichtiger Tipp ist hier die Möglichkeit ins Heimverzeichnis mit nur einer Taste zu wechseln - und zwar mit <kbd>~</kbd>. Auch interessant: im Windows Explorer kann das Heimverzeichnis mit dem Wort `%HOME%` erreicht werden.

# Navigation mittels Verzeichnisstruktur

Wechselt man in ein nur selten besuchtes Verzeichnis, dann hilft einem die Pfadleiste nicht. Eine Orientierung nach einer Sichtung der verfügbaren Unterverzeichnisse ist da oftmals die präferierte Variante.

Doch auch hier können einem Tastenkürzel das Leben leichter machen. Folgende sind verfügbar:
* Mit <kbd>Pfeilunten</kbd> wird nach unten navigiert (Listen- & Kachelsicht)
* Mit <kbd>Pfeiloben</kbd> wird nach oben navigiert (Listen- & Kachelsicht)
* Mit <kbd>Pfeillinks</kbd> wird nach links navigiert (Kachelsicht)
* Mit <kbd>Pfeilrechts</kbd> wird nach rechts navigiert (Kachelsicht)
* Mit <kbd>Enter</kbd> wird ein Verzeichnis betreten
* Mit <kbd>Alt-Pfeilunten</kbd> gleich wie <kbd>Enter</kbd>
* Mit <kbd>Alt-Pfeiloben</kbd> wird das übergeordnete Verzeichnis betreten
* Mit <kbd>Alt-Pfeillinks</kbd> wird das (in der Navigationshistorie) vorherig besuchte Verzeichnis betreten
* Mit <kbd>Alt-Pfeilrechts</kbd> wird das (in der Navigationshistorie) nächste besuchte Verzeichnis betreten
* Mit <kbd>Strg+Pfeiloben</kbd> wird in das übergeordnete Verzeichnis gewechselt 
* Mit <kbd>Strg+Pfeillinks</kbd> wird in das vorherig besuchte Verzeichnis gewechselt 
* Mit <kbd>Strg+Pfeilrechts</kbd> wird in das danach besuchte Verzeichnis gewechselt
* Mit <kbd>Menü</kbd> wird das Kontextmenü des ausgewählten Verzeichnis(se)/der ausgewählten Datei(en) geöffnet. 
 * Ist kein Verzeichnis/keine Datei ausgewählt, dann wird das Kontextmenü des derzeitigen Verzeichnis geöffnet.
 * Sollte die <kbd>Menü</kbd> Taste auf der Tastatur fehlen, dann kann diese normalerweise (in Xorg, als auch Windows) mit der Tastenkombination <kbd>Umschalttaste-F10</kbd> emuliert werden.
* Mit <kbd>Strg+Leertaste</kbd> wird die derzeitige Selektion entfernt. 
 * Das kann hilfreichsein um <kbd>Menü</kbd> aufs derzeitige Verzeichnis anwenden zu können, um zB eine neue Datei anlegen zu können.
 * Ein weiterer Anwendungsfall ist die weitere Dateiselektion bei gedrückt gehalteter <kbd>Strg</kbd> Taste
* Mit gedrückt gehaltener <kbd>Strg</kbd> kann eine Selektion gehalten werden
* Mit <kbd>Umschalt-Pfeilunten</kbd> kann eine mehrfach Selektion von Dateien nach unten durchgeführt werden
 * Dies ist auch mit <kbd>Strg</kbd> und <kbd>Strg+Leertaste</kbd> kombinierbar!
* Mit <kbd>Umschalt-Pfeiloben</kbd> kann eine mehrfach Selektion von Dateien nach oben durchgeführt werden
 * Dies ist auch mit <kbd>Strg</kbd> und <kbd>Strg+Leertaste</kbd> kombinierbar!

Die Dateinavigation mittels Pfeiltasten sollte keinesfalls unterschätzt werden. Da bei der Navigation mittels Pfeiltasten die derzeitig ausgewählte Datei immer größtmöglich hervorgehoben wird, kann man diese Hervorhebung als Ersatz für den Mauscursor verwenden. Denn ich habe immer mit dem Mauscursor - wie ein kreisender Falke über einem Feld - versucht die Datei zu finden. Ist die Datei gefunden, dann klickte ich so schnell wie möglich los - wie der Falke, wenn er seine Beute endlich gesichtet hat. Das kostet allerdings Energie. Denn sollten die Dateien ohnehin einzeln durchgegangen werden, dann bietet eine spezielle Hervorhebung noch einmal eine bessere Suchunterstützung.

## Anmerkung für Windows Explorer

<kbd>Alt-Pfeilunten</kbd> wird nicht unterstützt.

# Favoriten verstecken/anzeigen

Am linken Bildrand stellt Nautilus Favoriten dar. Diese könnten nervig sein. Mittels <kbd>F9</kbd> können diese aus- und eingeblendet werden.

# Versteckte Dateien anzeigen

In den meisten Fällen gelangt man unabsichtlich zu dieser Ansicht. Zumindest mir geht es so. Aber damit ist nun Schluss. Denn mit <kbd>Strg+h</kbd> können versteckte Dateien angezeigt/ausgeblendet werden.

## Anmerkung für Windows Explorer

Dieser Tastenkürzel wird so nicht unterstützt. Anstattdessen muss der Weg über die Werkzeugleiste bestritten werden.

Ich komme mit den folgenden Tastenkürzel dorthin: <kbd>Alt-V-HH</kbd>
