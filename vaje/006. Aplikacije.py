
def vsota_do_sto():
    v = 0
    for i in range(0, 101, 1):
        v = v + i
    print(f"Vsota je: {v}")

def vsota_do_stevila():
    v = 0
    m = int(input("Vnesi stevilo: "))
    for i in range(0, m, 1):
        v = v + i
    print(f"Vsota je: {v}")

def vsota_do_argumenta(m):
    v = 0
    for i in range(0, m, 1):
        v = v + i
    print(f"Vsota je: {v}")

def liha_soda(a):
    if(a % 2 == 0):
        print("Stevilka a je soda")
    else:
        print("Stevilka a ni soda")

def vsi_delitelji(a):
    for i in range(1, a+1, 1):
        if(a % i == 0):
            print(f"Delitelj: {i}")

def prastevilo(a):
    d = 0
    for i in range(2, a, 1):
        if(a % i == 0):
            d = d + 1
    if(d == 0):
        print("Je prastevilo")

def najvecji_delitelj(a):
    for i in range(a, 0, -1):
        if(a % i == 0):
            print(f"Najvecji delitelj: {i}")
            break

def najvecji_skupni_delitelj(a, b):
    d = 1
    if(a > b):
        m = a
    else:
        m = b
    for i in range(1, m, 1):
        if(a % i == 0 and b % i == 0):
            d = i
    print(d)

vsi_delitelji(12)
