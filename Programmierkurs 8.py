#Libraries/Bibliotheken
#import sys #=wir wollen diese Library mit dem Namen im Code verwenden
#sys.exit() #um etwas aus der importierten Library zu verwenden / Exit ist um die Library zu beenden

import nltk
satz = "the fisch in the barrel"
tokens = nltk.word_tokenize(satz) #so können wir mit nltk einfach tokenisieren
print(tokens)

from collections import Counter
tokens2 = ["the", "dog", "in", "the", "yard"]
tokens2_count = Counter(tokens2)
print(tokens2_count) # = Counter({'the': 2, 'dog': 1, 'in': 1, 'yard': 1})

common_words = tokens2_count.most_common(1) # = 1 steht für: gibt zurück das eine häufigste Wort
print(common_words) # = the, 2

#Datenstrukturen:
# Tupel:
t1 = (10, 20, 50, 80, 100) #Tupel erkennt man an runden Klammern
print(t1)
t2 = (20, "party", ["a", "b", "c"]) #Tupel können beliebige Elemente haben mit int, string und liste
print(t2[0])

#Set (Menge)
m1 = {10, 20, 50, 80}
#Mengen können immer nur einmal vorkommen
m1.add(120)
print(m1)
I = ["the", "fisch"]
I_unique = set(I) #Damit verwandeln wir eine Liste in eine Menge
print(I_unique)

#Dictionary
#=Erweiterung von Mengen = Bestitzen eine Menge von Schlüseln
d ={"the":4, "in":2, "yard":1, "barn":1}#Tipp: Ein Counter funktioniert über ein Dictionary
print(d["the"])