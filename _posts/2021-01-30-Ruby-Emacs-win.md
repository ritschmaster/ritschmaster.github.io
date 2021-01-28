---
layout: post
title:  Shell-Skript über markierte Zeilen im Editor ausführen
author: Richard Bäck
---

Ich hab seit Jahren immer wieder die notwendig kleine Formatierungen oder Zeichenkettenabänderungen mit Emacs durchzuführen. Bisher hab ich das entweder über [Vim Makros](https://vim.fandom.com/wiki/Macros) oder über Vims Visual Block (beide Funktionalitäten werden mit [Evil](https://github.com/emacs-evil/evil) in Emacs bereitgestellt) erledigt. Allerdings nervte es mich in letzter Zeit mehr, dass ich eigentlich immer und immer wieder die **gleichen** Anweisungen wieder als Makro hinterlegen musste.

Ein Beispiel: in meiner Arbeit in SAP brauche ich sehr oft Attributsnamen von Strukturen für die Zuweisung von Literalen. Die Attributsnamen kann ich sehr einfach markieren und in Emacs einfügen. Allerdings brauche ich dann Visual Block um die Zeile entsprechend vorzubereiten um nur noch die tatsächliche Variable einzufügen.

D.h. aus

    MATNR
    MTART
    MATKL
    
wird mit der Hilfe von Makros:

    -MATNR = ''.
    -MTART = ''.
    -MATKL = ''.
    
damit ich dann schlussendlich manuell nur mehr den Variablennamen und den Wert des Literals einfügen muss:

    LS_MARA-MATNR = 'TEST_MATERIAL.
    LS_MARA-MTART = 'FERT'.
    LS_MARA-MATKL = '1111'.

Allerdings muss ich jeden Tag das Makro von neuem definieren. Und im schlimmsten Fall sogar mehrmals am Tag, da ich mir nicht merke, auf welche Tastenbelegung ich mir das Makro gelegt habe.

Daher habe ich angefangen mir zu überlegen die Emacs Funktion [SHELL-COMMAND-ON-REGION](https://www.gnu.org/software/emacs/manual/html_node/emacs/Single-Shell.html#Single-Shell) in meine tägliche Arbeit einzubauen. Diese ermöglicht es einen markierten Text in Emacs an ein beliebiges Shell-Kommando zu senden und die Ausgabe wieder in Emacs zu empfangen. Damit erhält man eine Brücke zwischen zwei mächtige Welten: die Welt der Emacs-Funktionen und die Welt der Shell-Pipes.

So viel zur Überlegung. Aber wie sieht die Theorie in der Praxis aus? 

Das obige Beispiel kann nun mit einer Markierung über den Text, den Tastenkombinationen <kbd>C-u</kbd> <kbd>M-x</kbd>, dem Befehl `SHELL-COMMAND-ON_REGION` und dem finalen Skript `ruby -lne 'print "-", $_, " = '\'\''."'` erledigt werden.

Doch das tut immer noch weh! Inbesondere so viele Sonderzeichen einzutippen! Deshalb hab ich die gesamte Sequenz in eine eigene Elisp-Funktion gepackt. Die sieht so aus:

    (defun my/to-abap-assign-literal-on-region ()
        (interactive)
        (shell-command-on-region (region-beginning)
                                 (region-end)
                                 "ruby -lne 'print \"-\", $_, \" = '\\'\\''.\"'"
                                 (current-buffer)
                                 t))

Damit muss ich nun nur mehr <kbd>C-u</kbd> <kbd>M-x</kbd> und dem Befehl `MY/TO-ABAP-ASSIGN-LITERAL-ON-REGION` über die markierten Zeilen ausführen.

Dieser kleine Hack kann aber sicherlich auch in anderen Editoren auch umgesetzt werden. Emacs ist mir nur am nächsten.
