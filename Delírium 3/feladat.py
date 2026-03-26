def Almok(n):
    if n!=5:
        for i in range(n):
            print("", end=" ")
        print(f"Az aktuális szint: {n}")
        Almok(n+1)
        for i in range(n):
            print("", end=" ")
        print(f"Elindultunk vissazfele, az aktuális szint: {n}")
    else:
        for i in range(n):
            print("", end=" ")
        print(f"Elértük a célt")

Almok(0)

import math

def KristalyFeltores(n, eredetiN, pont):
    pont=0
    if n!=1:
        pont=KristalyFeltores(n-1, eredetiN, pont)
        for i in range(n):
            print("*", end=" ")
        print()
        return pont+math.pow(2, eredetiN-n)*(n*10)
    else:
        for i in range(n):
            print("*", end=" ")
        print()
        return math.pow(2, eredetiN-n)*(n*10)

print(KristalyFeltores(4, 4, 0))

def Menekules(tomb, ugras, poz):
    if (poz<len(tomb) and ugras!=100):
        if tomb[poz]%2==0:
            poz+=2
        else:
            poz-=1
        Menekules(tomb, ugras+1, poz)
    else:
        if ugras!=100 and (poz<0 or poz>=len(tomb)):
            print(f"Sikeres kiszabadulás a(z) {ugras}. szinten ")
        else:
            print(f"Nem sikerült kiszabadulni")

Menekules([2,3,4], 0, 0)
