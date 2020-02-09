---
layout: post
title:  Von Linux auf Android Telefon zugreifen
author: Richard Bäck
---

# Hintergrund Geschichte

Vor geraumer Zeit suchte ich nach einer Kurznachrichten Applikation die eine Unzahl von Anforderungern erfüllt:

- Möglichkeit Ende-zu-Ende verschlüsselte Nachrichten zu versenden
- Die Applikation soll auf allen gängigen Betriebssystemen (Linux, Windows, Mac, Android, iOS) laufen
- Es soll so einfach wie möglich sein, damit auch Normalos es bedienen können
- Es soll quelloffen sein

Zum damaligen Zeitpunkt blieben mir nur noch Signal und Telegram übrig. Matrix/Riot hab ich nach einem Problelauf ausgeschlossen, da es zum einen nur bedingt einfach zu bedienen war und zum anderen auf mobilen Geräten nicht so flüssig als auf stationären lief. Somit führten diese zwei Fakten zum technischen K.O.

Obwohl Signal oberflächlich sicherer schien, sagte mir Telegram aus zwei Punkten zu:

1. Die Gruppenchats in Telegram sind fast unlimitiert. Somit kann man Telegram als ein IRC Ersatz verwenden.
2. Meiner Meinung nach ist der Secret Chat Ansatz von Telegram der derzeitig sicherste am Markt. Je mehr Geräte und/oder Personen in den Nachrichtenempfängern involviert sind, desto unsicherer ist der Kanal.

Also entschied ich mich Telegram zu verwenden und zu bewerben. Im Rückblick (Stand des Blog-Eintrags) bereue ich meine Entscheidung nicht. Es gibt nur eine Kleinigkeit, die mich bis heute gestört hat: die Telegram Desktop Applikation bietet die "Geheimer Chat" Funktion nicht. D.h. ein Ende-zu-Ende verschlüsselter Kanal kann nur zwischen zwei mobilen Geräten versendet werden. Liest man sich die genaue [Begründung von Telegram](https://tsf.telegram.org/manuals/e2ee-simple) dazu durch, warum nur ein Gerät der Empfänger sein kann/darf, macht das sogar sinn. Dennoch ist es unangenehm, wenn man das Mobiltelefon eigentlich nur zur Telefonie benutzt.

Lange Suchen im Internet nach "Secret Chat Telegram Desktop" oder ähnliches führten zu keinem Ergebnis. Außer zu anderen Benutzern die die Funktion vermissen. Es gibt sogar einen [Fehlereintrag im Github-Projekt](https://github.com/telegramdesktop/tdesktop/issues/871). Doch nach sehr langer Zeit und allen möglichen Tricksereien mit [Shashlik](http://www.shashlik.io/), [Anbox](https://anbox.io/) und [Pidgin](https://github.com/majn/telegram-purple) hatte ich immer noch nicht die perfekte Lösung gefunden. Denn selbst wenn ich unter Linux einen Secret Chat starten könnte, könnte ich weder am Mobiltelefon einen zweiten aufmachen, noch auf die Nachrichten zugreifen.

Doch eines Tages erinnerte ich mich daran, dass es ja möglich ist, Android Apps direkt am Gerät zu testen. Das führte mich zu einer neuen Idee: warum nicht einfach direkt auf die Bildausgabe des Geräts zugreifen? Schlussendlich ist das ohnehin die einzig richtige Art den Geheimen Chat zu führen - auf nur einem Gerät und zwar einem mobilen, damit man die Nachrichten __immer und überall__ absenden kann. Und nun endlich habe ich sie, die perfekte Lösung um die "Geheimer Chat" Funktionalität auch unter Linux (Windows, MacOS, ...) zu benutzen!

# Installation unter Fedora

Die Applikation [scrcpy](https://github.com/Genymobile/scrcpy) erlaubt die Übertragung des Ausgabebildes eines beliebigen Android-Gerät zu Linux. Entweder über USB oder über WLAN. Um scrcpy allerdings nutzen zu können wird zuerst das [Android SDK](https://developer.android.com/studio/) benötigt.

Zuerst kommen die frei installierbaren Abhängigkeiten dran. Im Terminal folgendes absetzen:

    sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
    sudo dnf install SDL2-devel ffms2-devel meson gcc make java-devel

Danach von der [Download-Seite](https://developer.android.com/studio/) die _sdk-tools-linux_ für die Kommandozeile herunterladen, entpacken und mit dem Terminal in das entpackte Verzeichnis wechseln. Nun dort folgende Befehle absetzen um die weiteren benötigten Werkzeuge zu installieren:

    ./bin/sdkmanager --install "platforms;android-29"
    ./bin/sdkmanager --install "build-tools;28.0.3"
    echo 'export ANDROID_HOME=~/' >> ~/.bashrc
    echo 'export PATH=$PATH:~/platform-tools' >> ~/.bashrc

Als nächstes kommt scrpy dran. Einfach von der [Release-Seite](https://github.com/Genymobile/scrcpy/releases) die neueste _Source code zip_ herunterladen, entpacken und mit dem Terminal in das entpackte Verzeichnis navigieren. Von dort aus kann danach die Installation/Einrichtung erfolgen:

    meson x --buildtype release --strip -Db_lto=true
    ninja -Cx

# Erste Verwendung mit einem Telefon

Um scrcpy mit einem beliebigen Mobiltelefon benutzen zu können muss bei diesem zuerst die USB-Debugging Funktionalität eingeschaltet sein. Dies kann folgendermaßen erfolgen:

1. In die Einstellungen am Mobiltelefon wechseln
2. Ist dort ein Punkt "Entwickleroptionen" zu finden, dann dort hinein wechseln
    1. Die Entwickleroptionen einschalten
    2. Das USB-Debugging einschalten
3. Sollte der Punkt "Entwickleroptionen" nicht zu finden sein, dann nicht verzweifeln. Dann sind am Gerät die Entwickleroptionen noch versteckt. Sie können folgendermaßen aktiviert werden:
    1. In den Einstellungen "Telefoninfo" öffnen
    2. Sollte es den Punkt "Softwareinformationen", dann diesen öffnen
    3. Auf "Buildnummer" 7 mal tippen.
    4. Weiter mit 2.

Nachdem USB-Debugging eingeschaltet ist, muss ein per USB verbundenes Mobiltelefon bei einem absetzen des Kommandos `adb devices` im Terminal gefunden werden. Bevor das nicht der Fall ist, kann scrcpy den Bildschirm nicht übertragen.

Wenn in der Ausgabe von `adb devices` dann ein Gerät mit _unauthorized_ gelistet wird, dann das Mobiltelefon einfach noch einmal verbinden und die Verbindung am Mobiltelefon bestätigen. Danach sollte aus _unauthorized_ in der Ausgabe zu _device_ geändert worden sein. Sollte es dennoch nicht funktioniert kann dieser [Stackoverflow-Eintrag](https://stackoverflow.com/questions/23081263/adb-android-device-unauthorized#answer-25546300) helfen.

Nun endlich kann man im Verzeichnis von scrcpy Terminal mit den folgenden Befehlen scrcpy (im Verzeichnis von scrcpy) starten:

    ./run x

# Wiederholte Verwendung

Um die Verwendung einfacher zu gestalten kann die Datei`~/.local/share/applications/scrcpy.dekstop` angelegt werden. Mit dieser scheint dann auch ein Menüpunkt in KDE, GNOME, XFCE etc auf. Der Inhalt der Datei:

    [Desktop Entry]
    Version=1.0
    Name=scrcpy
    Exec=/bin/bash -c 'cd ~/scrcpy && ./run x'
    Terminal=false
    Type=Application

Die oben angeführte Konfiguration geht davon aus, dass scrcpy in `~/scrcpy` hinterlegt ist.

# Sicherheitshinweise

Da USB-Debugging höchst wahrscheinlich ab jetzt immer eingeschaltet ist, ist das Risiko höher, dass Fremdsysteme diese Verbindung ausnutzen. So lange man also das USB-Debugging eingeschaltet hat, sollte man das Mobiltelefon entweder nur über seinen eigenen Rechner oder über die Steckdose aufladen.

# Qubes-Benutzer

Für Qubes-Benutzer ist der gesamte Blog-Eintrag ebenso gültig. Allerdings gibt es nur ein Problem: die dynamische Umleitung von USB-Geräten zu den verschiedenen VMs funktioniert nur für Speichermedien. Daher kann der Verbindungsaufbau von adb als auch scrcpy nur in VMs funktionieren, die phyischen Zugriff auf den USB-Controller haben. Also hat man als Qubes-Benutzer folgende Optionen:

1. scrcpy in sys-usb einrichten und von dort aus bedienen.
2. Wenn man mehr als einen USB-Controller besitzt, dann ist es möglich eine eigene VM einrichten und in der scrcpy installieren.

Mit der 2. Option verliert man für sys-usb einige USB-Ports, allerdings bleibt weiterhin jedwediger, wenn auch theortischer, Netzerkzugriff für sys-usb verwehrt.
