import sys 
def IsPrime(value):
    if value <= 1:
        return False;
    elif value > 2:
        i = 2
        while i <= (value / 2) + 1:
            if value % i == 0:
              return False;
            i+=1
    return True

print("Bitte geben Sie die unterer Grenze des Zahlenbereichs ein (mindestens der Wert 2): ")
low = int(input())
if low < 2:
    sys.exit("Die untere Grenze des Zahlenbereichs muss mindestens 2 betragen");
    
print("Bitte geben Sie die obere Grenze des Zahlenbereichs ein (maximal 1000):   ");
high = int(input())
if high > 1000:
    sys.exit("Die obere Grenze des Zahlenbereichs ist 1000");
if high < low:
    sys.exit("Die obere Grenze des Zahlenbereichs darf nicht kleiner als die untere Grenze sein");

i = low
while i <= high:
    if IsPrime(i):
          print(i)
    i+=1
    
