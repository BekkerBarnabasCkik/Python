# #-----------------------Ea kiszámítása    1.1 Feladat------------------------------
# szamok=str(input()).split(",")
# ra=int(szamok[0])
# rb=int(szamok[1])
# ea=1/(1+pow(10, (rb-ra)/400))
# print(ea)
# #-----------------------------1.2 Feladat-----------------------------------
# import random
# szam=random.randint(0, 9)
# if szam<9:
#     s=1
# else:
#     s=0
# k=31
# print(f"A bekövetkezik, új értéke: {round(ra+(k*(1-ea)), 2)}")
# rUjNem=ra+(k*(0-ea))
# if rUjNem>=0:
#     print(f"A nem bekövetkezik új értéke: {round(rUjNem, 2)}")
# else:
#     print(f"A nem bekövetkezik új értéke: {0}")
# print()
# #----------------------2.1 Feladat------------------------------------
# hossz=10
# t=[]
# t2=[]
# for i in range(hossz):
#     ertek=random.uniform(0, 1000)
#     t.append(round(ertek, 2))
#     t2.append(round(ertek, 2))
#     print(f"{t[i]}_{i+1}")
# print()
# #--------------------2.2 Feladat-----------------------------------
# for i in range(hossz):
#     print(f"{i+1}: {t[i]} pont")
# #--------------------3.Feladat--------------------------------------
# poz=[0,0,0,0,0,0,0,0,0]
# for i in range(len(t)-1, 0, -1):
#     szam=0
#     while szam!=i:
#         if t[i]<t[szam]:
#             t.insert(szam, t[i])
#             t.pop(i+1)
#         else:
#             szam+=1
# print(t)
# print(t2)
# poz=[]
# for i in range(0, len(t), 1):
#     j=0
#     while t[i]!=t2[j]:
#         j+=1
#     poz.append(j)
# for i in range(0, len(t), 1):
#    print(f"{poz[i]+1}: {t[i]} pont")
# #-------------------4. Feladat-------------------------------------
# szam=int(input())
# i=0
# while szam!=poz[i]+1:
#     i+=1
# print(i)

import random
merkozesekszama=int(input())
print("----Kezdetek------")
hossz=10
t=[]
t2=[]
poz=[]
for i in range(hossz):
    ertek=random.uniform(0, 1000)
    t.append(round(ertek, 2))
    t2.append(round(ertek, 2))

for i in range(len(t)-1, 0, -1):
    szam=0
    while szam!=i:
        if t[i]<t[szam]:
            t.insert(szam, t[i])
            t.pop(i+1)
        else:
            szam+=1
for i in range(0, len(t), 1):
    j=0
    while t[i]!=t2[j]:
        j+=1
    poz.append(j)
for i in range(0, len(t), 1):
   print(f"{poz[i]+1}: {t[i]} pont")

valoszinuseg=0
for i in range(merkozesekszama):
    szam1=random.randint(1, hossz)
    szam2=random.randint(1, hossz)
    while szam1==szam2:
        szam1=random.randint(1, hossz)
        szam2=random.randint(1, hossz)
    valoszinuseg=random.randint(1,10)
    if valoszinuseg<10:
        valoszinuseg=1
    else:
        valoszinuseg=0
    ra=t[szam1-1]
    rb=t[szam2-1]
    ea=1/(1+pow(10, (rb-ra)/400))
    if valoszinuseg==1:
        t[szam1-1]=round(t[szam1-1]+(32*(1-ea)), 2)
        t[szam2-1]=round(t[szam1-1]+(32*(0-ea)), 2)
    else:
        t[szam1-1]=round(t[szam1-1]+(32*(0-ea)), 2)
        t[szam2-1]=round(t[szam1-1]+(32*(1-ea)), 2)
    if t[szam1-1]<0:
        t[szam1-1]=0
    elif t[szam2-1]<0:
        t[szam2-1]=0
    for i in range(len(t)-1, 0, -1):
        szam=0
        while szam!=i:
            if t[i]<t[szam]:
                t.insert(szam, t[i])
                t.pop(i+1)
                pozerdethely=szam
                pozerdetertek=poz[szam]
                poz.insert(szam, poz[i])
                poz.pop(i+1)
                poz.insert(pozerdethely+1, pozerdetertek)
                poz.pop(szam+1)
            else:
                szam+=1
t2=t
print("----Vége------")
for i in range(0, len(t), 1):
    j=0
    while t[i]!=t2[j]:
        j+=1
    poz.append(poz[j])
for i in range(0, len(t), 1):
   print(f"{poz[i]+1}: {t[i]} pont")
