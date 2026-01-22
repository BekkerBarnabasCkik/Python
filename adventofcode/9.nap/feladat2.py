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

def tavolsag(x, y, i, j):
    return (abs(x[j]-x[i])+1)*(abs(y[j]-y[i])+1)



# def eldonters(joy, jox, x, y):
#     metszesek=0
#     i=0
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

# def balFelso(jox, joy, x, y):
#     return (jox>=x and joy<=y)

# def jobbFelso(jox, joy, x, y):
#     return (jox<=x and joy<=y)

# def balAlso(jox, joy, x, y):
#     return (jox>=x and joy>=y)

# def jobbAlso(jox, joy, x, y):
#     return (jox<=x and joy>=y)

# def Eldontes(jox, joy, x, y):
#     egy=False
#     ketto=False
#     harom=False
#     negy=False
#     osszes=False
#     i=0
#     db=0
#     while i<len(x) and osszes==False:
#         if egy==False and balFelso(jox, joy, x[i], y[i]):
#            egy=True
#            db+=1
#         if ketto==False and jobbFelso(jox, joy, x[i], y[i]):
#             ketto=True
#             db+=1
#         if harom==False and balAlso(jox, joy, x[i], y[i]):
#            harom=True
#            db+=1
#         if negy==False and jobbAlso(jox, joy, x[i], y[i]):
#             negy=True
#             db+=1
#         if db==4:
#             osszes=True
#         i+=1
    
    # return osszes


def Kivalasztas(x, y):
    maxter=0
    for i in range(len(x)):
        for j in range(i+1, len(x), 1):
            ter=tavolsag(x, y, i, j)
            if ter>maxter:
                jox=[x[i], x[j]]
                joy=[y[i], y[j]]
                # k=0
                # while k<2 and Eldontes(jox[k], joy[len(joy)-(k+1)], x, y):
                #     k+=1
                # if k==2:
                #     maxter=ter
                #     print(maxter)
                    
    print(maxter)



ertekek=fajlbeovlasas("be.txt")
x=ertekek[0]
y=ertekek[1]
Kivalasztas(x, y)






# FÜGGVÉNY Pont_Benne_Van_E_Sokszögben(
#     PONT_X, PONT_Y,
#     SOKSZÖG_X, SOKSZÖG_Y
# ):

#     metszések = 0
#     n = SOKSZÖG_X hossza

#     CIKLUS i = 0-tól n-1-ig:

#         Ax = SOKSZÖG_X[i]
#         Ay = SOKSZÖG_Y[i]

#         Bx = SOKSZÖG_X[(i + 1) mod n]
#         By = SOKSZÖG_Y[(i + 1) mod n]

#         HA (Ay > PONT_Y) != (By > PONT_Y):

#             x_metszés =
#                 Ax + (PONT_Y - Ay) * (Bx - Ax) / (By - Ay)

#             HA PONT_X < x_metszés:
#                 metszések = metszések + 1

#     HA metszések páratlan:
#         VISSZA true
#     KÜLÖNBEN:
#         VISSZA false

