tizedikc=[
    ("Kis Pista", 2.7, "Testnevelés"), 
    ("Nagy Józsi", 3.1, "Matematika"),
    ("Közepes Julcsi", 4.7, "Programozás"),
    ("Átlagos Elemér", 3, "Lyukas óra")
]

for i in range(len(tizedikc)):
    print(f"{tizedikc[i][0]} ({tizedikc[i][1]}) - {tizedikc[i][2]}")

for emberek in tizedikc:
    print(f"{emberek[0]} ({emberek[1]}) - {emberek[2]}")

for i in range(len(tizedikc)):
    nev,atlag,tantargy=tizedikc[i]
    print(f"{nev} ({atlag}): {tantargy}")

for i in range(len(tizedikc)):
    nev,_,tantargy=tizedikc[i]
    print(f"{nev}: {tantargy}")

for nev,atlag,tantargy in tizedikc:
    print(f"{nev} ({atlag}): {tantargy}")


osszeg=0
for i in range(len(tizedikc)):
    _,atlag,_=tizedikc[i]
    osszeg+=atlag

print(osszeg/len(tizedikc))