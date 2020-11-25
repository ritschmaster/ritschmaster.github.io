---
layout: post
title:  Quakeworld - Ein Einstieg
author: Richard Bäck
---

[Quake](https://de.wikipedia.org/wiki/Quake) gehört mit seinen Erscheindungsjahr 1996 zu einem der ältesten noch aktiv gespielten Spiele überhaupt. Hauptgrund warum es überhaupt noch lebt ist die Tatsache, dass dessen Quellcode unter der [GPL](https://de.wikipedia.org/wiki/GNU_General_Public_License) veröffentlicht wurde und somit freie Software ist. Denn dieses Faktum bat sehr vielen Entwicklern und Interessenten in der Vergangenheit und auch in der Zukunft die Möglichkeit eigene Werke darauf aufzubauen. Abgesehen von Mods (wie [CTF](https://de.wikipedia.org/wiki/Capture_the_Flag) oder [Team Fortress](https://de.wikipedia.org/wiki/Team_Fortress)) sind damit auch Erweiterung der Engine selber möglich - wie zB die Unterstützung von Full HD. Selber Mods und Karten erstellen ist sehr einfach, da es eine [Unzahl von Anleitungen](https://www.youtube.com/watch?v=gONePWocbqA&list=PLgDKRPte5Y0AZ_K_PZbWbgBAEt5xf74aE) bereits Online gibt.

Das alleine macht Quake natürlich nicht aus. Es ist die wunderschöne Einfachheit des Spielprinzips, die es bietet. Es gibt nur sehr wenige Waffen und in den Abwerk-Spielmodi immer einen Instant-Respawn. Das vermeidet Frust, selbst wenn das Gegenüber wesentlich besser ist als man selbst. Und weil es so einfach ist, kann man sich auf das wesentliche konzentrieren: das Verbessern der eigenen Reaktionen und des Lagebewusstseins.

Weiters ist die Freiheit über den Spielklienten fast einmalig in der Computer-Spiele welten (außer vielleicht bei [ICS](https://de.wikipedia.org/wiki/Schachserver)-Klienten). Ob man mit dem originalen Klienten von 1996 spielt, oder einem modernen mit neuen Texturen, [Blur-Effekten](https://de.wikipedia.org/wiki/Weichzeichnen) und verbesserten Explosionsdarstellungen, macht keinen Unterschied. Jeder kann das Spiel so spielen wie er will.

Diese Freiheit des Spielklienten kommt natürlich auch mit einem Preis. Gute Spieler haben eigene Konfigurationen, die Spielfiguren und Gegenstände eigens hervorheben. Neue Spieler kennen diese Kniffe nicht und haben somit klarerweise das Nachsehen. Das wierderum führt zu einem Ohnmachtsgefühl was sich im schlimmsten Fall zu einem Fernbleiben von Duellen (1vs1), Mannschafts-Modi (2vs2, 4vs4, ...) oder sogar vom ganzen Spiel führt. Das wiederum hilft der Gemeinschaft nicht, da sie nicht wachsen (oder zumindest seine Spielerbasis halten) kann.

Damit du dich, lieber Leser, auch an Quake trauen kannst und nicht so wie ich alles zusammen suchen musst erkläre ich in diesem Artikel wie du in einer halben Stunde durchstarten kannst.

# Der Klient

Der einfachste Klient ist eine bereits vorkonfigurierte Version von [ezQuake](https://www.ezquake.com/) durch die [Quakeworld Gemeinschaft](https://www.quakeworld.nu/): die nquake Distribution.

1. Den Klienten von [nquake.com](https://www.nquake.com/) über den "Download"-Knopf für sein Betriebssystem herunterladen
 1. Unter Linux wird nquake einfach im Heimverzeichnis installiert
2. Installieren
 1. Alle Modi installieren (TF, ...)
 2. Keine HD Texturen installieren, die braucht sowieso niemand
 3. Wenn man Quake nicht besitzt, dann ist das kein Problem. Die gratis Shareware-Version ist ausreichend für den Mehrspielermodus und wird automatisch heruntergeladen
 
Mit dem Klienten nun installiert könnte man nun schon loslegen. Aber halt! Da kommt noch etwas mehr um bei der ersten Partie auch Frags zu ergattern!

# Die Konsole

Das wichtigste des Spielklienten ist die Konsole. Nach dem Öffnen des Klienten kann sie über <kbd>^</kbd> erreicht werden.

# Das Spielprinzip

Quake kennt nur ein Spielprinzip: Deathmatch. Zwar einzeln oder mannschaftsbasiert, dennoch nicht mehr. Daher ist es wichtig die folgenden Punkte zu meistern:

* Die Waffen kennen lernen
* Die Karten kennen lernen
* Das Rüstungssystem kennen lernen
* Die Gegenstände stoppen lernen
* Die möglichen Bewegungen kennen lernen
* Lernen gute Informationen zu geben (wahlweise für 2vs2, ...) - werde ich nicht weiter ausführen

Ich werde auf diese Punkte nun eingehen, allerdings nur auf die wichtigsten Punkte. Ich empfehle sehr stark diese [sehr, sehr, sehr gute Video-Serie eines ehemaligen Profis](https://www.youtube.com/watch?v=pLmuRRm1Bag&list=PLxP7tvMqaXzDjw7OYYIEbplCdZOaHLFPg). 

## Die Waffen kennen lernen

Es gibt insgesamt 8 verschiedene Waffen:
* Axe
 * Basisausrüstung beim Spawn
 * Nicht wichtig, dient nur zum Trollen
* Shotgun
 * Basisausrüstung beim Spawn
 * Gut um entfernte Gegner zu treffen
 * Hitscan = Keine verzögerung der Projektile. Nach dem Abdrücken schlagen die Projektile schon ein.
* Super Shotgun
 * Wie Shotgun, bringt nur mehr Schrot pro Schuss raus
 * Gut um entfernte Gegner zu treffen
 * Hitscan
* Nailgun
 * Schießt langsame Projektile
 * Dient entweder zum Trollen oder als Ersatzwaffe für den Grenade Launcher
* Shuper Nailgun
 * Wie Nailgun, bringt nur mehr Nails in einem kleinerem Zeitintervall raus
* Grenade launcher
 * Verschießt Granaten, die nach der Zeit explodieren. Wenn ein Projektil eine Spielfigur direkt trifft, dann explodiert sie sofort
 * Die Granaten fliegen parabelförmig
 * Verursacht 100 Schaden
 * Dient zum Verwehren von Wegen (zB bei Ein- oder Ausgängen von Räumen)
 * Kann als Ersatz für [Rocket jumps](https://en.wikipedia.org/wiki/Rocket_jumping) verwendet werden
* Rocket Launcher
 * Verschießt Raketen. Wenn ein Projektil eine Spielfigur direkt trifft, dann explodiert sie sofort.
 * Das Projektil fliegt gerade und sehr schnell
 * Verursacht 100 Schaden
 * Erlaubt Rocket jumps
 * Erlaubt wie der Grenade Launcher das Verwehren von Wegen
 * Ist neben der Lightning Gun die wichtigste Waffe im Spiel
* Lightning Gun
  * Hit scan
  * Verursacht 300 Schaden in der Sekunde
  * Ist neben dem Rocket Launcher die wichtigste Waffe im Spiel
  * In Flüssigkeiten (Wasser, Lava) entladet sich die Lightning Gun, wenn man sie feuert. Das führt zum sofortigen Tod der eigenen Spielfigur. Allerdings erwischt es auch Spielfiguren im näheren Umkreis. Wieviel und wie weit der Schaden geht, hängt von der Menge an Munition für die Lightning Gun ab. ZB bei voller Munition kann eine Entladung im Lava-Becken auf DM4 jede Spielfigur im gleichen Raum des Lava-Beckens töten.
  
Die wichtigste Strategie ist es einen Rocket Launcher und eine Lightning Gun zu bekommen.

Noch wichtiger ist es zu wissen und zu verstehen, dass das Wechseln von Waffen keine Zeit kostet. Daher verwenden geübte Quake-Spieler keine Tastenbelegung, die eine Waffe auswählen, sondern Tastenbelegungen, die gleich mit einer Waffe schießen.

## Die Karten kennen lernen

In Quakeworld haben sich einige Karten sehr lange gut gehalten. Vorteil: man kann sich auf eine engere Auswahl konzentrieren. Nachteil: andere haben sich bereits auf eine engere Auswahl konzentriert.

* DM2 (Claustrophobolis)
 * Hat keine Lightning Gun
 * Hat 2 Red Armors und 2 Megahealths
 * Wird gerne für Duels, FFAs (Free for all - jeder gegen jeden) und Mannschaftsspiele verwendet
* DM3 (The Abandoned Base)
 * Wird sehr gerne für Mannschaftsspiele verwendet
* DM4 (The Bad Place)
 * Wird sehr gerne für Duels verwendet
* DM6 (Darkzone)
 * Wird sehr gerne für Duels verwendet
* E1M2
 * Wird sehr gerne für Mannschaftsspiele verwendet
* ZTNDM3 (Bloodrun)
 * Wird sehr gerne für Duels und FFAs verwendet
* BRAVADO
 * Wird sehr gerne für Duels und FFAs verwendet
* SKULL
 * Wird sehr gerne für Duels verwendet
* SCHLOSS
 * Wird sehr gerne für Mannschaftsspiele verwendet
* PUSHDMM4
 * Trainiert das Schießen mit dem Rocket Launcher auf Spielfiguren, die in der Luft fliegen
* POVDMM4
 * Trainiert das Schießen mit der Lightning Gun
 
Jede Karte kann mit dem Konsolen-Kommando `/MAP <Kartenname>` erreicht werden.

## Die möglichen Bewegungen kennen lernen

Die wichtigsten Begriffe, die man kennen und können muss:

* Running next to walls
* Strafe running/jumping
* Rocket jumping

Ich werde das nicht weiter ausführen. Die beste Erklärung ist die [sehr, sehr, sehr gute Video-Serie eines ehemaligen Profis](https://www.youtube.com/watch?v=pLmuRRm1Bag&list=PLxP7tvMqaXzDjw7OYYIEbplCdZOaHLFPg).

### Rocket jumps in Quake

Der Rocket jump in Quake ist schwieriger als in Quake III und anderen Nachfolgern von Quake. Deshalb wird meistens dafür ein Skript in der Quake Konfiguration hinterlegt. Auf diese gehe ich in den nachfolgenden Kapiteln ein.

## Das Rüstungssystem kennen lernen

In Quake ist das Rüstungssystem anders als in den Nachfolger Quakes. In Quake III zB absorbiert die Rüstung immer 66% des erhaltenen Schadens. In Quake ist der absorbierte Schaden progressiv. D.h. es kommt darauf an, welche Rüstung man hat. Außerdem können schwächere Rüstungen nur aufgenommen werden, wenn die Stärke unter einem Schwellenwert gesunken ist.

* Red Armor
 * Bei Aufnahme sofort 200 Rüstungspunkte
 * Absorbiert 80% des erhaltenen Schadens
 * Yellow Armor kann erst aufgenommen werden, wenn < 113 Rüstungspunkte übrig sind
 * Green Armor kann erst aufgenommen werden, wenn < 38 Rüstungspunkte übrig sind
* Yellow Armor
 * Bei Aufnahme sofort 150 Rüstungspunkte
 * Absorbiert 60% des erhaltenen Schadens
 * Green Armor kann erst aufgenommen werden, wenn < 50 Rüstungspunkte übrig sind
* Green Armor
 * Bei Aufnahme sofort 100 Rüstungspunkte
 * Absorbiert 30% des erhaltenen Schadens
 
Wichtiger Hinweis: mit 100 Lebenspunkte und voller Green Armor überlebt man genau einen Volltreffer einer Rakete oder einer Granate.

## Die Gegenstände stoppen lernen

Die Uhr ist das wichtigste Element auf dem gesamten Bildschirm. Mit ihr können Gegenstände gestoppt werden um sie beim nächsten Erscheinen vor dem Gegner zu erreichen.

* Megahealth
 * Erscheint 20 Sekunden *nachdem* der Spieler, der es als letztes gehabt hat, <= 100 Lebenspunkte hat
* Red, Yellow, Green Armor
 * Erscheint 20 Sekunden *nachdem* ein Spieler den Gegenstand aufgenommen hat

# Den Klienten richtig konfigurieren

## Die Texturen

Texturen sind nur zu Beginn wichtig, damit sich das Gehirn sich die Räume in den Karten leichter einprägen kann. So bald man die Grundrisse der Karten inne hat, bringen sie nichts mehr. Deren Abwesenheit ist sogar besser, da man die Gegenstände und die anderen Spielfiguren leichter erkennt. Daher ist eine einheitliche graue Farbe für alle Wände vorteilhaft.

## Die Spielfiguren

Die Spielfiguren sollten so einfach zu erkennen sein wie möglich. Deshalb sollten die feindlichen Spielfiguren in einer einheitlichen Farbe sein (zB rot) und die freundlichen ebenso (zB weiß).

## Das Fadenkreuz

Da es in Quake keinen Rückstoß gibt dient das Fadenkreuz nur dazu die Projektile oder die Schüsse möglichst genau zu platzieren. Wie bei allen Fadenrkreuzen ist der Kontrast das aller wichtigste. Da kein Rückstoßindikator notwendig ist kann das Fadenrkeuz auch sehr klein sein um die Sicht nicht unnötig einzuschränken.

## Das Sehfeld

Das Sehfeld ist ein kompliziertes Thema. Das Problem: je größer das Sehfeld, desto schneller wird die Mausbewegung und umgekehrt. Es gilt daher eine Balance zwischen dem Sehfeld und der Mausgeschwindigkeit zu finden. Glücklicherweise kann man durch die Quake-Konfiguration auf eine Tastenkombination mehrere Kommandos legen. D.h. es ist möglich das Sehfeld oder die Mausgeschwindigkeit automatisch zu wechseln, wenn die Waffe gewechselt wird.

## Die Waffenmodelle

Die Standard-Waffenmodelle sind ausreichend um zu erkennen welche Waffe man gerade trägt. Was allerdings wichtig ist: die Waffenmodelle nehmen sehr viel Platz im Sehfeld ein. Es macht daher Sinn die Waffenmodelle entweder teilweise oder sogar vollständig durchsichtig zu schalten.

## Kontrastreiche Projektile

Projektile müssen so bald wie möglich erkannt werden um ihnen effektiv ausweichen zu können. Deshalb ist es ratsam die Projektilfarbe auf violet, rosa oder grün zu ändern. Natürlich darf es nicht die gleiche Farbe wie die der Spielfiguren sein.

## Die gesamte Konfiguration

Zuerst die allgemeine Klientenkonfiguration. Diese ist unter `/Pfad/zu/nquake/ezquake/configs/config.cfg` erreichbar. Meine Konfigurationsdatei kannst du von [hier](/assets/quake/config.cfg) herunterladen und benutzen. Sie erfüllt alle oben genannten Punkte und kann dir entweder direkt als deine Konfiguration oder als Vorlage deiner höchst persönlichen Konfiguration dienen.

Für kontrastreichere Projektile platziere dir [diese Datei](/assets/quake/grenade_0.png) in `/Pfad/zu/nquake/qw/textures/models/`.

# Bereit werden

In FFA läuft das Spiel in dem Moment los, in dem die Karte geladen wurde. Im Duel und in den Mannschaftsspielen muss immer jeder Spieler zuerst mit `/ready` bestätigen, dass er bereit zum Spielen ist. Erst dann geht das Spiel nach einem Runterzählen (normalerweise von 10) los.

## Bereit für die nächste Karte

In den meisten Servern werden zwei Befehle angeboten:

* `/votemap <Karte>` um für eine bestimmte Karte zu stimmen
* `/nextmap` um für das Überspringen der derzeitigen Karte zu stimmen.

## Training

Das wichtigste ist Training. Die nquake Distribution liefert bereits eine volle Konfiguration für das Training gegen Bots mit. Mit den folgenden Befehlen kann es losgehen:

* `/bot_arena`
 * Startet ein Spiel im Arena Modus.
 * Das hilft auf PUSHDMM4 oder POVDMM4, aber auch auf Duel-Karten
* `/bot_1on1`
 * Datart ein Spiel im Duel Modus
 * Das hilft die verschiedenen Duel-Karten kennen zu lernen
* `/addbot`
 * Wenn im Spiel kann damit ein Bot hinzugefügt werden
* `/skillup` und `/skilldown`
 * Damit kann die Spielstärke der Bots reguliert werden
* `/timelimit <Minuten>`
 * Damit kann die Rundenlänge reguliert werden 
 
## Spiele finden

Entweder über `/join <IP:PORT oder NAME:PORT>` mit IP:PORT bzw. NAME:PORT von [quakeservers.net](https://www.quakeservers.net/quakeworld/servers/so=8/) oder man geht selbständig auf einen Server und verwendet den [IRC](https://en.wikipedia.org/wiki/Internet_Relay_Chat) Broadcast. Der IRC Broadcast ist die Möglichkeit auf allen verbunden Quake-Servern eine Nachricht zu senden - ähnlich wie der globale Chat in World of Warcraft. Außerdem wird die Nachricht auch in den IRC channel #quakeworld im [QuakeNet](https://www.quakenet.org/) gesendet.

Um eine Nachricht über den IRC Broadcast zu senden reicht `.QW <Nachricht>` in der Konsole auf einem Quake Server.

## Gemeinschaft finden

* [IRC](https://hexchat.github.io/): #quakeworld im QuakeNet
 * Bin dort im übrigen auch regelmäßig
* [Discord](https://discord.com/): https://discord.com/invite/0vmvMMyzOSMYrYbA

# Los gehts!

Wir sehen uns beim Spielen!
