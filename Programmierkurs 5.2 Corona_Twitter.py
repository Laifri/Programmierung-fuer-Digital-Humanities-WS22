#To Do:
#Liste von Sätzen einlesen
#Vergleichen mehrere Listen mit dem Index
#Wörter suchen mit "in"
#In neue Dateien schreiben

twitter_daten = open("corona_twitter.txt", "r", encoding="utf8").read().split("\n")
#print(twitter_daten)
#print(type(twitter_daten))

satzliste = ["Guten Tag", "hi", "moooin"]
tokensliste = [2, 1, 1]

#Ansatz um mehrere Tokens zu integrieren
index = 0
#for satz in satzliste:
#    print(satz)
#    print(tokensliste[index])
#    index += 1

#Wörter in String finden
#for satz in satzliste:
#    if "a" in satz:
#       print("Ein A in Satz:", satz)

twitter_daten = open("corona_twitter.txt", "r" ,encoding="utf8").read().split("\n")[:100]
#List Slice [:100] = Von der Liste die ersten 100 Elemente
for satz in twitter_daten:
    if "a" in satz.lower(): #Tip wegen lowercase/uppercase
        print(satz)

result_file = open("twitter_ergebnis.txt", "w", encoding="utf8")
print(twitter_daten)