import random as r
r.seed()
i = 0
zahlen = set()
while len(zahlen) < 6:
    i += 1
    zahlen.add(r.randint(1,49))
    
print(zahlen, i)

