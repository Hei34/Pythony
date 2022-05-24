def fibonaciii(n):
    if n<=1:
        return n
    else:
        return (fibonaciii(n-1)+fibonaciii(n-2))
print(fibonaciii(11))

def sumatrzecichpoteng(n):
    suma=0
    for i in range(1,n+1):
        suma+=i**3
    return suma
print(sumatrzecichpoteng(3))
slowniczek={1:'jablko',2:'jablko',3:'banan'}

def slownikbezpow(slownik):
    slownik2=set(slownik.values())
    return slownik2
print(slownikbezpow(slowniczek))