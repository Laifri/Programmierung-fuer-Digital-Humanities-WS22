#Lesen Sie die Datei "corona_twitter.txt" ein und speichern sie alle Sätze in einer Liste.
twitter_daten = open("corona_twitter.txt", "r", encoding="utf8").read().split("\n")[:100] #ersten 100 Sätze

#Erstellen Sie jeweils eine Funktion, die:
#-einen String als Parameter nimmt und die Anzahl der Tokens (mit split() zurückgibt).
def count_tokens(satz):
    basic_token = satz.split() #Wenn nichts in Split steht wird auch bei Leerzeichen getrennt
    return len(basic_token)
#for line in twitter_daten:
 #   print(count_tokens(line))

#-eine Liste von Strings als Parameter nimmt und die durchschnittliche Wortanzahl pro Satz zurückgibt. = Alle Wörter / 100
def durchschnitt_tokens(saetze):
    token_gesamt = 0
    for satz in saetze:
        anzahl_token = count_tokens(satz)
        token_gesamt += anzahl_token
    return token_gesamt/len(saetze)
#print("durschnittliche Wortzahl:", durchschnitt_tokens(twitter_daten))

#-eine Liste von Strings, sowie ein einzelnes Schlüsselwort (auch als String) als Parameter entegennimmt und alle Strings
#in einer Liste zurückgibt, die dieses Schlüsselwort enthalten.
def saetze_schluesselwort(saetze,schluesselwort):
    schluesselwort_saetze = []
    for satz in saetze:
        if satz.find(schluesselwort) > 0:
            schluesselwort_saetze.append(satz)
    return schluesselwort_saetze
#print(saetze_schluesselwort(twitter_daten,"mask"))

#-eine Liste von Strings, sowie einen Dateipfad (als String) als Parameter nimmt und alle Strings aus der Liste in eine neue Datei mit dem Dateipfad schreibt.
def dateipfad(liste,dateipfad):
    datei = open(dateipfad, "w", encoding="utf8")
    for saetze in liste:
        datei.write(saetze+"\n")
#dateipfad(twitter_daten,"Twitter_Daten_Kopie")

#Schreiben Sie alle Sätze, die eines von 3 selbstgewählten Schlüsselwörtern enthalten in eine neue Datei.
def schluesselwoerter_dateipfad(liste,schluesselwort_1,schluesselwort_2,schluesselwort_3,dateipfad):
    datei= open(dateipfad,"w",encoding="utf8")
    for saetze in liste:
        if saetze.find(schluesselwort_1) > 0:
            datei.write(saetze+"\n")
        elif saetze.find(schluesselwort_2) > 0:
            datei.write(saetze+"\n")
        elif saetze.find(schluesselwort_3) > 0:
            datei.write(saetze+"\n")
#schluesselwoerter_dateipfad(twitter_daten,"mask","corona","covid","SchlüsselwörterDatei")

#Schreiben Sie alle Sätze, die weniger Tokens haben, als der Durchschnitt in eine neue Datei.
def saetze_weniger_durchschnitt(saetze,dateipfad):
    datei= open(dateipfad,"w",encoding="utf8")
    durchschnitt = durchschnitt_tokens(saetze)
    for satz in saetze:
        if count_tokens(satz) < durchschnitt:
            datei.write(satz+"\n")
#saetze_weniger_durchschnitt(twitter_daten,"SätzeWenigerDurchi")