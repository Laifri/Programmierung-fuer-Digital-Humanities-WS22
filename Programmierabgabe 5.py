#Lesen Sie die Datei "corona_twitter.txt" ein und speichern Sie den Inhalt der Datei als Liste einzelner Sätze.
twitter_daten = open("corona_twitter.txt","r", encoding="utf8").read().split("\n")

#Speichern Sie die Anzahl der Tokens(Wörter) für jeden Satz in einer neuen Liste (dafür ist es in dieser Abgabe ausreichend 'split()' zu verwenden)
anzahl_token = []
for satz in twitter_daten:
    anzahl_token.append(len(satz.split(" "))) #Append=Anhängen

#Geben Sie die Anzahl der Sätze aus.
saetze_gesamt = len(twitter_daten)
print("Anzahl der Sätze:", saetze_gesamt)

#Geben Sie die durchschnittliche Anzahl von Wörtern pro Satz aus. = Anzahl Wörter / Anzahl  Sätze
#Anzahl Sätze = saetze.gesamt
woerter_gesamt = sum(anzahl_token) #Liste summieren = Jede Zahl in der Liste zusammenzählen
durchschnitt_Wörter =woerter_gesamt/saetze_gesamt
print("Durchschnittliche Anzahl Wörter:",durchschnitt_Wörter)

#Schreiben Sie alle Sätze, die mehr Tokens haben als der Durchschnitt in eine neue Datei.
dateipfad  = "Sätze_mehr_als_Durchschnitt.txt"
datei = open(dateipfad, "w",encoding="utf8")
saetze_mehr_Durchschnitt = []
for saetze in twitter_daten:
    if len(saetze) > 18:
        datei.write(saetze+"\n")
        saetze_mehr_Durchschnitt.append(saetze)

#Schreiben Sie alle Sätze, die weniger Tokens haben als der Durchschnitt in eine weitere Datei.
dateipfad_2 = "Sätze_weniger_als_Durschnitt"
datei_2 = open(dateipfad_2, "w", encoding="utf8")
saetze_weniger_Durchschnitt = []
for saetze in twitter_daten:
    if len(saetze.split()) < 18: #Korrektur von len(saetze)
        datei_2.write(saetze+"\n")
        saetze_weniger_Durchschnitt.append(saetze)

#Geben Sie die Anzahl der jeweiligen Sätze (mehr als Durchschnitt, weniger als Durchschnitt) aus.
print("Anzahl der Sätze die mehr Wörter als der Durschnitt haben:",len(saetze_mehr_Durchschnitt))
print("Anzahl der Sätze die weniger Wörter als der Durschnitt haben:",len(saetze_weniger_Durchschnitt))

#Suchen Sie sich drei Schlagwörter, die in den Tweets oft vorkommen könnten. Schreiben Sie alle Sätze, die mindestens
#eines dieser Wörter enthalten in eine neue Datei. Denken Sie daran, die Sätze nicht mehrmals in die Datei zu schreiben,
#auch wenn sie mehrere Schlagwörter enthalten.
dateipfad_3 = "Schlagwörter"
datei_3 = open(dateipfad_3, "w", encoding="utf8")
schlagwoerter_saetze = []
maskcounter = 0
covidcounter = 0
viruscounter = 0
for saetze in twitter_daten:
    if saetze.find("mask") > 0:
        datei_3.write(saetze + "\n")
        schlagwoerter_saetze.append(saetze)
        maskcounter += saetze.count("mask")
    elif saetze.find ("covid") > 0:
        datei_3.write(saetze + "\n")
        schlagwoerter_saetze.append(saetze)
        covidcounter += saetze.count("covid")
    elif saetze.find ("virus") > 0:
        datei_3.write(saetze + "\n")
        schlagwoerter_saetze.append(saetze)
        viruscounter += saetze.count("virus")
#Geben Sie die Anzahl dieser Sätze, sowie die Schlagwörter aus.
print("Anzahl der Schlagwörter:", (maskcounter)+(covidcounter)+(viruscounter))
print("Anzahl Sätze mit den Schlagwörter:'mask' und/oder 'covid' und/oder 'virus':", len(schlagwoerter_saetze))