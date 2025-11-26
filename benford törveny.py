#könyvelés hamisítás a törvénynek megfelően
#-----------összegek-------------------
import math
import random
# n=int(input())
# t=[]
# kiadasokszama=0
# bevetekeszama=0
# elojel=0
# for i in range(0, n, 1):
#     elojel=random.randint(1, 10)
#     if elojel<=6:
#         t.append(str(random.randint(-999999, -1)))
#     else:
#         t.append(str(random.randint(1, 999999)))
# print(t)
t=["123", "5872", "194", "3014", "145", "94532", "2346",
    "1872", "113",
 "429", "15893", "275", "1987", "10345", "7521", "641",
 "17823", "217", "3679", "51235", "1424", "289", "19876",
 "304", "134", "75433", "2679", "183", "4232", "101235"]


#-----------------viszgálat------------------
szazalekok=[30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
szamok=[]
alkalmak=[]
for i in range(0, len(t), 1):
    if int(t[i])>0:
        elsoszam=int(t[i][0])
    else:
        elsoszam=int(t[i][1])
    i=0
    while i<len(szamok) and szamok[i]!=elsoszam:
        i+=1
    if i<len(szamok):
        if i<len(alkalmak):
            alkalmak[i]+=1

    else:
        szamok.append(elsoszam)
        alkalmak.append(1)
print(szamok, alkalmak)
i=0
while alkalmak[i]>szazalekok[szamok[i]-1]-0.5 and szamok[i]<szazalekok[szamok[i]-1]+0.5 and i<len(szamok):
    i+=1
if i<len(szamok):
    print(f"Nem felel meg!")
else:
    print(f"Megfelel!")