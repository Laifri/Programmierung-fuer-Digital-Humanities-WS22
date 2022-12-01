#Tokenisierung mit Slices
#List Index
satz = ["Jeder","mag","den","kleinen","Michel"]
print(satz[1]) # = mag = Die eckigen Klammern sind wie ein "an der Stelle" -> satz[0] ist "Jeder"
print(satz[-1]) # -1 gibt das letzte Element zurück = Michel
#List Slices
print(satz[0:2]) #-> Jeder mag = Also Stelle 0 und 1 aber NICHT 2
print(satz[1:4])#=mag den kleinen
#Schreibweise = liste[start_index:end_index]
print(satz[2:]) #kein end_index = ab start_index alle Elemente = den kleinen Michel
print(satz[:2]) #kein start_index = start_index =0 = Jeder mag
print(satz[:]) #die gleiche Liste
print(satz[0:-1]) #Alles bis auf das letzte Element = Jeder mag den kleinen
print(satz[1:-2]) #Element 1 bis zum zweiletzten = mag den
#String Slices
wort = "Tischler"
print(wort[0]) #=T
print(wort[-1]) #=r
print(wort[0:3]) #=Tis
print(wort[3:7]) #chle
#[0:-1] = Punkt am Ende will man nicht mehr