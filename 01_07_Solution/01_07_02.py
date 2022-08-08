import random
random.seed()
def zufall():
    i = 0
    zahlen=[]
    while i < 6:
        x = random.randint(1,49)
        if x in zahlen:
            print("Schon vorhanden",x)
            continue
        zahlen.append(x)
        i += 1
    return zahlen
print(zufall())
