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
from typing import Any

class Node:
    value: Any
    next: 'Node'
    def __init__(self, v1):
        self.value = v1
        self.next = None
    def __str__(self):
        return '[' + str(self.value)+ ' -> ' + str(self.next.value) + ']'
class LinkedList:
    head: Node
    tail: Node
    def __init__(self):
        self.head = None

    def push(self, v1):
        nnode = Node(v1)
        nnode.next = self.head
        self.head = nnode
    def append(self,v1):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = Node(v1)
        self.tail = temp
    def __str__(self):
        result = ""
        node = self.head
        if node != None:
            result += str(node.value)
            node = node.next
            while node:
                result += " -> " + str(node.value)
                node = node.next
        return result

lista1 = LinkedList()

lista1.push(5)
lista1.push(2)
lista1.push(6)
lista1.append(3)
lista1.append(4)
lista1.push(1)

print(lista1)
print(lista1.head)
print(lista1.head.next)
print(lista1.tail)

