import random
import math


try:
    with open("statistik.txt","r")as f:
        content=f.read()
    statistik=eval(content)
except:
    statistik = [0,0]
anzahlVersuche = statistik[0]
richtig=statistik[1]
while True:
    winkel=[] # Liste für die verschiedenen Winkel
    bogenmass = random.random() * 2 * math.pi  # zufällige Berechnung Bogenmass
    grad = round(math.degrees(bogenmass)) # Umrechnung Grad
    # print(bogenmass,grad) # Testausgabe
    index = random.randint(0,3) # Bestimmung Index mit dem richtigen Wert - zufälliger Wert aus 0 bis 3
    # Liste mit 4 zufälligen Werten in Grad
    i = 0
    while i < 4:
        wert = random.randint(0,359) # Wert zwischen 0 und 359
        if wert != grad and wert not in winkel: # Sicherstellen, dass Wert nicht mit richtigem Grad übereinstimmt und nicht mehrfach vorkommt
            winkel.append(wert)
            i +=1
    
    winkel[index] = grad # Ersetzen des zufälligen Werts durch tatsächlichen Grad an der Position index
    #print(winkel)

    print("Welchem Winkelgrad entspricht näherungsweise das folgende Bogenmass", round(bogenmass,2))
    eingabe = int(input("0) " + str(winkel[0])
                    + ", 1) " + str(winkel[1])
                    + ", 2) "+ str(winkel[2])
                    + ", 3) " +str(winkel[3])+"\n"))
    anzahlVersuche+=1
    if eingabe == index:
        print("Korrekte Antwort")
        richtig+=1
    else:
        print("Antwort falsch")
        print("Korrekt ist Antwort", index)
    if input("Weiterer Test (Y/N)?\n").upper()=="N":
        break
print("Die Anzahl der Versuche:",anzahlVersuche,"\nAnzahl der richtigen Versuche:",richtig,"\n","*"*50)
proz=math.floor(richtig/anzahlVersuche*100)
print("Der Prozentanteil der richtigen Antworten:",proz,"%")
if anzahlVersuche<5:
    print("Die Anzahl der Versuche ist zu gering. Eine statistische Aussage ist nicht sinnvoll!")
else:
    if proz < 30:
        print("Das ist wohl nur geraten")
    elif proz < 50:
        print("Ausbaufähig")
    elif proz < 85:
        print("Das kann man erwarten")
    else:
        print("Mathe-Ass")


try:
    with open("statistik.txt","w")as f:
        f.write(str([anzahlVersuche,richtig]))
    
except:
    print("Fehler beim Speichern der Statistik")
