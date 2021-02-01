---
layout: post
title:  Dokumentation mit Ruby-Skript gemeinsam ausliefern
author: Richard Bäck
---

Ich suche schon eine längere Zeit nach einer Skript Sprache mit der ich Alltagsprobleme schnell lösen kann und die etwas einfacher zu verwenden ist für komplexe Probleme als die [Bash](https://www.gnu.org/software/bash/). Was meine ich mit komplexe Probleme: zB Daten einer CSV an einen Web-Dienst zu senden. Das ist zwar möglich mit Bash, allerdings doch etwas schwerfälliger als mit anderen Programmiersprachen. Nachdem ich Perl betrachtet habe, schaue ich mir nun Ruby an.

Ruby ist eine grandiose Programmiersprache für kleine und große Probleme. [ri](https://ruby.github.io/rdoc/RI_rdoc.html) gibt dem Entwickler ein super Werkzeug in die Hand um schnell die Klassen im Ruby-Standard und in den installierten [gem](https://de.wikipedia.org/wiki/RubyGems)-Paketen zu durchforsten. Will man selber eine Dokumentation schreiben, die durch `ri` gelesen werden kann, dann ist das auch sehr einfach mit [rdoc](https://ruby.github.io/rdoc/RI_rdoc.html) oder [yard](https://yardoc.org/) lösbar.

Doch so vorteilhaft die Existenz und Idee von `ri` ist, hat es ein Feature nicht: eine einfach aufrufbare Dokumentation aus Benutzersicht zu einem Ruby-Skript. Denn bevor `ri` verwendet werden kann, muss mit einem anderen Werkzeug das Dokument erzeugt werden, dass betrachtet werden kann. Das schafft eine unnötige Hürde, wenn es nur drum geht ein sehr, sehr spezielles Problem zu lösen und für die Nachwelt die Nutzung der Applikation zu dokumentieren.

Der Ansatz von Perl dagegen ist da schon fast magisch! Mit [POD](https://de.wikipedia.org/wiki/Plain_Old_Documentation) und [perldoc](https://perldoc.perl.org/) ist es möglich ein [man](https://de.wikipedia.org/wiki/Manpage)-ähnliches Dokument direkt in der Applikation zu platzieren und somit auch mit diesem auszuliefern. Einfach und genial zu gleich. Denn es ist weder ein [Makefile](https://de.wikipedia.org/wiki/Make) noch eine andere zusätzliche Datei für die Applikation notwendig!

Geht das nicht vielleicht auch in Ruby? Die Antwort: Ja!

Und wie? In dem man sich das Schlüsselwort [__END__](https://idiosyncratic-ruby.com/74-super-snakes.html#end-at-beginning-of-line) zu nutze macht. Mit diesem kann man nicht ausführbare Daten in einem Ruby-Skript mit ausliefern.

Das kann dann so in einem `hello.rb` aussehen:

    #!/usr/bin/env ruby
    
    print "Hello world\n"
    
    __END__
    
    =pod
    
    =encoding utf8
    
    =head1 NAME
    
    hello - A hello world application written in Ruby
    
    =head1 SYNOPSIS
    
    hello [options] file
    
    =head1 DOCUMENTATION
    
    The purpose of this application is to show a hello world message. Additionally the usage of POD (Plain Old Documentation) is shown with it.
    
    =head1 AUTHOR
    
    Richard Bäck
   
    =cut
    
Wenn nun `perldoc hello.rb` ausgeführt wird, dann erhält man eine wunderschöne `man`-ähnliche Dokumentation der Applikation!
