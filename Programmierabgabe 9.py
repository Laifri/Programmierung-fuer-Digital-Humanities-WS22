import nltk
import string
from collections import Counter
from nltk import word_tokenize
from nltk import wordpunct_tokenize

# Lesen Sie, wie bei den vergangenen Abgaben die Sätze aus corona_twitter ein.
twitter_daten = open("corona_twitter.txt", "r", encoding="utf8").read().split("\n")
# Lesen Sie auch die Wörter aus positive_cues.txt und negative_cues.txt als separate Listen ein.
positive_words = open("positive_cues.txt", "r", encoding="utf8").read().split("\n")
negative_words = open("negative_cues.txt", "r", encoding="utf8").read().split("\n")
# Wir wollen Sätze filtern, die positive oder negative Wörter enthalten:
# Schreiben Sie alle Sätze, die mindestens ein negatives Wort enthalten in eine neue Datei mit dem Namen "negative.txt".
dateipfad_negative = "negative.txt"
datei_negative = open(dateipfad_negative, "w", encoding="utf8")

all_tokens = []
for satz in twitter_daten:
    tokenized = word_tokenize(satz)
    all_tokens.extend(tokenized)

negative_sentence = []
for word in all_tokens:
    if word in negative_words:
        negative_sentence.append(satz)

for sentence in negative_sentence:
    datei_negative.write(sentence)
    datei_negative.write("\n")


print(satz)



# Schreiben Sie alle Sätze, die mindestens ein positives Wort enthalten in eine neue Datei mit dem Namen "positve.txt".
#dateipfad_positive = "positve.txt"
#datei_positive = open(dateipfad_positive, "w", encoding="utf8")

#for satz in twitter_daten:
  #  for word in twitter_daten:
 #       if word in positive_words:
   #         datei_positive.append(satz)
  #      datei_positive.write(satz)



# Alle Sätze, die sowohl negative als auch positive Wörter enthalten sollen in eine Datei mit dem Namen "ambiguous.txt" geschrieben werden. (Die Sätze dürfen auch in positive.txt oder negative.txt stehen)


# In den neuen Dateien sollten alle Sätze untereinander stehen und gut lesbar sein. Jeder Satz sollte maximal einmal in jeder Datei stehen.
