def Fajlbeolvasas(fajl):
    f=open(fajl)
    f2=open(fajl)
    hossz=hosszmeghatarozas(f2)
    t=f.read()
    f.close()
    ertekek=[]
    for i in t:
        if i=="S" or i=="." or i=="^":
            ertekek.append(i.strip())

    return hossz, ertekek

def hosszmeghatarozas(tömb):
    t=tömb.readline()
    
    return len(t)-1

def main(fajl):
    ertekek=Fajlbeolvasas("proba.txt")
    hossz=ertekek[0]
    t=ertekek[1]

    print(hossz)
    print(t)

main("proba.txt")

# def feladat():

