import random

def szerencse():
    szam=random.randint(1, 40)

    if szam%2!=0:
        return szam/2
    else:
        return (szam+1)/2

print(f"Béla vagyok, szerencse számám a(z) {szerencse()}, kedvenc színem a piros.")

#2.feladat

nev=str(input())
szam=random.randint(2, 12)
t=[]
def tabla(t, szam):
    t=[szam]
    for i in range(9):
        t.append(szam+(i+1)*5)
