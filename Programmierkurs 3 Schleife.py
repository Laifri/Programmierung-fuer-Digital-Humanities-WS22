#Schleifen; Die For-Schleife
#Eine for-Schleife wiederholt Code für jedes Element aus einer Liste (oder anderer Datenstruktur)
#Erste Kontrollstruktur: Wir werden die for-Schleife verwenden um die Bearbeitung der Satzliste zu automatisieren

#liste=[0,1,2,3,4] #Ziel= Summe aller Elemente aus der Liste ausgeben
#summe = 0
#for item in liste: #Die Schleife läuft 5 mal =Das passiert: 0+0, 0+1, 1+2, 3+3
#    summe = summe + item
#print(summe) #=10

#liste=["ein","hund","spielt","gern"]
#gesamt=""
#for item in liste:
#            gesamt = gesamt + item
#print(gesamt) #=einhundspieltgern

#Strings sind auch Listen = Strings werden als Listen repräsentatiert, Buchstaben = characters

satz1 = "Der Hund bellt heute nicht im Garten sondern im Hof." #string: beliebige anzahl von zeichen
satz2 = "Die Katze schleicht morgens zum Nachbarn."
satz3 = "Vielleicht genehmige ich mir heute Abend Lebkuchen"

satz1_tokens = (satz1.split(" ")) #Mit Leerzeichen=Bei jedem Leerzeichen wird gesplittet
satz2_tokens = (satz2.split(" "))
satz3_tokens = (satz3.split(" "))
tokensliste = [satz1_tokens,satz2_tokens,satz3_tokens]
#Anzahl der Wörter bzw. Tokens ist die Länge der Liste satz1_tokens
woerter1 = len(satz1_tokens)
woerter2 = len(satz2_tokens)
woerter3 = len(satz3_tokens)

woerter_gesamt = woerter1 + woerter2 + woerter3
woerter_durchschnitt = woerter_gesamt / 3

#Alle Sachen in Listen speichern:
satzliste = [satz1,satz2,satz3,"Die Gärtnerei hat geschlossen"]
#Wie bekomm ich das automatisch hin?
woerterliste = [woerter1,woerter2,woerter3,4]
woerterliste.append(x)

#Jeder Satz aus Satzliste soll ausgegeben werden
for satz in satzliste:
    print(satz)

#Jede Satzlänge ausgeben
for wordcount in woerterliste:
    print(wordcount)

#Beides gleichzeitig
#for satz in satzliste
    #dann irgendwas mit token und len

#Summe aller Satzlängen
#woerter_gesamt = 0
#for #Hausaufgabe



#len() funktion: Gibt länge einer Liste aus
print("Anzahl Sätze:",len(satzliste))
print("Wörter Durschnitt:",woerter_durchschnitt)

