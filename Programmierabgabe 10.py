import re
#Schreiben Sie die folgenden regulären Ausdrücke und testen Sie die Ausdrücke an der bereitgestellten Testfile:
#Ihre Regulären Ausdrücke sollten alle Vorkommen finden. Sie können mehrere reguläre Ausdrücke benutzen um die Teilaufgaben zu lösen.
text = open("RegEx_test.txt", "r", encoding="utf8").read()
#-Finden Sie alle Datumsangaben
datum = re.findall(r"(\d\d[ |\/|\.](?:\d\d|Jan|Feb|Mär|Apr|Mai|Jun|Jul|Aug|Sept|Okt|Nov|Dez)[ |\/|\.]\d{2,4})", text)
print("Datum:", datum)
#-Finden Sie alle Telefonnummern
telefonnr1 = re.findall(r"\d{5}-\d{6}", text)
telefonnr2 = re.findall(r"(\d{5}[\s|-](?:\d{7,8}))", text)
telefonnr3 = re.findall(r"\d{4}-\d{3}\-\d", text)
print("Telefonnummer:", telefonnr1, telefonnr2, telefonnr3)
#-Finden Sie alle E-Mail adressen
email = re.findall(r"\w+\.?\w+@\w+\.\w{2,3}",text)
print("Email:", email)
#-Finden Sie Abkürzungen, die aus mehreren Großbuchstaben bestehen (z.B. NASA)
abkürzung = re.findall(r"[A-Z]{2,}", text)
print("Abkürzung:", abkürzung)
#-Finden Sie mehrteilige Eigennamen, wie z.B. New York City.
eigennamen = re.findall(r"[^\n][A-Z][a-z]+\s[A-Z][a-z]+", text)
print("Eigennamen:", eigennamen)
#Speichern Sie die gefundenen Strings für jede RegEx die Sie benutzt haben in Dateien
#und geben Sie die Dateien zusammen mit dem Code ab.
dateipfad_datum = "datum.txt"
datei_datum = open(dateipfad_datum, "w", encoding="utf8")
for date in datum:
    datei_datum.write(date)
    datei_datum.write("\n")

dateipfad_telefonnummer = "telefonnummer.txt"
datei_telefon = open(dateipfad_telefonnummer, "w", encoding="utf8")
for number in telefonnr1:
    datei_telefon.write(number)
    datei_telefon.write("\n")
for number in telefonnr2:
    datei_telefon.write(number)
    datei_telefon.write("\n")
for number in telefonnr3:
    datei_telefon.write(number)
    datei_telefon.write("\n")

dateipfad_email = "email.txt"
datei_email = open(dateipfad_email, "w", encoding="utf8")
for adress in email:
    datei_email.write(adress)
    datei_email.write("\n")

dateipfad_abkürzung = "abkürzung.txt"
datei_abkürzung = open(dateipfad_abkürzung, "w", encoding="utf8")
for wort in abkürzung:
    datei_abkürzung.write(wort)
    datei_abkürzung.write("\n")

dateipfad_eigennamen = "eigennamen.txt"
datei_eigennamen = open(dateipfad_eigennamen, "w", encoding="utf8")
for name in eigennamen:
    datei_eigennamen.write(name)
    datei_eigennamen.write("\n")