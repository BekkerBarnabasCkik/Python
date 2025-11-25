#Genetálj egy n hosszúságú tömböt ahol tároljuk a szövetségesek napo tank veszteségüket 0-100 között
#Kérdések:
#Összesen mennyi tankot vesztettek?
#Átlagosan?
#Hány olyan nap volt mikor nem vezstettek tankot?
#Melyik volt az első olyan nap (ha volt) mikor 50-nél több tankot veszetettek?
#Melyik nap vesztették a legtöbbet ha első nap hétfő volt?
import random
t=[]
szam=int(input())
for i in range(0, szam, 1):
    t.append(random.randint(0, 100))
#---------Lista feltöltés-------------
osszes=0
for i in range(0, len(t), 1):
    osszes+=t[i]
print(f"Összesen {osszes} tankot vezstettek.")
#------------Összesen--------------
print(f"Átlagosan pedig napi {osszes/szam} tankot vesztettek")
#---------Átlag számítás--------------
db=0
for i in range(0, len(t), 1):
    if t[i]==0:
        db+=1
#--------------DB szám-------------------
i=0
while i<len(t) and t[i]<=50:
    i+=1
if i<len(t):
    print(f"{i}. napon vesztettek több mint 50 tankot")
else:
    print(f"Egyik nap se vesztettek több tankot mint 50")
#----------------------------Több mint 50-------------------------
legnagyobb=t[0]
poz=0
napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]

for i in range(1, len(t), 1):
    if legnagyobb<t[i]:
        legnagyobb=t[i]
        poz=i
#------------------------Napok---------------------------------------
print(f"Összesen {db} nap nem vesztettek tankot")
print(f"Amikor a legtöbb tankot vesztették el akkor {napok[poz-poz//7*7]} volt")

print(t)