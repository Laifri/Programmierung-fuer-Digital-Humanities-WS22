#Reguläre Ausdrücke = Sprache für Suchanfrage in Strings
#Wiederholungsoperatoren:
#"a" -> sucht nach allen Vorkommen von a im Text, auch Teilwörter
#"a*" -> sucht nach beliebig vielen Wiederholungen von "a", auch 0 Wiederholungen  = a, aa, aaa
#"a+" -> sucht nach beliebig vielen, aber mindestens einer Wiederholung von a = a, aa, aaa
#"Klauseln?" -> behandelt n als optional. n darf 1mal oder 0mal vorkommen = a, A, aA, AaaAaaaAAaa

#Klammern:
#[Aa] -> sucht nach mindestens einem Element, was innerhalb der Klammern steht
#(peter)+ -> sucht nach dem Wort Peter, mehrere male aber mindestens 1mal

#Beispiele:
#[A-Z][a-z] -> Abkürzungen aller Buchstaben von A bis Z -> Alle Zeichenketten die mit genaue einem Großbuchstaben beginnen u dann alle Kleinbuchstaben
#[A-Z]+ -> Suche nach allen Zeichenketten, nur aus Großbuchstaben bestehen
#"Bäcker(in)? -> Suche nach allen Zeichenketten die mit Bäcker anfangen u. dann entweder 1 mal in oder kein in am Ende haben

#Bachslash:
#"\?" -> sucht nach vollkommen von ? im Text
#[\(\)[\]] -> sucht nach einem von vier Zeichen ( ) [ ]
#Abkürzungen:
#\w -> matched alles was ein Groß u Kleinbuchstaben oder Zahl
#\s -> machted alles was ein Leerzeichen ist
#\b -> matched am Wortanfang und Ende
#\W -> mached alles was KEIN Groß/Kleinbuchstaben oder eine Zahl ist
#\S -> machted alles was KEIN Leerzeichen ist

#. -> matcht ein beliebiges Zeichen
#^ -> bedeutet normalerweise Zeilenanfang
#[^A-Z] -> innerhalb eckiger Klammern bedeutet ^ "nicht". Also hier wird alles gematcht, was kein Großbuchstabe von A-Z ist
#$ -> bedeutet Zeilenende
#| -> bedeutet "oder"

import re
suchtext = "Geboren bin ich am 12.02.2001 in den USA. Und Sie?" #Alle Großgeschriebenen Wörter finden
matches = re.findall(r"[A-Z[a-z]*", suchtext) #findall gibt Liste mit allen Matches zurück
print(matches) #= ['Geboren', '', 'bin', '', 'ich', '', 'am', '', '', '', '', '', '', '', '', '', '', '', '', 'in', '', 'den', '', 'USA', '', '', 'Und', '', 'Sie', '', '']
matches = re.findall(r"[A-Z]+[a-z]*", suchtext) #mindestens ein Großbuchstabe, dann beliebig viele Kleinbuchstaben
print(matches)
