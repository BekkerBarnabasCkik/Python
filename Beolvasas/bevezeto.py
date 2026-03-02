def fajlbeolvasas(fajl):
    t=[]
    f=open(fajl, "r", encoding="utf-8")
    osszesSor=f.readlines()
    for i in range(len(osszesSor)):
        adatok=osszesSor[i].strip().split(";")
        t.append((adatok[0], adatok[1], adatok[2], int(adatok[3]), int(adatok[4]), int(adatok[5])))
    f.close()   

    return t 

def kiiras(tomb):
    for i in range(len(tomb)):
        for j in range(len(tomb[i])):
            if j+1==len(tomb[i]):
                print(tomb[i][j])
                print()
            else:
                print(tomb[i][j], end=", ")



def main(fajl):
    t=fajlbeolvasas(fajl)
    kiiras(t)
main("szeleromu.txt")