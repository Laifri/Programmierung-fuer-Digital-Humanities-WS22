import nltk
import string
from collections import Counter
from nltk import word_tokenize
from nltk import wordpunct_tokenize

# Lesen Sie alle Sätze aus "corona-twitter.txt" ein und tokenisieren Sie die Sätze mithilfe der Library nltk.
twitter_daten = open("corona_twitter.txt", "r", encoding="utf8").read().split("\n")[:100]

# Speichern sie alle Tokens in einer Liste und verwenden Sie einen Counter, um die Token zu zählen.
all_tokens = []
for line in twitter_daten:
    tokenized = word_tokenize(line)
    all_tokens.extend(
        tokenized)  # method "extend" adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
word_count = Counter(all_tokens)
print("Token und ihre jeweilige Anzahl:", word_count)

# Geben Sie die häufigsten 100 Wörter aus (mit print()) - sie werden sehen, dass viele Sonderzeichen dabei sind.
most_common_100 = word_count.most_common(100)
print("Die 100 häufigsten Wörter und ihre Anzahl:", most_common_100)

# Modifizieren Sie ihr Programm, so dass Tokens, die nur aus Sonderzeichen bestehen nicht in die Liste aller Wörter aufgenommen werden. Dafür können Sie auf string.punctuation zurückgreifen.
# wir wollen keine Satzzeichen in den tokens:
# neue Liste von tokens erhält alle tokens aus der alten liste
# nltk.download('punkt') = wenn punktion nicht funktioniert
# Modifizieren Sie dann ihr Programm, dass die Wörter "the", "and", "or" und "to" nicht die Liste aller Wörter aufgenommen werden.
def clean_punctuation(tokens):
    punctuations = "…●“’"
    words = ["the", "end", "or", "to"]
    new_tokens = []
    for t in tokens:
        if t[0] in string.punctuation:
            pass
        elif t in punctuations:
            pass
        elif t in words:
            pass
        else:
            new_tokens.append(t)
    return new_tokens

ohne_punktion = []
for line in twitter_daten:
    tokenized = wordpunct_tokenize(line)
    ohne_punktion.extend(clean_punctuation(tokenized))
print("Liste aller Wörter ohne Sonderzeichen und ohne the, and, or und to:", ohne_punktion)

# Schreiben Sie nun die häufigsten 100 Wörter in eine neue Datei mit dem Namen "100_most_common.txt"
saetze = Counter(ohne_punktion).most_common(100)
dateipfad = "100_most_common.txt"
datei = open(dateipfad, "w", encoding="utf8")
for satz in saetze:
    datei.write(satz[0])
    datei.write("\n")
datei.close()