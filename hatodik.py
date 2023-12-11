import random

def intervallum():
    eleje = int(input("Adja meg az intervellum alsó határát!"))
    vege = int(input("Adja meg az intervellum felső határát!"))
    return eleje
    return vege
def hatodik():
    lista = []
    index = 1
    eleje = intervallum(eleje)
    vege = intervallum(vege)
    while index < 21:
        szam = random.randint(eleje, vege)
        lista.append(szam)
        index += 1
    return lista
def kiiratas():
    lista = hatodik()
    print(lista)
    for index in range(0, len(lista), 3):
        print(lista[index], end=" ")
        if lista[index] < 0:
            print("")

