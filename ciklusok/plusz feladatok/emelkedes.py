import random
import math
szam=int(input())
ujszam=0
emelkedes=0
for i in range(szam):
    vszam=random.randrange(0, 100)
    if vszam<60:
        velszam=random.randrange(ujszam, ujszam+100)
    else:
        velszam=random.randrange(ujszam-100, ujszam)
    if ujszam<velszam:
        print("folyamatos") 
    print(f"Emelkedési mérték: {velszam-ujszam}")
    emelkedes+=velszam-ujszam
    ujszam=velszam 
    print(ujszam)
print(f"Átlagos emelkedés: {emelkedes/szam}")
