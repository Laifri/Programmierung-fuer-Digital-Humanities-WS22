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
        self.preis = 0

    def belegen(self, zutat):
        self.belag.append(zutat)

    def bepreisen(self):
        for belag in self.belag:
            if belag == "Käse":
                self.preis = self.preis + 3
            if belag == "Tomatensoße":
                self.preis = self.preis + 2
            if belag == "Salami":
                self.preis = self.preis + 5
            if belag == "Mais":
                self.preis = self.preis + 2
            if belag == "Gemüse":
                self.preis = self.preis + 2
            if belag == "Knoblauch":
                self.preis = self.preis + 3

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
            print("Vielen Dank für ihre Bestellung. Hier ist ihre Pizza:")
            print("Belag:", self.belag)
            print("Stücke:", self.stuecke)
            print("Gebacken:", self.gebacken)
            print("Preis:", self.preis, "Euro")

if __name__ == "__main__":
    pizza1 = Pizza()
    pizza1.belegen("Käse")
    pizza1.belegen("Tomatensoße")
    pizza1.bepreisen()
    pizza1.backen()
    pizza1.schneiden()
    pizza1.schneiden()
    print(pizza1.status())

    pizza2 = Pizza()
    pizza2.belegen("Salami")
    pizza2.belegen("Käse")
    pizza2.belegen("Tomatensoße")
    pizza2.bepreisen()
    pizza2.backen()
    pizza2.schneiden()
    pizza2.schneiden()
    pizza2.schneiden()
    print(pizza2.status())

    pizza3 = Pizza()
    pizza3.belegen("Salami")
    pizza3.belegen("Käse")
    pizza3.belegen("Tomatensoße")
    pizza3.belegen("Knoblauch")
    pizza3.belegen("Mais")
    pizza3.belegen("Gemüse")
    pizza3.bepreisen()
    pizza3.backen()
    pizza3.schneiden()
    pizza3.schneiden()
    pizza3.schneiden()
    pizza3.schneiden()
    print(pizza3.status())