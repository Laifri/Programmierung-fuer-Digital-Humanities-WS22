# Erweitern Sie das Pizza-Beispiel um die folgenden Funktionen:
# Jede Pizza sollte einen Preis haben. Der Preis setzt sich zusammen aus den Belägen.
# Legen Sie die Preise für bestimme Beläge (mindestens: Salami, Käse, Tomatensoße und 2 weitere Ihrer Wahl) fest und berechnen Sie den Preis der Pizza aus der Summe aller Beläge.
# Unbekannte Beläge können Sie vom Preis her alle gleich behandeln. Überlegen Sie sich die Preise der einzelnen Zutaten einfach selbst.
# Die Berechnung des Preises soll innerhalb der Klasse passieren.
# Erstellen sie die "main" methode, und erstellen sie 3 verschiedene Objekte der Klasse Pizza mit verchiedenen Belägen, um ihre Preisberechnung zu testen.
# Geben Sie alle Pizzen mit Preis auf der Konsole aus.

class Pizza:

    def __init__(self):
        self.belag = []
        self.stuecke = 1
        self.gebacken = False
        self.verbrannt = False

    def belegen(self, zutat):
        self.belag.append(zutat)

    def backen(self):
        if self.gebacken == False:
            self.gebacken = True
        else:
            self.verbrannt = True

    def schneiden(self):
        self.stuecke = self.stuecke * 2

    def status(self):
        if self.verbrannt == True:
            print("Die Pizza ist verbrannt!")
        else:
            print("Belag:", self.belag)
            print("Stücke:", self.stuecke)
            print("gebacken:", self.gebacken)


if __name__ == "__main__":
    # Alles was darunter steht wird ausgeführt, nichts darüber
    pizza1 = Pizza()
    pizza1.belegen("käse")
    print(pizza1.status())
