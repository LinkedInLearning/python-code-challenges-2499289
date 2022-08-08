import sys
print("Bitte geben Sie eine Zahl zwischen 0 und 9 ein: ")
wert = input()
if wert == "":
    sys.exit("Es muss ein Zeichen eingegeben werden!")
if len(wert) > 1:
    sys.exit("Es darf nur ein Zeichen eingegeben werden!")
if ord(wert) < 48 or ord(wert) > 57:
    print("Das ist keine Zahl zwischen 0 und 9.")
