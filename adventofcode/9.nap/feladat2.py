import math

def fajlbeovlasas(fajlNev):
    f=open(fajlNev)
    t=f.read()
    f.close()
    ertekek=[]
    ertek=""
    x=[]
    y=[]
    for i in t:
        i=i.strip()
        if i!="," and i!="":
            ertek+=i
        elif i=="," and ertek!="":
            x.append(int(ertek))
            ertek=""
        elif ertek!="":
            y.append(int(ertek))
            ertek=""
    y.append(int(ertek))

    return x, y 

# def terulet(x, y, i, j):
#     return (abs(x[j]-x[i])+1)*(abs(y[j]-y[i])+1)


#----------------------------ChatGPT---------------------------

# def eldonters(joy, jox, x, y):
#     metszesek=0
#     for i in range(len(x)):
#         Ax=x[i]
#         Ay=y[i]
#         Bx=x[(i+1)%len(x)]
#         By=y[(i+1)%len(x)]
#         if (Ay > joy and By <= joy) or (Ay <= joy and By > joy):
#             x_metszes=Ax+(joy-Ay)*(Bx-Ax)/(By-Ay)
#             if x_metszes>jox:
#                 metszesek+=1
    
#     if metszesek%2!=0:
#         return True
#     else:
#         return False

#-------------------------ChatGPT-------------------------




#------------------Saját------------------------------------

# def balFelso(jox, joy, x, y):
#     return (jox>=x and joy<=y)

# def jobbFelso(jox, joy, x, y):
#     return (jox<=x and joy<=y)

# def balAlso(jox, joy, x, y):
#     return (jox>=x and joy>=y)

# def jobbAlso(jox, joy, x, y):
#     return (jox<=x and joy>=y)

# def BalFelsoVizsgalat(jox, joy, x, y, i, egy, db):
#     if egy==False and balFelso(jox, joy, x[i], y[i]):
#         egy=True
#         db+=1

#     return db, egy

# def JobbFelsoVizsgalat(jox, joy, x, y, i, ketto, db):
#     if ketto==False and jobbFelso(jox, joy, x[i], y[i]):
#         ketto=True
#         db+=1

#     return db, ketto

# def BalAlsoVizsgalat(jox, joy, x, y, i, harom, db):
#     if harom==False and balAlso(jox, joy, x[i], y[i]):
#         harom=True
#         db+=1

#     return db, harom

# def JobbAlsoVizsgalat(jox, joy, x, y, i, negy, db):
#     if negy==False and jobbAlso(jox, joy, x[i], y[i]):
#         negy=True
#         db+=1

#     return db, negy

# def Eldontes(jox, joy, x, y):
#     egy=False
#     ketto=False
#     harom=False
#     negy=False
#     osszes=False
#     i=0
#     db=0
#     while i<len(x) and osszes==False:
#         db, egy=BalFelsoVizsgalat(jox, joy, x, y, i, egy, db)
#         db, ketto=JobbFelsoVizsgalat(jox, joy, x, y, i, ketto, db)
#         db, harom=BalAlsoVizsgalat(jox, joy, x, y, i, harom, db)
#         db, negy=JobbAlsoVizsgalat(jox, joy, x, y, i, negy, db)
#         if db==4:
#             osszes=True
#         i+=1
    
#     return osszes

# def Feltetel(k, jox, joy, x, y):
#     return k<2 and Eldontes(jox[k], joy[len(joy)-(k+1)], x, y)

# def maxterEldontes(x, y, i, j, ter, maxter):
#     jox=[x[i], x[j]]
#     joy=[y[i], y[j]]
#     k=0
#     while Feltetel(k, jox, joy, x, y):
#         k+=1
#     if k==2:
#         return ter
#     else:
#         return maxter

# def Terulet(x, y, i, j, maxter):
#     ter=terulet(x, y, i, j)
#     if ter>maxter:
#         maxter=maxterEldontes(x, y, i, j, ter, maxter)

#     return maxter
# def Kivalasztas(x, y):
#     maxter=0
#     for i in range(len(x)):
#         for j in range(i+1, len(x), 1):
#             maxter=Terulet(x, y, i, j, maxter)
                    
#     print(maxter)



# ertekek=fajlbeovlasas("proba.txt")
# x=ertekek[0]
# y=ertekek[1]
# Kivalasztas(x, y)



# def eldonters(joy, jox, x, y):
#     metszesek=0
#     for i in range(len(x)):
#         Ax=x[i]
#         Ay=y[i]
#         Bx=x[(i+1)%len(x)]
#         By=y[(i+1)%len(x)]
#         if (Ay>joy) != (By > joy):
#             x_metszes=Ax+(joy-Ay)*(Bx-Ax)/(By-Ay)
#             if x_metszes>jox:
#                 metszesek+=1
    
#     if metszesek%2!=0:
#         return True
#     else:
#         return False

# def maxterEldontes(x, y, i, j, ter, maxter):
#     jox=[x[i], x[j]]
#     joy=[y[i], y[j]]
#     db=0
#     print(jox)
#     for k in range(2):
#         if eldonters(joy[k], jox[len(jox)-(k+1)], x, y):
#             db+=1
#     if db==2:
#         return maxter
#     else:
#         return ter
    
# def terulet(x, y, i, j):
#     return (abs(x[i]-x[j])*abs(y[i]-y[j]))

# def TerEldontes(x, y, i, j, maxter):
#     ter=terulet(x, y, i, j)
#     print(ter, maxter)
#     if int(ter)>maxter:
#         maxter=maxterEldontes(x, y, i, j, ter, maxter)

#     return maxter

# def Kivalasztas(x, y):
#     maxter=0
#     for i in range(len(x)):
#         for j in range(i+1, len(x), 1):
#             maxter=TerEldontes(x, y, i, j, maxter)
                    
#     print(maxter)



# ertekek=fajlbeovlasas("proba.txt")
# x=ertekek[0]
# y=ertekek[1]
# Kivalasztas(x, y)

# def Eldontes(jox, joy, x, y):
#     metszes=0
#     for i in range(len(x)):
#         Ay=y[i]
#         Ax=x[i]
#         By=y[(i+1)%len(y)]
#         Bx=x[(i+1)%len(x)]
#         if (Ay>joy) != (By>joy):
#             x_metszes=Ax + (joy - Ay) * (Bx - Ax) / (By - Ay)
#             if x_metszes>jox:
#                 metszes+=1
            
#     if metszes%2!=0:
#         return True
#     else:
#         return False

# def MaxterMeghatarozas(x, y, i, j, maxter):
#     bent = Eldontes(x[i], y[i], x, y) and Eldontes(x[j], y[j], x, y)

#     if bent:
#         return TeruletMeghatarozas(x, y, i, j)
#     else:
#         return maxter




# def TeruletMeghatarozas(x, y, i, j):
#     return abs(x[i]-x[j])*abs(y[i]-y[j])

# def Feladat(x, y):
#     maxter=0
#     for i in range(len(x)):
#         for j in range(i+1, len(x), 1):
#             if TeruletMeghatarozas(x, y, i, j)>maxter:
#                 maxter=MaxterMeghatarozas(x, y, i, j, maxter)
#     print(maxter)

# def main():
#     x, y=fajlbeovlasas("proba.txt")
#     Feladat(x, y)

# main()


#-------------------------------------------- uj proba--------------------------------

# def tomegkkozeppont(x, y):
#     osszes=0
#     for i in range(len(x)):
#         osszes+=x[i]
#         osszes+=y[i]

#     return osszes/((len(x)-1)*2)

# def szog(x, y):
#     return math.atan2()

# def terulet(x, y, i, j):
#     return (abs(x[i]-x[j])*abs(y[i]-y[j]))

# def TerEldontes(x, y, i, j, maxter):
#     ter=terulet(x, y, i, j)
#     print(ter, maxter)
#     if ter>maxter:
#         maxter=maxterEldontes(x, y, i, j, ter, maxter)


# def Kivalasztas(x, y):
#     maxter=0
#     for i in range(len(x)):
#         for j in range(i+1, len(x), 1):
            
#     print(maxter)

def Terulet(x, y, i, j):
    return abs(x[i]-x[j])*abs(y[i]-y[j])


def kozrefogas(Ay, By, joy):
    return (Ay>joy) != (By>joy)

def x_metszes(joy, Ay, By, Bx, Ax):
    return ((Bx-Ax)*(joy-Ay))/(By-Ay)+Ax

def vizsgalat(Ay, By, joy, jox, Bx, Ax, metszes):
    if kozrefogas(Ay, By, joy):
        if jox<x_metszes(joy, Ay, By, Bx, Ax):
            metszes+=1

    return metszes

def eldontes(jox, joy, x, y):
    metszes=0
    for i in range(len(x)):
        Ay=y[i]
        Ax=x[i]
        By=y[(i+1)%len(y)]
        Bx=x[(i+1)%len(x)]
        metszes =vizsgalat(Ay, By, joy, jox, Bx, Ax, metszes)
    print(metszes)

    return metszes%2!=0
        

def Feladat(x, y):
    maxter=0
    for i in range(len(x)):
        for j in range(i+1, len(x), 1):
            if Terulet(x, y, i, j)>maxter:
                jox=[x[i], x[j]]
                joy=[y[j], y[i]]
                jo=True
                for k in range(2):
                    if not eldontes(jox[k], joy[k], x, y):
                        jo = False
                        print("test")

                if jo:
                    maxter = Terulet(x, y, i, j)
                    print("Új max:", maxter)
    
    print(maxter)



def main():
    x, y=fajlbeovlasas("proba.txt")
    Feladat(x, y)

main()

