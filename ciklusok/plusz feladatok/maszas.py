import random
szam=0
legnagyobb=0
legkisebb=0
szint=0
i=0
<<<<<<< HEAD
alkalom=list()
for i in range(10):
=======
legtobb=0
legin=0
alkalom=[1]
for i in range(1000):
>>>>>>> c5ee70c9ea2d766f473738eb926a072ae924edb0
    szam=random.randint(0, 1)
    if szam==1:
        szint+=1
        if legnagyobb<szint:
            legnagyobb=szint
<<<<<<< HEAD
=======
            alkalom.append(0)
>>>>>>> c5ee70c9ea2d766f473738eb926a072ae924edb0
    else:
        szint-=1
        if legkisebb>szint:
            legkisebb=szint
<<<<<<< HEAD
    alkalom[szint]+=1
# for i in range(len(alkalom), len(alkalom)*(-1), -1):




    
=======
            alkalom.insert(0, 0)
    i=szint-legkisebb
    alkalom[i]+=1
    print(szint)
for i in range(0, len(alkalom), 1):
    if alkalom[i]>legtobb:
        legin=i
        legtobb=alkalom[legin]
print(legtobb, legin)


# import random

# # Kezdőállapot
# szint = 0
# legtobb = 0
# legin = 0

# # Lista: minden elem egy szinthez tartozik, a 0. indexhez tartozik az eltolás
# alkalom = [1]  # induláskor a 0. szinten vagyunk egyszer
# eltolas = 0    # eltolás a negatív szintek miatt

# # Véletlenszerű lépések
# for _ in range(100):  # 100 lépés példaként
#     szam = random.randint(0, 1)
    
#     if szam == 1:
#         szint += 1
#         # Ha új magasabb szint, bővítjük a listát jobbra
#         if szint + eltolas >= len(alkalom):
#             alkalom.append(0)
#     else:
#         szint -= 1
#         # Ha új negatív szint, bővítjük a listát balra és növeljük az eltolást
#         if szint + eltolas < 0:
#             alkalom.insert(0, 0)
#             eltolas += 1

#     # Index kiszámítása a listához
#     index = szint + eltolas
#     alkalom[index] += 1

# # Megkeressük a legtöbbet járt szintet
# legtobb = alkalom[0]
# legin = 0
# for i in range(1, len(alkalom)):
#     if alkalom[i] > legtobb:
#         legtobb = alkalom[i]
#         legin = i

# # Visszaszámoljuk a valós szintet
# hely = legin - eltolas

# print("A legtöbbet járt szint:", hely)
# print("Ennyiszer volt ott:", legtobb)

# # Ha szeretnéd, kiírhatod az összes szint előfordulását is
# for i in range(len(alkalom)):
#     sz = i - eltolas
#     print(f"Szint {sz}: {alkalom[i]} alkalom")
>>>>>>> c5ee70c9ea2d766f473738eb926a072ae924edb0
