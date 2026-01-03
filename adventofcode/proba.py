def Fajlbeolvasa():
    t=[2,3,4,1,3,13,1,2,0,0,3,24,5,63,4,65,3]
    ertekek=[]
    hossz=0
    ertek=0
    for i in t:
        if i!="":
            hossz+=1
            ertekek.append(int(i))
        else:
            hossz=0
    
    return ertekek, hossz
