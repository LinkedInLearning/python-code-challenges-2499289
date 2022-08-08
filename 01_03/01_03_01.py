def fibonacciZahlen(n):
    if n > 1:
        return fibonacciZahlen(n-1) + fibonacciZahlen(n-2)
    return n
for i in range(10):
    print(fibonacciZahlen(i))
