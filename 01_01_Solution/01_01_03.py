import sys
print("Bitte geben Sie eine Zahl zwischen 0 und 9 ein: ")
if wert == "":
    sys.exit("Es muss ein Zeichen eingegeben werden!")
wert = input()[0]
if ord(wert) < 48 or ord(wert) > 57:
    print("Das ist keine Zahl zwischen 0 und 9.")
