def otodik():
    print("\tA mikulás manói olyan csomagoló papírt készítenek ami kézzel van megírva.\n\tMondanak két számot a köztük lévő negatív számok helyett * elválasztva írják le.\n\tpl.:  be: (-7,-2)  ki: -7*-6*-5*-4*-3*-2")
    eleje = int(input("Első szám: "))
    vege = int(input("Második szám: "))

    print("A végeredmény:")
    if eleje < vege:
        for i in range(eleje, vege, 1):
            print(i, end="*")
        print(vege)
    else:
        for i in range(vege, eleje, 1):
            print(i, end="*")
        print(eleje)