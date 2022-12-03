#def tokenize(satz):
 #   tokens = satz.split(" ")
  #  new_tokens = []

def tokenize(satz):
    tokens = satz.split(" ")
    new_tokens = []

    for token in tokens:
        if token == "":
            continue #Ignoriert den restlichen Code aus der Schleife und geht direkt in die nächste über
        # Hat das Token ein Punkt am Ende?
        if token[-1] == ".":
            new_token = token[:-1]
            punkt_token = token [-1]
            new_tokens.append(new_token)
            new_tokens.append(punkt_token)
        elif (token[0] == "("):
            new_tokens.append(token[0])
            new_tokens.append(token[1:])
        else:
            new_tokens.append(token)
    return new_tokens

twitter_daten = open("corona_twitter.txt", "r", encoding="utf8").read().split("\n")[:10] #ersten 100 Sätze

for line in twitter_daten:
    tokens = tokenize(line)
    print(tokens)







#Bauen Sie die tokenize-Funktion aus der Vorlesung nach.

#--Für die folgenden 2 Schritte können Sie gerne die vorherige Abgabe erneut benutzen--

#Lesen sie die Datei "corona_twitter.txt" ein und speichern Sie die einzelnen Sätze als Liste.

#Ermitteln Sie die durchschnittliche Anzahl von Tokens für alle Sätze, verwenden Sie zum Tokenisieren nun die zuvor implementierte tokenize-Funktion.

#---

#Erweitern Sie die tokenize-Funktion um mindestens eine der drei folgenden Möglichkeiten:

#-Der Tokenizer soll mindestens 2 weitere Sonderzeichen am Wortende erkennen, die in den Sätzen auftauchen.

#-Der Tokenizer soll mindestens 3 Sonderzeichen am Satzanfang erkennen, die in den Sätzen vorkommen. Zum Beispiel: "(Kansas)" -> ["(", "Kansas", ")"]

#-Der Tokenizer soll die Abkürzungen n't und 's erkennen und entsprechend abtrennen. Zum Beispiel: "isn't" -> ["is", "n't"]

#Testen Sie zum Schluss ihre Abgabe!