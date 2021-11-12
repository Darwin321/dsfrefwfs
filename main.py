import random
from tkinter import * 
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
    print("One:",reOne)
    test1.configure(text=f"Test - 1 = {reOne}")
    print("Two:",reTwo)
    test2.configure(text=f"Test - 2 = {reTwo}")
    print("Three:",reThree)
    test3.configure(text=f"Test - 3 = {reThree}")
    print("Fore:",reFore)
    test4.configure(text=f"Test - 4 = {reFore}")
    print("Five:",reFive)
    test5.configure(text=f"Test - 5 = {reFive}")
    print("Six:",reSix)
    test6.configure(text=f"Test - 6 = {reSix}")
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
        tekst7.configure(text="50% na 50%")
    elif lolz < lol:
        print("<-----True----->")
        tekst7.configure(text="no coż... Ryzykuj!")
    elif lol < lolz:
        print("<-----False----->")
        tekst7.configure(text="no coż... NIE Ryzykuj!")
    sleep(5)

if __name__ == "__main__":
    print("----start-----")
    zmiena = input()
    window = Tk()
    window.title("Pomagier w decyzjach życiowych")
    window.geometry("850x595")
    tlo2 = Canvas(window, bg="#1e1e1e", height=600, width=40)
    tlo2.place(x=-5,y=-5) #1e1e1e
    tlo3 = Canvas(window, bg="#1e1e1e", height=600, width=40)
    tlo3.place(x=825,y=-5) #1e1e1e
    tlo1 = Label(window, bg="#252526", height=50, width=100)
    tlo1.pack()
#label = tkinter.Label(window_main, text="Witaj! HeHe", foreground="red",font=("Alien encounters", 50), bg="black", width=900,height=2)
    tekst = Label(window, text="Czy opłaca się podjąć ryzyko i -",foreground="#86b5d3", font=("Arial",35), bg="#252526")
    tekst.place(x=100,y=0)
    tekst1 = Label(window, text=zmiena,foreground="#86b5d3", font=("Arial",30), bg="#252526")
    tekst1.place(x=50,y=50)
    test1 = Label(window, text="Test - 1 =",foreground="Black", font=("Arial",35), bg="#252526")
    test1.place(x=50,y=100)
    test2 = Label(window, text="Test - 2 =",foreground="Black", font=("Arial",35), bg="#252526")
    test2.place(x=50,y=150)
    test3 = Label(window, text="Test - 3 =",foreground="Black", font=("Arial",35), bg="#252526")
    test3.place(x=50,y=200)
    test4 = Label(window, text="Test - 4 =",foreground="Black", font=("Arial",35), bg="#252526")
    test4.place(x=50,y=250)
    test5 = Label(window, text="Test - 5 =",foreground="Black", font=("Arial",35), bg="#252526")
    test5.place(x=50,y=300)
    test6 = Label(window, text="Test - 6 =",foreground="Black", font=("Arial",35), bg="#252526")
    test6.place(x=50,y=350)

    tekst7 = Label(window, text="",foreground="Red", font=("Arial",40), bg="#252526")
    tekst7.place(x=250,y=405) #no coż... Ryzykuj!

    button = Button(window, text="Boże, Dopomóż",bg="#1e1e1e", height=3,width=60, font=("Arial",20), command=PuNaPu)
    button.place(x=-5,y=490)
    window.mainloop()
