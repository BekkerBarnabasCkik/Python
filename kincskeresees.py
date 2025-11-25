# oldal=int(input())
# t=[]
# szammax=oldal*oldal+1
# for i in range(1, szammax, 1):
#     t.append(i)
# #-----------------------------------Mátrix lista létrehozása------------------------------------------
# import random
# irany=random.randint(1, 4)
# betuk=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# alkalmak=[]
# kordinatak=[]
# for i in range(0, len(betuk), 1):
#     szam=random.randint(1, szammax)
#     db=0
#     if szam>oldal and irany==1:
#         szam-=oldal
#         db+=1
#     elif szam<(szammax-oldal+1) and irany==3:
#         szam+=oldal
#         db+=1
#     elif (szam-1)%oldal!=0 and irany==2:
#         szam-=1
#         db+=1
#     elif szam%oldal!=0 and irany==4:
#         szam+=1
#         db+=1
#     kordinatak.append(szam)
#     #-----------------------Első mozdulás----------------------
#     while szam>oldal and (szam-1)%oldal!=0 and szam/oldal<=(oldal-1) and szam%oldal!=0:
#         irany=random.randint(1, 4)
#         if szam>oldal and irany==1:
#             szam-=oldal
#             db+=1
#         elif szam<(szammax-oldal+1) and irany==3:
#             szam+=oldal
#             db+=1
#         elif (szam-1)/oldal!=0 and irany==2:
#             szam-=1
#             db+=1
#         elif szam%oldal!=0 and irany==4:
#             szam+=1
#             db+=1
#         kordinatak.append(szam)
#     alkalmak.append(db)
#     kordinatak.append(" ")
# #-----------------------------Vonalak létrehozása és hosszúságuknak lejegyzése---------------------------
# max=0
# poz=0
# for i in range(0, len(alkalmak), 1):
#     if alkalmak[i]>max:
#         max=alkalmak[i]
#         poz=i
# print(f"A legtöbb kordinátával rendelkező vonal a(z) {betuk[poz]} vonal volt ami {max} elemmel rendelkezik és a lehetséges vonalak közül a {poz}. vonal volt.")
# #--------------------------------Legnagyobb kiválasztása------------------------------------------
# szokoz=0
# i=0
# i2=0
# while i!=poz:
#     while kordinatak[i2]!=" ":
#         i2+=1
#     i2+=1
#     i+=1
# print(f"Kordinátái pedig:", end=" ")
# while kordinatak[i2]!=" ":
#     print(kordinatak[i2], end=",")
#     i2+=1
# #--------------------------------------------Kordináták kiírása---------------------------------
# print()
# print(alkalmak)
# print(kordinatak)

oldal=int(input())
szamok=[]
for i in range(1, oldal*oldal+1, 1):
    szamok.append(i)
#-----------------------Számok-----------------------------
import random
szammax=oldal*oldal
kordinatak=[]
betuk = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(0, len(betuk), 1):
    irany=random.randint(1, 4)
    szam=random.randint(1, szammax)
    db=0
    if szam>oldal and irany==1:
        szam-=oldal
    elif szam<(szammax-oldal+1) and irany==3:
        szam+=oldal
    elif (szam-1)%oldal!=0 and irany==2:
        szam-=1
    elif szam%oldal!=0 and irany==4:
        szam+=1
    kordinatak.append(szam)
    #-----------------------Első mozdulás----------------------
    while szam>oldal and (szam-1)%oldal!=0 and szam/oldal<=(oldal-1) and szam%oldal!=0:
        irany=random.randint(1, 4)
        if szam>oldal and irany==1:
            szam-=oldal
        elif szam<(szammax-oldal+1) and irany==3:
            szam+=oldal
        elif (szam-1)/oldal!=0 and irany==2:
            szam-=1
        elif szam%oldal!=0 and irany==4:
            szam+=1
        kordinatak.append(szam)
    kordinatak.append(" ")
print(kordinatak)
#-----------------Kordináták létrehozása-----------------
db=0
max=0
vonal=0
dbvonal=0
for i in range(0, len(kordinatak), 1):
    if kordinatak[i]!=" ":
        db+=1
    else:
        if db>max:
            max=db
            vonal=dbvonal
        dbvonal+=1
        db=0
#--------------Legnagyobb kiválasztása-------------------
print(max, betuk[vonal])