def Fajlbeolvasas(fajl):
    f=open(fajl)
    t=f.read()
    f.close()
    ertek=""
    honnan=[]
    hova=[]
    mennyi=[]
    db=0
    osszes=0
    for i in range(len(t)):
        i=t[i].strip()
        if i!="" and i!=":" and i!="\n":
            ertek+=i
        else:
            if i==":":
                honnan.append(ertek)
                osszes+=db
                mennyi.append(db)
                db=0
                ertek=""
            elif i=="" and ertek!="":
                hova.append(ertek)
                db+=1
                ertek=""
    hova.append(ertek)
    mennyi.append(len(hova)-osszes)
    mennyi.pop(0)

    return honnan, hova, mennyi

def Kereses(honnan, mit):
    i=0
    while honnan[i]!=mit:
        i+=1
    
    return i

# def Vegigmenes(hova, mennyi, honna):
    

def Feladat(honnan, hova, mennyi):
    you=Kereses(honnan, "you")
    for i in range(mennyi[i]):
        osszes=0
        for j in range(you):
            osszes+=mennyi[i]
        poz=Kereses(honnan, hova[osszes+i])
        # Vegigmenes(hova, mennyi, honnan, poz)



def main():
    honnan, hova, mennyi=Fajlbeolvasas("proba.txt")
    Feladat(honnan, hova, mennyi)
