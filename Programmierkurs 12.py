#Klasse = Vorlage aus Code, Sammlung von Code. Wird definiert durch Eigenschaften und Funktionen.
#Klasse wird benutzt, indem man sie im Code aufruft -> Dann wird ein Objekt der Klasse erzeugt.
#Beispiel = Wir wollen ein Spiel programmieren das Pizza backt, daher muss der Nutzer Pizza zusammenstellen können
#und beliebig belegt werden und gebacken werden können.
#Pizza ist die Klasse; Objekte sind eine Pizza

#def_int_(self): Um neues Objekt von Pizza zu erzeugen, auch "Konstruktor"

class Pizza:
    def __init__(self):
        self.belag =[]
        self.stücke = 1
        self.gebacken = False
        self.verbrant = False

    def belegen(self,zutat):
        self.belag.append(zutat)

    def backen(self):
        if self.gebacken == False:
            self.gebacken = True

    def schneiden(self):
        self.stücke = self.stücke*2

pizza1 = Pizza()
#Klassen werden groß geschrieben, Funktionen klein
pizza1.belegen("salami")
pizza1.belegen("käse")

pizza1.schneiden()
pizza1.schneiden()

print(pizza1.belag)
print(pizza1.stücke)

if __name__ == "__main__":
# Alles was darunter steht wird ausgeführt, nichts darüber