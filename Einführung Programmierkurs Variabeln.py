#Variabeln
#Name der Variabel = Daten, jede Variabel hat nur eine Anzahl von Daten, bei zweimal satz wird der erste Satz überschrieben
#Sätze
#Gleichzeichen ist eine Zuweisung
satz1 = "Der Hund bellt im Garten." #string: beliebige anzahl von zeichen
satz2 = "Die Katze schleicht morgends zum Nachbarn."
satz3 = "Vielleicht genehmige ich mir heute Abend Lebkuchen"

#Zahlen, Anzahl der Wörter im Satz, Satzzeichen gelten auch als Wort
woerter1 = 6 #Punkt zählt auch als Wort
woerter2 = 7
woerter3 = 8 #Integer: Ganze Zahl, Kommazahlen: Float

#Anzahl der Wörter in allen Sätzen zusammen
woerter_gesamt = woerter1 + woerter2 + woerter3 #dazu neue Variabel

#Durchschnittliche Anzahl der Wörter pro Satz = Durschnittl. Summe ais allen Elementen/Anzahl der Elemente
woerter_durchschnitt = woerter_gesamt / 3

print(satz1) #zum ausgeben von Satz
print("Anzahl Wörter:", woerter1)
print(satz2)
print("Anzahl Wörter:", woerter2)
print("Wörter gesamt:", woerter_gesamt)
print("Durschnittliche Anzahl der Wörter pro Satz:", woerter_durchschnitt)