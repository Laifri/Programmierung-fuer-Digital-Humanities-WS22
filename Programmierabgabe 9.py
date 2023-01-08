import nltk
import string
from collections import Counter
from nltk import word_tokenize
from nltk import wordpunct_tokenize

# Lesen Sie, wie bei den vergangenen Abgaben die Sätze aus corona_twitter ein.
twitter_daten = open("corona_twitter.txt", "r", encoding="utf8").read().split("\n")[:1000]
# Lesen Sie auch die Wörter aus positive_cues.txt und negative_cues.txt als separate Listen ein.
positive_words = open("positive_cues.txt", "r", encoding="utf8").read().split("\n")
negative_words = open("negative_cues.txt", "r", encoding="utf8").read().split("\n")
# Wir wollen Sätze filtern, die positive oder negative Wörter enthalten:
# Schreiben Sie alle Sätze, die mindestens ein negatives Wort enthalten in eine neue Datei mit dem Namen "negative.txt".
# Schreiben Sie alle Sätze, die mindestens ein positives Wort enthalten in eine neue Datei mit dem Namen "positive.txt".
# Alle Sätze, die sowohl negative als auch positive Wörter enthalten sollen in eine Datei mit dem Namen "ambiguous.txt" geschrieben werden.
# (Die Sätze dürfen auch in positive.txt oder negative.txt stehen)
# In den neuen Dateien sollten alle Sätze untereinander stehen und gut lesbar sein. Jeder Satz sollte maximal einmal in jeder Datei stehen.

dateipfad_negative = "negative.txt"
datei_negative = open(dateipfad_negative, "w", encoding="utf8")
dateipfad_positive = "positive.txt"
datei_positive = open(dateipfad_positive, "w", encoding="utf8")
dateipfad_ambiguous = "ambiguous.txt"
datei_ambiguous = open(dateipfad_ambiguous, "w", encoding="utf8")

all_tokens = []
negative_sentence = []
positive_sentence = []
ambiguous_sentence = []
for satz in twitter_daten:
    tokenized = word_tokenize(satz)
    all_tokens.extend(tokenized)
    negative = False
    positive = False
    for word in tokenized:
        if word in negative_words:
            negative = True
        if word in positive_words:
            positive = True
    if negative and positive:
        ambiguous_sentence.append(satz)
    elif negative:
        negative_sentence.append(satz)
    elif positive:
        positive_sentence.append(satz)

for sentence in negative_sentence:
    datei_negative.write(sentence)
    datei_negative.write("\n")

for sentence in positive_sentence:
    datei_positive.write(sentence)
    datei_positive.write("\n")

for sentence in ambiguous_sentence:
    datei_ambiguous.write(sentence)
    datei_ambiguous.write("\n")