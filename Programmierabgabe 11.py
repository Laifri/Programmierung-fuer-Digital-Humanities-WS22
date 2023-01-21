import sys
import random


# Programmieren sie einen kleinen virtuellen Assistenten:
# Ihr Programm sollte den Benutzer fragen, welche Aktion ausgeführt werden soll und dementsprechend handeln
# Ihr Programm muss terminieren, wenn der Benutzer es wünscht
#Achten Sie darauf, dass Ihr Programm mit falschen Eingaben umgehen kann.
# Subtrahieren: Ihr Programm soll 2 Zahlen voneinander abziehen und das Ergebnis ausgeben
# Dividieren: Ihr Programm soll 2 Zahlen teilen und das Ergebnis ausgeben
#Sentiment Wort: Ihr Programm nimmt ein Wort entgegen und sagt, ob es positiv oder negativ oder neutral ist. Benutzen Sie dazu die Listen mit positiven/negativen Wörtern aus den letzten Abgaben. Sie können annehmen, dass Wörter, die nicht in einer der Listen vorkommen neutral sind.
# Witz erzählen: Ihr Assisten gibt einen Witz auf der Kommandozeile aus. Alternativ kann auch ein Witz zufällig aus einer Liste ausgewählt werden.

def menu():
    print("Menü:")
    print("1 - Zwei Zahlen addieren")
    print("2 - Zwei Zahlen subtrahieren")
    print("3 - Zwei Zahlen dividieren")
    print("4 - Sentimentanalyse")
    print("5 - Witz erzählen")


def addieren(x, y):
    zahl1 = int(x)
    zahl2 = int(y)
    return zahl1 + zahl2


def subtrahieren(x, y):
    zahl1 = int(x)
    zahl2 = int(y)
    return zahl1 - zahl2


def dividieren(x, y):
    zahl1 = int(x)
    zahl2 = int(y)
    return zahl1 / zahl2


positive = open("positive_cues.txt", "r", encoding="utf8").read()
negative = open("negative_cues.txt", "r", encoding="utf8").read()


def sentimentanalyse(wort):
    if wort in positive:
        print("Das Wort ist positiv!")
    elif wort in negative:
        print("Das Wort ist negativ!")
    else:
        print("Das Wort ist neutral!")


witz = ["Was ist weiß und rollt den Berg hoch? Eine Lawine mit Heimweh.",
        "Was ist gesund und schmollt? Ganz klar: Ein Schmollkornbrot.",
        "Wie heißt ein Ritter ohne Helm? Willhelm.",
        "Was ist das? Es rennt durch den Wald und brennt. Ein Kaminchen!",
        "Was ist grün und sitzt hinter Gittern? Ein Essigschurke.",
        "Wie heißt eine Bratkartoffel mit Haaren? Bartkartoffel."]

while True:
    menu()
    menu_selection = input("Wählen Sie eine der Funktion durch Eingabe der Zahl:")
    if menu_selection == "1":
        print("Zahlen addieren:")
        eingabe = input("Geben sie zwei Zahlen zum addieren ein")
        if eingabe == "Ende":
            sys.exit()
        zahl1 = eingabe.split(" ")[0]
        zahl2 = eingabe.split(" ")[1]
        try:
            print("Ergebnis:", addieren(zahl1, zahl2))
        except:
            print("Versuchen Sie eine andere Zahl")
    elif menu_selection == "2":
        print("Zahlen subtrahieren:")
        eingabe = input("Geben sie zwei Zahlen zum subtrahieren ein")
        if eingabe == "Ende":
            sys.exit()
        zahl1 = eingabe.split(" ")[0]
        zahl2 = eingabe.split(" ")[1]
        try:
            print("Ergebnis:", subtrahieren(zahl1, zahl2))
        except:
            print("Versuchen Sie eine andere Zahl")
    elif menu_selection == "3":
        print("Zahlen dividieren:")
        eingabe = input("Geben sie zwei Zahlen zum dividieren ein")
        if eingabe == "Ende":
            sys.exit()
        zahl1 = eingabe.split(" ")[0]
        zahl2 = eingabe.split(" ")[1]
        try:
            print("Ergebnis:", dividieren(zahl1, zahl2))
        except:
            print("Versuchen Sie eine andere Zahl")
    elif menu_selection == "4":
        print("Sentimentanalyse:")
        eingabe = input("Geben sie ein Wort ein")
        if eingabe == "Ende":
            sys.exit()
        wort = (sentimentanalyse(eingabe))
    elif menu_selection == "5":
        print(random.choice(witz))
    elif menu_selection == "Ende":
        sys.exit()
