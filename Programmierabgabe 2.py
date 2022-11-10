#Speichern Sie alle Sätze in einer Liste.
satz1 = "Am liebsten esse ich Apfelkuchen."
satz2 = "Gestern gab es zum Abendessen Thailändisches Pad Thai."
satz3 = "Die Maultaschen mag ich gebraten mit Feldsalat."
satzliste = [satz1,satz2,satz3]

#Erstellen Sie für jeden Satz eine Liste von Tokens mit der "split()"-Funktion und speichern sie die Ergebnisse in einer neuen Liste.
satz1_tokens = (satz1.split(" "))
satz2_tokens = (satz2.split(" "))
satz3_tokens = (satz3.split(" "))
tokensliste = [satz1_tokens,satz2_tokens,satz3_tokens]

#Speichern Sie alle Anzahlen von Tokens in einer Liste, indem sie die Länge der jeweiligen Liste von Tokens mit der "len()"-funktion bestimmen.
woerter_satz1 = len(satz1_tokens)
woerter_satz2 = len(satz2_tokens)
woerter_satz3 = len(satz3_tokens)
woerterliste = [woerter_satz1,woerter_satz2,woerter_satz3]

#Geben Sie jeden Satz, gefolgt von der Liste der Tokens und der Anzahl der Tokens aus.
print(satzliste[0],tokensliste[0],"Anzahl Wörter:", woerterliste[0])
print(satzliste[1],tokensliste[1],"Anzahl Wörter:", woerterliste[1])
print(satzliste[2],tokensliste[2],"Anzahl Wörter:", woerterliste[2])

#Geben Sie durchschnittliche Anzahl der Tokens von allen Sätzen aus
woerter_gesamt = woerter_satz1 + woerter_satz2 + woerter_satz3
woerter_durschnitt = woerter_gesamt / len(woerterliste)
print("Durschnittliche Anzahl an Wörtern:",woerter_durschnitt)

