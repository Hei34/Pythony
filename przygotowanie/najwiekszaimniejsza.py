lista1=[1,4,5,6,2,10,5,10]
def funkcjaznajdz(lista):
    max=0
    min=9999999
    for i in lista:
        if i>max:
            max=i
    for i in lista:
        if i<min:
            min=i
    tupelek=(max,min)
    return tupelek
print(funkcjaznajdz(lista1))
