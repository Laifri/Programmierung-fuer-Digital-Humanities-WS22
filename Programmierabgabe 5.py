#Lesen Sie die Datei "corona_twitter.txt" ein und speichern Sie den Inhalt der Datei als Liste einzelner Sätze.
#Speichern Sie die Anzahl der Tokens für jeden Satz in einer neuen Liste (dafür ist es in dieser Abgabe ausreichend 'split()' zu verwenden)
twitter_daten = open("corona_twitter.txt", "r", encoding="utf8").read().split("\n")


#Geben Sie die Anzahl der Sätze aus.
saetze_gesamt = [len(twitter_daten)]
print(saetze_gesamt)

#Geben Sie die durchschnittliche Anzahl von Wörtern pro Satz aus.
token_gesamt =


#Schreiben Sie alle Sätze, die mehr Tokens haben als der Durchschnitt in eine neue Datei.

#Schreiben Sie alle Sätze, die weniger Tokens haben als der Durchschnitt in eine weitere Datei.

#Geben Sie die Anzahl der jeweiligen Sätze (mehr als Durchschnitt, weniger als Durchschnitt) aus.

#Suchen Sie sich drei Schlagwörter, die in den Tweets oft vorkommen könnten. Schreiben Sie alle Sätze, die mindestens eines dieser Wörter enthalten in eine neue Datei. Denken Sie daran, die Sätze nicht mehrmals in die Datei zu schreiben, auch wenn sie mehrere Schlagwörter enthalten.

#Geben Sie die Anzahl dieser Sätze, sowie die Schlagwörter aus.