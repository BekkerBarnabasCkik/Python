print("1-Add meg a nevet")
print("2-Üdv (nev)")
print("3-Helló (nev)")
print("4-Szia (nev)")
print("5-Kilépés")
szam=int(input())
nev=""
while szam!=5:
    if szam==1:
        nev=str(input("Írd be a neved: "))
    else:
        if szam==2:
            print(f"Üdv: {nev}")
        elif szam==3:
            print(f"Helló {nev}")
        elif szam==4:
            print(f"Szia {nev}")
    szam=int(input())

        

