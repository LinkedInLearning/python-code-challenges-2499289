def getBremsweg(geschwindigkeit, faktor,  verzoeger):
    bremsmeter = (geschwindigkeit * geschwindigkeit / 100) * faktor
    verzoegermeter = 0
    if verzoeger:
        verzoegermeter = geschwindigkeit/10*3
    return round((bremsmeter + verzoegermeter)*100)/100.0


while True:
    geschwindigkeit = int(input("Eingabe Geschwindigkeit\n"))
    belag = int(input(
        "Auswahl Fahrbahnzustand/Situation:\n0: Trocken\n1: Nass\n2: Eis\n3: Gefahrenbremsung\n"))
    if belag == 0:
        faktor = 1
    elif belag == 1:
        faktor = 1.5
    elif belag == 2:
        faktor = 6.5
    elif belag == 3:
        faktor = 0.5
    verzoeger = input("Verzögerung einkalkulieren (Y/N)?\n")
    if verzoeger.upper() == "Y":
        verzoeger = True
    else:
        verzoeger = False

    print("Der Bremsweg ist", getBremsweg(
        geschwindigkeit, faktor,  verzoeger), "Meter")

    if input("Weitere Bremswegberechnungen (Y/N)?\n").upper() == "N":
        print("Danke, dass Sie unseren Service genutzt haben!")
        break
