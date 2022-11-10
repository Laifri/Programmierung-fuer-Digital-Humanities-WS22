#Speichern Sie alle Sätze in einer Liste:
#Erstellen Sie 3 weitere Sätze und fügen Sie sie der Liste hinzu, fügen Sie auch der Liste mit Tokens die entsprechenden Zahlen hinzu:
satz1 = "Ich gehe ins Kino"
satz2 = "Ich wohne in Stuttgart"
satz3 = "Freitags habe ich frei"
satz4 = "Es ist 9 Uhr"
satz5 = "Beeil dich bitte !"
satz6 = "Wohin gehst du ?"
satzliste = [satz1,satz2,satz3,satz4,satz5,satz6]

#Speichern Sie alle Anzahlen von Tokens in einer Liste:
satz1_tokens = satz1.split(" ")
satz2_tokens = satz2.split(" ")
satz3_tokens = satz3.split(" ")
satz4_tokens = satz4.split(" ")
satz5_tokens = satz5.split(" ")
satz6_tokens = satz6.split(" ")
tokensliste = [satz1_tokens,satz2_tokens,satz3_tokens,satz4_tokens,satz5_tokens,satz6_tokens]

woerter_satz1 = len(satz1_tokens)
woerter_satz2 = len(satz2_tokens)
woerter_satz3 = len(satz3_tokens)
woerter_satz4 = len(satz4_tokens)
woerter_satz5 = len(satz5_tokens)
woerter_satz6 = len(satz6_tokens)
woerterliste = [woerter_satz1,woerter_satz2,woerter_satz3,woerter_satz4,woerter_satz5,woerter_satz6]

#Nutzen Sie Schleifen, um jeden Satz und dann jede Anzahl von Tokens auszugeben:
for satz in satzliste:
    print("Der Satz lautet:",satz)

for woerter in woerterliste:
    print("Dieser Satz hat eine Anzahl von",woerter,"Tokens")

#Nutzen Sie eine Schleife, um die Summe der Tokens in allen Sätzen zu berechnen und geben Sie das Ergebnis aus:
woerter_gesamt = 0
for woerter in woerterliste:
    woerter_gesamt = woerter_gesamt + woerter
print("Die Gesamtanzahl der Tokens beträgt:",woerter_gesamt)

#Berechnen Sie die durchschnittliche Anzahl von Tokens pro Satz aus der Summe der Tokens und der Länge der Liste:
woerter_durchschnitt = woerter_gesamt / len(woerterliste)
print("Im Durchschnitt haben die Sätze",woerter_durchschnitt,"Tokens")

#Geben sie das Ergebnis aus
print("Anzahl Sätze:", len(satzliste))

#OPTIONAL: Automatisieren Sie die Anzahl der Wörter pro Satz, indem sie mithilfe einer Schleife die Funktionen '.split()' und 'len()' verwenden:
#split = Split a string into a list//len = Return the number of items in a list//mit append = Adding List to a List

for satz in satzliste:
   tokens = satz.split(" ")
   tokensliste.append(tokens)
   woerter = len(tokens)
   woerterliste.append(woerter)

#Ausgabe:
print(satzliste)
print(woerterliste)

#oder:
satzliste.append(woerterliste)
print(satzliste)

#oder:
for satz in satzliste:
    print(satz)
    print("Anzahl Tokens von diesem Satz:" , len(tokens))