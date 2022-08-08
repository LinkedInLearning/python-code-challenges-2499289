fibonacciListe=[0,1]
fZahl=0
#print(fibonacciListe[-1])
#print(fibonacciListe[-2])
i=0
while i < 10:
    fZahl=fibonacciListe[-1]+fibonacciListe[-2]
    fibonacciListe.append(fZahl)
    i = i + 1
print(fibonacciListe)
