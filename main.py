#Zadanie1
def poloncz(imie,nazwisko):
    return imie[0]+"."+nazwisko
print(poloncz('bartosz','gorski'))
#Zadanie2
def poloncz2(imie,nazwisko):
    imietemp = imie.capitalize()
    nazwisko = nazwisko.capitalize()
    return imietemp[0]+"."+nazwisko
print(poloncz2('bartosz','gorski'))
#Zadanie3
def sprawdzuro(dwadziescia,dekadairok,wiek):
    rok = dwadziescia*100+dekadairok
    return rok-wiek
print(sprawdzuro(20,22,21))
#Zadanie4
def zadanie4(imie,nazwisko,funkcja):
    return (funkcja(imie,nazwisko))
print(zadanie4('bartosz','gorski',poloncz2))
#5
def dzielenie(a,b):
    if a > 0 and b > 0 and b != 0:
        return a/b
    else:
        print("jedna lub obie sa ujemne albo 2. jest 0")
        return 0
print(dzielenie(6,1))
#6
# suma = 0
# while suma < 100:
#     a = int(input(),10)
#     suma+=a
#     print(suma)
#7
lista1 = ['wololo',5,1,3,3]
def dokrotku(lista):
    return (*lista, )
print(dokrotku(lista1))
#8
# templist = []
# for x in range(6):
#     templist.append(input())
# print((*templist,))
#9
def dnitygodniazksiazki(x):
    dnitygodnia = {
        1: 'poniedzialek',
        2: 'wtorek',
        3: 'srododa',
        4: 'czwartek',
        5: 'piatek',
        6: 'sobota',
        7: 'niedziela'}
    return dnitygodnia[x]
print(dnitygodniazksiazki(6))
slowko = 'kamil limak'
def czypalindrom(slowo):
    temp = slowo[::-1]
    if temp == slowo:
        return True
    else:
        return False
print(czypalindrom(slowko))