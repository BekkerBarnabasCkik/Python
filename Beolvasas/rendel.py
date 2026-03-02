def beolvasas(fajl):
    f=open(fajl, "r", encoding="utf-8")
    t=f.readlines()
    f.close()
    joadatok=[]
    for i in range(len(t)):
        sor=t[i].strip().split()
        joadatok.append((int(sor[0]), sor[1], int(sor[2])))
    
    return joadatok

def kiiras(adatok):
    for i in range(len(adatok)):
        for j in range(len(adatok[i])):
            if j!=len(adatok[i])-1:
                print(adatok[i][j], end=", ")
            else:
                print(adatok[i][j])

def main(fajl):
    adatok=beolvasas(fajl)
    kiiras(adatok)

main("rendel.txt")