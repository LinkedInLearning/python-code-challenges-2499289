warenkorb = {}                  #Erstellt ein leeres Dictionary
print("Geben Sie Ihre Bestellung ein.")
while True:           
    produkt = input("Geben Sie das Produkt ein.\n").lower()
    anzahl = input("Geben sie die Menge ein.\n")

    warenkorb[produkt] = anzahl
    
    exitOrNot = input("w(eiter einkaufen), b(estellen), a(bbruch).\n").upper()

    if exitOrNot == "A":
        print("Bestellung wird abgebrochen")
        break
    elif exitOrNot == "B":
        print("Bestellung ", warenkorb)
        break
    else:
        print("Weiter einkaufen.\nNeues Produkt wählen.")
