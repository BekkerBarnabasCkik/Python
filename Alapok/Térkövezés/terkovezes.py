# oldal1=int(input())
# oldal2=int(input())
# terko=int(input())
# darab=0
# terulet=oldal1*oldal2
# terulet2=terko*terko
# darab=terulet/terulet2
# print(round(darab, 1))

import math
oldal1=int(input("Add mrg a téglalap hosszúságát: "))
oldal2=int(input("Add meg a téglalap szélességét: "))
oldal3=int(input("Add meg a térkő oldalhosszát: "))

hossz=math.ceil(oldal1/oldal3)
szelesseg=math.ceil(oldal2/oldal3)

print(hossz*szelesseg)