import sys


def addieren(a, b):
    zahl1 = int(a)
    zahl2 = int(b)
    return zahl1 + zahl2


while True:
    eingabe = input("Bitte zwei Zahlen eingeben")
    if eingabe == "Ende":
        sys.exit()
    zahl1 = eingabe.split(" ")[0]
    zahl2 = eingabe.split(" ")[1]
    try:
        addieren(zahl1, zahl2)
        print(addieren(zahl1,zahl2))
    except:
        print("bitte geben sie nur Zahlen ein")
