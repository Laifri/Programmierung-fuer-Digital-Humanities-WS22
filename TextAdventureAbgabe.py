# Text Adventure
# Larissa Fritz
# Programmierung für die Digital Humanities WS 2022/23

# Kapitel 1: Name und Starten des Spiels
name = input(
    "Abenteuer wird geladen...\n...Langsam öffnest du deine Augen.\nDu erblickst einen kleinen alten Mann mit langem weißen Bart. Er dreht sich zu dir um und fragt:\n>>Wie lautet dein Name Fremder?<<\n")
print(
    ">>Sei gegrüßt " + name + ". Wir haben dich bereits erwartet.<<\nVerduzt schaust du dich um, du befindest dich in einem altmodisch eingerichtetem und staubigem Wohnzimmer, wessen Wänden voll mit Bücherregalen stehen.\n>>Wir?<< fragst du überrascht.")
print(">>Wir haben keine Zeit mehr für Fragen<< antwortet der alte Mann.\n")

# Mögliche Eingaben
spiel_start = ["ja", "nein"]
buecher = ["tiger", "drache", "muffins"]
weg_mine = ["pferd", "esel"]
aktion_mine = ["rennen", "hauen", "reden"]
raetsel = ["fisch", "Fisch"]
weg_drache = ["hoch", "runter"]
drache = ["1", "2", "3", "4", "5"]

antwort = ""
while antwort not in spiel_start:
    antwort = input(">>Bist du bereit für ein Abenteuer?<<\n(ja/nein)\n")
    if antwort == "ja":
        print(">>Sehr gut<< sagt der alte Mann mit sanfter Stimme. >>Komm mit mir.<<\n")
    elif antwort == "nein":
        print(">>Was willst du dann noch hier?<< brüllt der alte Mann und dir wird schwarz vor Augen...")
        quit()
    else:
        print(">>Ich benötige eine klare Antwort!<<\n")

# Kapitel 2: Die Buchauswahl und wichtige Info
antwort = ""
while antwort not in buecher:
    print(
        ">>Hör gut zu " + name + ", deine Aufgabe lautet: Finde und töte den Drachen Onyx bis zum Sonnenuntergang diesen Tages und befreie die Gefangenen in dessen Höhle.<<\nDer alte Mann sieht dich ernst an >>Alle Informationen die du dazu benötigst, findest du in meinen Büchern. Beeil dich!<<\n")
    antwort = input(
        "Du schaust dich im Raum um und erblickst drei Bücher:\n 1. Das Leben eines Tigers.\n 2. Wie man einen Drachen besiegt.\n 3. Lecker Muffins.\n Für welches Buch entscheidest du dich?\n(tiger/drache/muffins)\n")
    if antwort == "drache":
        print(
            "Du greifst nach einem dicken verstaubten Buch über Drachen und blätterst es durch. Einen Drachen tötet man mit einem Schwert aus Diamant und einem präzisen Stich zwischen die Augen.\nDu schlägst das Buch zu und machst dich auf den Weg.")
    elif antwort == "tiger":
        print("Der alte Mann sieht dich streng an: >>Es geht um einen Drachen und nicht um einen Tiger!<<\n")
        print(
            "Du greifst nach einem dicken verstaubten Buch über Drachen und blätterst es durch. Einen Drachen tötet man mit einem Schwert aus Diamant und einem präxisen Stich zwischen die Augen.\nDu schlägst das Buch zu und machst dich auf den Weg.")
    elif antwort == "muffins":
        print(
            "Völlig außer sich kommt der alte Mann auf dich zu und brüllt:\n>>MUFFINS?<<\nDir wird schwarz vor Augen...")
        quit()
    else:
        print("Solch ein Buch existiert nicht!")

# Kapitel 3: Weg zur Mine
antwort = ""
while antwort not in weg_mine:
    print(
        "Du verlässt das Haus des alten Mannes und möchtest so schnell wie möglich zu einer Diamantmine um ein Schwert zu besorgen.")
    antwort = input(
        "Vor dem Haus siehst du ein Pferd und einen Esel. Für welches Tier entscheidest du dich?\n(pferd/esel)\n")
    if antwort == "pferd":
        print("Du sattelst auf und reitest los in Richtung Mine, welche du innerhalb weniger Stunden erreichst.")
    elif antwort == "esel":
        print(
            "Du setzt dich auf den zerbrechlichen Esel und reitest los. Der Esel ist jedoch so langsam, dass du es nicht mehr rechtzeitig zur Mine schaffst.\nDie Aufgabe ist gescheitert.")
        quit()
    else:
        print("Dieses Tier ist nicht in Sicht.")

# Kapitel 4: In der Mine
antwort = ""
while antwort not in aktion_mine:
    antwort = input(
        "Vorsichtig machst du dich auf den Weg in die tiefe dunkle Mine hinein.\nPlötzlich springt dir ein kleiner gemeiner Kobold vor die Füße und faucht dich an:\n>>Du musst " + name + " sein. Was möchtest du, unwürdige Kreatur, in meiner Mine?<<\nDu kannst nun fliehen und aus der Mine rennen, dem Kobold auf den Kopf hauen oder den Kobold um Hilfe bitte.\nWas tust du?\n(rennen/hauen/reden)\n")
    if antwort == "reden":
        print(
            "Du redest mit dem gemeinem Kobold und erklärst ihm deine Aufgabe.\nDer Kobold schaut dich gespannt an und sagt:\n>>Wirklich interessant! Ich werde dich bei deinem Abenteuer begleiten und dir mein Schwert aus Diamant ausleihen.<<\nDu springst in die Luft und freust dich.\n>>Dafür...<< murmelt der Kobold >>...musst du jedoch folgendes Rätsel lösen:<<\n")
    elif antwort == "hauen":
        print(
            "Mit voller Wucht haust du dem kleinen Kobold auf den Kopf, sodass dieser umkippt.\nPlötzlich kommen zehn weitere gemeine Kobolde aus ihren Verstecken gesprungen und pieksen dir die Augen aus.\nDie Aufgabe ist gescheitert.")
        quit()
    elif antwort == "rennen":
        print(
            "Du rennst los und stürzt dich aus der Mine.\nDer alte Mann mit langem weißem Bart wartet bereits dort auf dich: >>Du bist an dieser Aufgabe gescheitert<<.\nGeschockt bleibst du steht und dir wird schwarz vor Augen...")
        quit()
    else:
        print("Der Kobold schaut dich böse an und wartet auf eine richtige Antwort.")

antwort = ""
while antwort not in raetsel:
    antwort = input(
        ">>Atemlos lebt es, kalt wie der Tod schwebt es. Kennt keinen Durst – Dennoch trinkt es. Trägt ein Kettenhemd, doch nie klingt es<<.\n")
    if antwort == "fisch":
        print(">>Sehr gut<< sagt der Kobold. Du bist mein Schwert würdig.")
    elif antwort == "Fisch":
        print(">>Sehr gut<< sagt der Kobold. Du bist mein Schwert würdig.")
    else:
        print("Versuche es erneut.")

# Kapitel 5: Die Höhle
antwort = ""
while antwort not in weg_drache:
    print("Du und der Kobold verlasst gemeinsam die Mine. Ihr macht euch auf den Weg zur Höhle des Onyx.\n")
    print(
        "Als ihr die Höhle betretet könnt ihr bereits die Schreie der Opfer des Drachen hören.\nZitternd steigst du von dem Pferd ab und machst dich auf die Suche nach Onyx.\n")
    antwort = input(
        "Vom oberen Teil der Höhle hörst du die Schreie. Im unteren Teil der Höhle scheint es leise zu sein. Wo befindet sich Onyx?\nDu erblickst eine Treppe. Möchtest du die Treppe hoch oder runter gehen?\n(hoch/runter)\n")
    if antwort == "runter":
        print("Du gehst die Treppen hinunter und erblickst den schlafenden Onyx. Ein perfekter Überraschungsangriff!\n")
    elif antwort == "hoch":
        print(
            "Du gehst die Treppen nach oben.\nOnyx befindet sich jedoch im Keller. In dem Moment, indem du die letzte Treppe nach oben betrittst kommt Onyx hochgeflogen und beißt dir den Kopf ab.\n")
        quit()
    else:
        print("Beeil dich, die Sonne geht bald unter!")

# Kapitel 6: Kampf mit dem Drachen
antwort = ""
while antwort not in drache:
    print("Du nutzt deine Chance und rennst in Richtung Onyx. Jetzt muss es schnell gehen!\n")
    antwort = input("Wie kannst du einen Drachen töten?\n "
                    "1. Du führst einen uralten Tanz namens >Tanzender Drache< auf, welchen du aus Avatar-Der Herr der Elemente kennst.\n "
                    "2. Du nimmst das Diamantschwert und führst eine präzisen Stich zwischen Onyxs Augen aus.\n "
                    "3. Du fragst den Drachen zitternd nach einen Rat.\n "
                    "4. Du nimmst das Diamantschwert und stichst es in einem Überraschungsangriff Onyx in die Brust.\n "
                    "5. Du verlässt die Höhle schnell wieder.\n(1/2/3/4/5)\n")
    if antwort == "2":
        print(
            "Du rennst auf Onyx zu und mit einem epischen Stich zwischen seinen Augen schaffst du es, Onyx zu töten.\nDer Kobold ruft >>Super, Super!!" + name + ", du hast es geschafft!<<\nSo schnell du kannst rennst du die Treppen hoch um den Verletzten zu helfen.\nSie erzählen dir die schrecklichsten Geschichten ihrer unglaublichen Reise und Gefangenschaft unter Onyx.\nDu kannst es kaum fassen und reibst dir die Augen.\nPlötzlich öffnest du deine Augen.\nDu findest dich in deinem kuschligen Bett zu Hause wieder.\n>>Mhh?<< du wunderst dich...es fühlte sich so echt an...")
    elif antwort == "1":
        print(
            "Onyx erwacht, erblickt und beobachtet dich. In Schweiß gebadet tanzt du weiter und weiter.\nDer Kobold ruft >>WAS TUST DU DA?<<\nDoch bevor du realisierst, was gerade geschieht, packt dich der Drache und verspeißt dich als Frühstück.")
        quit()
    elif antwort == "3":
        print(
            "Onyx ist von deinem Angriff nicht beeindruckt und erhebt sich.>>Was versuchst du da kleine Kreatur?<< lacht er dich aus. >>Wie kannst du es wagen in meine Höhle einzudringen?<<\nOhne zu zögern zermalmt dich Onyx unter seinen Klauen.\nDu stirbst.")
        quit()
    elif antwort == "4":
        print(
            "Onyx erwacht und blickt dich an. Einen Rat hat er nicht für dich, jedoch siehst du für ihn sehr lecker aus.\nDu stirbst.")
        quit()
    elif antwort == "5":
        print(
            "Du flüchtest die Treppen wieder nach oben, doch Onyx hört dich. Er erhebt sich und brüllt dich an >>WER BIST DU?<<\nOhne zu zögern schnappt er dich in einem Happen.\nDu stirbst.")
        quit()
    else:
        print("Beeil dich bevor Onyx aufwacht!")
