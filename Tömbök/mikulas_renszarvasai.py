#Mikulás rénszaravasai 10db három tuléajd. hany km/s repül 100-1000, mennyi ideig repül? 10-100, mennyit pihen 1-10
#Kérdés: Amennyiben a mikuláés körbe szeretné utazni a Földet az egyenlítő mentén akkor melyik rénszarvast válassza hogy a lehető leggyorsabb legyen.

import random
renszarvasok=["Rudolf", "Üstökös", "Táncos", "Íjas", "Csillag", "Villám", "Felhő", "Mogyoró", "Zúzmara", "Havas"]
t=[]
for i in range(0, len(renszarvasok)*3, 3):
    t.append(random.randint(100, 1000))
    t.append(random.randint(10, 10))
    t.append(random.randint(1, 10)) 
idok=[]
for j in range(0, len(renszarvasok)*3, 3):
    i=0
    sebesseg=t[j]
    ido=t[j+1]
    pihenes=t[j+2]
    összmp=0
    össztav=0
    while össztav<40000:
        if össztav+(sebesseg*ido)<40000:
            össztav+=(sebesseg*ido)
            összmp+=ido
            összmp+=pihenes
        else:
            összmp+=(((40000-össztav)/sebesseg)*ido)
            össztav+=40000-össztav
    idok.append(összmp)
Leggyorsabb=idok[0]
poz=0
for i in range(1, len(idok), 1):
    if Leggyorsabb>idok[i]:
        Leggyorsabb=idok[i]
        poz=i
print(idok, t)
print(f"{renszarvasok[poz]} volt a leggyorsabb ugyanis vele {round(Leggyorsabb, 5)} másodperc körbekerülni a Földet.")