import random
from time import sleep
def One():
    listaTrue = []
    listaFalse = []
    print("Renderuje losowe liczby - One")
    for i in range(100):
        zmiena = random.randint(0,100)
        if zmiena <= 50:
            listaFalse.append("0")
        else:
            listaTrue.append("1")
    print("ListaTrue", listaTrue)
    zmiena1 = len(listaTrue)
    print(zmiena1)
    print("ListaFalse", listaFalse)
    zmiena2 = len(listaFalse)
    print(zmiena2)
    if zmiena1 == 50 or zmiena2 == 50:
        eh = "50% na 50%"
        return eh
    elif zmiena1 >= 50:
        return True
    elif zmiena2 >= 50:
        return False

def Two():
    listaPa = []
    listaNpa = []
    print("Renderuje losowe liczby - Two")
    for i in range(100):
        zmiena = random.randint(0,100)
        if zmiena % 2 == 0:
            listaPa.append("1")
        else:
            listaNpa.append("0")
    print("Parzyste:",listaPa)
    zmiena1 = len(listaPa)
    print(zmiena1)
    print("Nie Parzyste:",listaNpa)
    zmiena2 = len(listaNpa)
    print(zmiena2)
    if zmiena1 == 50 or zmiena2 == 50:
        eh = "50% na 50%"
        return eh
    elif zmiena1 >= 50:
        print("Parzystych więcej")
        return True
    elif zmiena2 >= 50:
        print("Nie parzystych więcej")
        return False
    
def Three():
    listaPa = []
    listaNpa = []
    print("Renderuje losowe liczby - Three")
    for i in range(100):
        zmiena = random.randint(0,100)
        if zmiena % 2 != 0:
            listaNpa.append("1")
        else:
            listaPa.append("0")
    print("Nie Parzyste:",listaNpa)
    zmiena2 = len(listaNpa)
    print(zmiena2)
    print("Parzyste:",listaPa)
    zmiena1 = len(listaPa)
    print(zmiena1)
    if zmiena1 == 50 or zmiena2 == 50:
        eh = "50% na 50%"
        return eh
    elif zmiena2 >= 50:
        print("Nie parzystych więcej")
        return True
    elif zmiena1 >= 50:
        print("Parzystych więcej")
        return False
    
def Fore():
    listaTrue = []
    listaFalse = []
    print("Renderuje losowe liczby - One")
    for i in range(100):
        zmiena = random.randint(0,100)
        if zmiena <= 50:
            listaFalse.append("0")
        else:
            listaTrue.append("1")
    print("ListaTrue", listaTrue)
    zmiena1 = len(listaTrue)
    print(zmiena1)
    print("ListaFalse", listaFalse)
    zmiena2 = len(listaFalse)
    print(zmiena2)
    if zmiena1 == 50 or zmiena2 == 50:
        eh = "50% na 50%"
        return eh
    elif zmiena1 >= 50:
        return False
    elif zmiena2 >= 50:
        return True

def Five():
    x = random.randint(3,5)
    q = random.randint(10, 20)
    w = random.randint(21, 30)
    zmiena = random.randint(q,w)
    print("q",q)
    print("w",w)
    print("x",x)
    print("zmiena",zmiena)
    for i in range(x):
        e = random.randint(1,3)
        print("e",e)
        if e == 1:
            print("-------------")
            q = random.randint(1, 50)
            w = random.randint(51, 101)
            r = random.randint(q,w)
            print("r =",r)
            print("zmiena =",zmiena)
            zmiena = zmiena + r
            print("zmiena + r =",zmiena)
            print("-------------")
        if e == 2:
            print("-------------")
            q = random.randint(1, 50)
            w = random.randint(51, 101)
            r = random.randint(q,w)
            print("r =",r)
            print("zmiena =",zmiena)
            zmiena = zmiena * r
            print("zmiena * r =",zmiena)
            print("-------------")
        if e == 3:
            print("-------------")
            q = random.randint(1, 50)
            w = random.randint(51, 101)
            r = random.randint(q,w)
            print("r =",r)
            print("zmiena =",zmiena)
            zmiena = zmiena - r
            print("zmiena - r =",zmiena)
            print("-------------")

    if  zmiena % 2 == 0:
        return True
    else:
        return False

def Six():
    x = random.randint(3,5)
    q = random.randint(10, 20)
    w = random.randint(21, 30)
    zmiena = random.randint(q,w)
    print("q",q)
    print("w",w)
    print("x",x)
    print("zmiena",zmiena)
    for i in range(x):
        e = random.randint(1,3)
        print("e",e)
        if e == 1:
            print("-------------")
            q = random.randint(1, 50)
            w = random.randint(51, 101)
            r = random.randint(q,w)
            print("r =",r)
            print("zmiena =",zmiena)
            zmiena = zmiena + r
            print("zmiena + r =",zmiena)
            print("-------------")
        if e == 2:
            print("-------------")
            q = random.randint(1, 50)
            w = random.randint(51, 101)
            r = random.randint(q,w)
            print("r =",r)
            print("zmiena =",zmiena)
            zmiena = zmiena * r
            print("zmiena * r =",zmiena)
            print("-------------")
        if e == 3:
            print("-------------")
            q = random.randint(1, 50)
            w = random.randint(51, 101)
            r = random.randint(q,w)
            print("r =",r)
            print("zmiena =",zmiena)
            zmiena = zmiena - r
            print("zmiena - r =",zmiena)
            print("-------------")

    if  zmiena % 2 != 0:
        return True
    else:
        return False
        
def PuNaPu():
    listaTrue = []
    listaFalse = []
    reOne = One()
    reTwo = Two()
    reThree = Three()
    reFore = Fore()
    reFive = Five()
    reSix = Six()
    sleep(1)
    print("One:",reOne)
    sleep(1)
    print("Two:",reTwo)
    sleep(1)
    print("Three:",reThree)
    sleep(1)
    print("Fore:",reFore)
    sleep(1)
    print("Five:",reFive)
    sleep(1)
    print("Six:",reSix)
    sleep(2)
    if reOne == True:
        listaTrue.append("1")
    else:
        listaFalse.append("0")
    if reTwo == True:
        listaTrue.append("1")
    else:
        listaFalse.append("0")
    if reThree == True:
        listaTrue.append("1")
    else:
        listaFalse.append("0")
    if reFore == True:
        listaTrue.append("1")
    else:
        listaFalse.append("0")
    if reSix == True:
        listaTrue.append("1")
    else:
        listaFalse.append("0")
    lol = len(listaTrue)
    lolz = len(listaFalse)
    if lol == lolz:
        print("50% na 50%")
    elif lolz < lol:
        print("<-----True----->")
        print("Czy opłaca sie podjąć ryzyko i -",zmiena)
        print("no coż... Ryzykuj!")
        
    elif lol < lolz:
        print("<-----False----->")
        print("Czy opłaca sie podjąć ryzyko i -",zmiena)
        print("no coż... NIE Ryzykuj!")
    

if __name__ == "__main__":
    print("----start-----")
    print("Czy opłaca sie podjąć ryzyko i -")
    zmiena = input()
    sleep(5)
    PuNaPu()
