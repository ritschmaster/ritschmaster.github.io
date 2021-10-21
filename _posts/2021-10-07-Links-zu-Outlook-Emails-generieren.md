---
layout: post
title:  Links zu Outlook Emails generieren
author: Richard Bäck
---

Empfangene E-Mails sind meist ein Anstoß etwas bestimmtes zu tun. In der Software (Individual) Entwicklung ist bedeutet eine E-Mail meistens einen Fehler beheben oder nach Rücksprache mit Kollegen einen Termin für eine Neuerung festlegen. In der Welt der org-mode Benutzer bedeutet das zumindest ein neuer TODO Gegenstand.

Wäre es da nicht wahnsinnig vorteilhaft, wenn man in seinen org-mode Notizen direkt auf die ursprüngliche E-Mail verweisen könnte?

Auf diese Idee bin tatsächlich gar nicht ich gekommen. Ich hab mich bisher mit immer wieder suchen begnügt. Bei meiner Odyssee Outlook mit Emacs zu ersetzen bin ich zufällig auf diese Idee gestoßen. Ich finde sie aber so gut, dass ich sie teilen möchte.

Das Ziel ist sehr simpel: mit einem Knopf kann der Link zu einer E-Mail generiert werden. Dieser kann dann beliebig in org-mode platziert werden. Klickt man darauf, dann landet man in Outlook, bei der exakten E-Mail.

# Outlook Anpassung

1. Outlook starten
2. "Menüband anpassen" - Das kann über das Dreieck Symbol rechts unten in der Werkzeugleiste erreicht werden
3. Die Entwickler Werkzeuge einschalten und diese Optionen mit "OK" schließen 
   ![Entwicklertools einschalten](/assets/links-zu-outlook-emails-generieren/1_entwickertools_einschalten.png)
4. Entwicklertools > Makros > Makros
5. Neues Makro anlegen - den Namen der einfachheithalber gleich lassen
   ![Makro anlegen](/assets/links-zu-outlook-emails-generieren/2_makro_anlegen.png) 
6. Unter bearbeiten den folgenden Quellcode einfügen:

        Sub AddLinkToMessageInClipboard()
            Dim objMail As Outlook.MailItem
            Set doClipboard = CreateObject("New:{1C3B4210-F441-11CE-B9EA-00AA006B1A69}")
                
            'One and ONLY one message must be selected
            If Application.ActiveExplorer.Selection.Count <> 1 Then
                MsgBox ("Select one and ONLY one message.")
                Exit Sub
            End If
            
            Set objMail = Application.ActiveExplorer.Selection.Item(1)
            doClipboard.SetText "[[outlook:" + objMail.EntryID + "][MESSAGE: " + objMail.Subject + " (" + objMail.SenderName + ")]]"
            doClipboard.PutInClipboard
        End Sub
7. Speichern
8. Noch einmal in "Menüband anpassen" wechseln
9. Unter _Start (E-Mail)_ eine neue Kategorie _org-mode_ anlegen. Darin kann dann aus der Befehlskategorie _Makros_ das oben erzeugte Makro platziert werden
   ![Makro erreichbar machen](/assets/links-zu-outlook-emails-generieren/3_makro_erreichbar_machen.png)

Damit ist der Outlook Teil erledigt! Jedes Mal, wenn eine E-Mail nun verknüpft werden soll, dann kann das Makro verwendet werden.

Tipp: mit <kbd>Alt-h</kbd> kann die gesamte Werkzeugleiste mit der Tastatur bedient werden. Daher auch das neue Makro!

# Emacs Anpassung

1. Paket "org-outlook" installieren
2. In `.emacs` die folgende Konfiguration hinterlegen:

    (require 'org-outlook)
   
    ; Pfad bitte entsprechend anpassen!
    (setq org-outlook-location "C:/Program Files (x86)/Microsoft Office/root/Office16/OUTLOOK.exe")

Nun kann der generierte Link in `.org` Dateien eingefügt werden. Das verwenden von <kbd>Enter</kbd> auf einem Link öffnet automatisch Outlook mit der verlinkten E-Mail.
