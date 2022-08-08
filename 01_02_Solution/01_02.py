print("Eingabe Datei")
dat = input()
with open(dat,"r") as eingabedatei:
    text=eingabedatei.read()
i = 1
treffer=0
zeichen = {}
while i < 255:
    treffer = text.count(chr(i))
    if treffer > 0:
        zeichen[chr(i)] = treffer
    i += 1
sortierteliste = sorted(zeichen.items(), key=lambda x:x[1])
sortdict = dict(sortierteliste)
for key, value in sortdict.items():
    print(f'Zeichen: {key}, Anzahl: {value}')
