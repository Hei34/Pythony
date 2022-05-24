def silnia(n):
    s = 1
    for i in range(2, n+1):
        s *= i
    return s
def symbolneutona(n,k):
    if 0<=k<=n:
        return (silnia(n)/(silnia(k)*silnia(n-k)))
    else:
        print("zle wartosci")
        return 0

print(symbolneutona(8,5))

print([i**3 for i in range(1,30)])
