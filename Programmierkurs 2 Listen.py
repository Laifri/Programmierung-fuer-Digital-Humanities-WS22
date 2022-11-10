#Listen = Datenstrukturen = Reihenfolge von eingespeicherten Elementen, Listen sind sehr flexibel
#Definition einer Liste = Eckige Klammern! [element1, element2, element3]
#Damit man die Liste benutzen kann muss man sie als Variabel speichern = meine_liste=[element1...]

satzliste0=["Hallo","Wie geht es dir?","Tschüss!"]
#Liste mir drei Strings, getrennt durch Komma

print(satzliste0[0]) #Position 0 ist Hallo -> Man fängt immer an mit 0 zu zählen
print(satzliste0[2]) #Postiion 3
#Wenn man was printen kann, kann man auch alles andere daraus machen

#Andere Möglichkeit:
satz11 = "Hi!"
satz21 = "Was geht heute?"

satzliste_neu = [satz11,satz21]
print(satz21)

#Warum Listen? Um Variabeln in einer Variabel zu speichern, sehr wichtig wenn man vorher nicht genau weiß wieviel
#Variabeln man braucht

#Beispiel:
satz1 = "Der Hund bellt heute nicht im Garten sondern im Hof." #string: beliebige anzahl von zeichen
satz2 = "Die Katze schleicht morgens zum Nachbarn."
satz3 = "Vielleicht genehmige ich mir heute Abend Lebkuchen"

#Split Funktion mit String .
#Zahlen, Anzahl der Wörter im Satz, Satzzeichen gelten auch als Wort
#woerter1 = 8 #Punkt zählt auch als Wort
#woerter2 = 7
#woerter3 = 8 #Integer: Ganze Zahl, Kommazahlen: Float
#Wir müssen Wörter manuell zählen, das ist doof, Automatisierung:
#Basic rudimentäre Tokensierung mit split() mit .
satz1_tokens = (satz1.split(" ")) #Mit Leerzeichen=Bei jedem Leerzeichen wird gesplittet
satz2_tokens = (satz2.split(" "))
satz3_tokens = (satz3.split(" "))
tokensliste = [satz1_tokens,satz2_tokens,satz3_tokens]
#Anzahl der Wörter bzw. Tokens ist die Länge der Liste satz1_tokens
woerter1 = len(satz1_tokens)
woerter2 = len(satz2_tokens)
woerter3 = len(satz3_tokens)


#Anzahl der Wörter in allen Sätzen zusammen
woerter_gesamt = woerter1 + woerter2 + woerter3 #dazu neue Variabel

#Durchschnittliche Anzahl der Wörter pro Satz = Durschnittl. Summe ais allen Elementen/Anzahl der Elemente
woerter_durchschnitt = woerter_gesamt / 3

#Alle Sachen in Listen speichern:
satzliste = [satz1,satz2,satz3]
woerterliste = [woerter1,woerter2,woerter3]
print(satzliste[0], "Anzahl Wörter:", woerterliste[0])
print(satzliste[1],"Anzahl Wörter:", woerterliste[1])
print(satzliste[2],"Anzahl Wörter:", woerterliste[2])

#len() funktion: Gibt länge einer Liste aus
print("Anzahl Sätze:",len(satzliste))
print("Wörter Durschnitt:",woerter_durchschnitt)

