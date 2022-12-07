#Bauen Sie die tokenize-Funktion aus der Vorlesung nach:
#Lesen sie die Datei "corona_twitter.txt" ein und speichern Sie die einzelnen Sätze als Liste.
#Erweitern Sie die tokenize-Funktion um mindestens eine der Möglichkeiten:
#-Der Tokenizer soll mindestens 2 weitere Sonderzeichen am Wortende erkennen, die in den Sätzen auftauchen.
#-Der Tokenizer soll mindestens 3 Sonderzeichen am Satzanfang erkennen, die in den Sätzen vorkommen. Zum Beispiel: "(Kansas)" -> ["(", "Kansas", ")"]
def tokenize(satz):
    tokens = satz.split(" ")
    new_tokens = []

    for token in tokens:
        if token == "":
            continue
        sonderzeichen = {"#","@"} #Dies hab ich nachträglich angefügt um zu probieren ob es auch so funktioniert
        if token[-1] == ".":
            new_token = token[:-1]
            punkt = token[-1]
            new_tokens.append(new_token)
            new_tokens.append(punkt)
        elif token[0] in sonderzeichen:
            new_tokens.append(token[0])
            new_tokens.append(token[1:])
        elif token[-1] == "?":
            new_token = token[:-1]
            fragezeichen = token[-1]
            new_tokens.append(new_token)
            new_tokens.append(fragezeichen)
        elif token[0] == "(" and token[-1] == ")":
            new_tokens.append(token[0])
            new_tokens.append(token[1:-1])
            new_tokens.append(token[-1])
        elif (token[0] == "("):
            new_tokens.append(token[0])
            new_tokens.append(token[1:])
        elif (token[-1] == ")"):
            new_tokens.append(token[:-1])
            new_tokens.append(token[-1])
        elif (token[0] == "#"):
            new_tokens.append(token[0])
            new_tokens.append(token[1:])
        elif (token[-1] == "!"):
            new_tokens.append(token[:-1])
            new_tokens.append(token[-1])
        elif (token[-1] == ":"):
            new_tokens.append(token[:-1])
            new_tokens.append(token[-1])
        else:
            new_tokens.append(token)
    return new_tokens

twitter_daten = open("corona_twitter.txt", "r", encoding="utf8").read().split("\n")[:100] #ersten 100 Sätze

#Ermitteln Sie die durchschnittliche Anzahl von Tokens für alle Sätze, verwenden Sie zum Tokenisieren nun die zuvor implementierte tokenize-Funktion.
def count_tokens(satz):
    woerter = tokenize(satz)
    return len(woerter)
def durchschnitt_tokens(saetze):
    token_gesamt = 0
    for satz in saetze:
        anzahl_token = count_tokens(satz)
        token_gesamt += anzahl_token
    return token_gesamt/len(saetze)
print("Durschnittliche Wortzahl:", durchschnitt_tokens(twitter_daten))

#Testen Sie zum Schluss ihre Abgabe!
for line in twitter_daten:
    tokens = tokenize(line)
    print(tokens)