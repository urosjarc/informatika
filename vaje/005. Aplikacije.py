import random


def vnos_stevil():
    while(True):
        a = int(input("Vnesi stevilo: "))
        if(a == 0):
            print("Konec")
            break

def vsota_stevil():
    vsota = 0
    while(True):
        a = int(input("Vnesi stevilo: "))
        if(a == 0):
            print(f"Vsota je: {vsota}")
            break
        vsota = vsota + a

def najvecja_stevilka():
    n = 0
    while(True):
        a = int(input("Vnesi stevilo: "))
        if(a == 0):
            print(f"Najvecja je: {n}")
            break
        if(a > n):
            n = a

def povprecje():
    vsota = 0
    n = 0
    while(True):
        a = int(input("Vnesi stevilo: "))
        if(a == 0):
            print(f"Povprecje je: {vsota/n}")
            break
        vsota = vsota + a
        n = n + 1

def ugibanje_stevil():
    r = random.randint(0, 100)
    c = 0
    while(True):
        a = int(input("Vnesi stevilo: "))
        c = c + 1
        if(a == r):
            print(f"Uganil si v: {c} poskusu!")
            break
        elif(a > r):
            print("Prevelika je")
        else:
            print("Premajhna je")
