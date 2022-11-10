#If-Bedingungen -> Wenn- Dann- Sonst
#Wenn ich die Bahn sehen, dann steige ich ein (sonst mache ich nichts)
#if kann immer nur true oder false sein = Ja oder Nein
if bahn_gesehen: #wenn
    einsteigen() #dann

#Wenn ich die Bahn sehe, dann steige ich ein, sonst schaue ich auf die Uhr
if bahn_gesehen: #wenn
    einsteigen () #dann
else:
    uhr() #sonst

#Wenn ich die Bahn sehe, dann steige ich ein. Sonst steige ich, wenn ich den Bus sehe in den Bus ein
if bahn_gesehen(): #wenn
    einsteigen() #dann
elif bus_gesehen: #sonst wenn
    bus_einsteigen() #sonst

#Mathematischen Operatoren = In erster Linie für Zahlen
# == gleich -> Damit kann man auch strings vergleichen. Zahlen vergleichen ist einfach aber man kann auch Strings(Ketten) vergleichen, aber wann sind sie gleich?
# <, > kleiner, größer
# <=, >= kleiner-gleich, größer-gleich
# != nicht gleich

#Logische Operatoren
# or linke Seite oder rechte Seite stimmt (oder beide)
# and linkte und rechte Seite stimmt
# not rechte Seite stimmt nicht

#Listen-Operator
# in ist das linke element in der rechten Kollketion
