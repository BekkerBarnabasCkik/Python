# Feladat:
# TUDJUK, HOGY A TÖMBEN VAN T tulajdonságú elme, és meg akarjuk határozni az első ilyen elem helyét
#Ezt úgy tesszük, hogy elindulunk a tömb elejétől és amíg nem találunk T tulajdonságú elemet, addig haladunk és ha találtunk akkor megállunk.
# Példa: t=[6, 10, 1, 3, 8, 9] n=6 T=prím Ki=prím
# Algoritmus
# Program kewzdete
#     be: t,n,T
#     i=0
#     ciklus amíg nem(T(t[i]))
#         i=i+1
#     Ciklus vége
#     Ki:i
# Program vége


#TIPYNGMASTER gépírás gyakorlás

#Példa: Mikor jöttünk ki elösször! (Feltéve, hogy a teljes játék kockadobása adott)
#Be szam, hossz
import random
szam=int(input())
t=[]
osszeg=0
for i in range(0, szam, 1):
    t.append(random.randint(1, 6))
print(t)
i=0
while t[i]!=6:
    i+=1
print(i)