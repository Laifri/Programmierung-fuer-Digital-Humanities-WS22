#Dateien/Files
#Textdatei = Ausschließlich Text  // Binärdateien = Enthalten alles mögliche (Bilder, PDF, Word...)
#Methode open() = Es wird auf Dateien auf der Festplatte zugegriffen
#Dateipfad hat drei Methoden: r, w, a
#open(pfad, "r") -> read = Modus, die Datei wird eingelesen und nicht beschrieben
#open(pfad, "w") -> write = Modus, die Datei wird nicht eingelesen, sondern es wird eine neue, leere Datei erzeugt
#open(pfad, "a") -> append = Modus, die Datei wrd eingelesen, kann aber auch beschrieben werden. Neue Inhalte werden hinten an die Datei angehängt. Datei muss schon existieren.
#Wenn man auf Binärdateien zugreifen mit open(), einfach "b" hinter den Modus = "rb" oder "wb"

#Textdatei lesen
dateipfad = "testdatei.txt"
datei = open(dateipfad, "r") #generisches File-Objekt, noch nicht sehr nützlich
#oder: datei = open(dateipfad, "r").read
dateitext = datei.read() #verwandelt die ganze Datei in einen String
zeilen = dateitext.split("\n") #splitted den grpßen String an jedem Zeilenende. Man erhält eine Liste von Strings
# \n = Zeilenumbruch
for satz in zeilen:
    ...

datei.close() #schließt die Datei so dass der Arbeitsspeicher frei wird. Wichtig bei großen Datein.

#Textdatei schreiben
saetze = [s1, s2, s3] #Liste mit irgendwelchen Stings

dateipfad = "testdatei_neu.txt"
datei = open(dateipfad, "w") #Datei wird zum beschreiben leer erstellt. Heißt, wenn die Datei schon existier wird sie überschrieben!
for satz in saetze:
    datei.write(satz) #write() akzeptiert nur strings
    datei.write("\n") #sonst wird alles hintereinander geschrieben
datei.close()







