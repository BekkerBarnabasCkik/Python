szam=int(input())
jegyek=0
db=0
while szam>0 and szam<6:
    jegyek+=szam
    db+=1
    szam=int(input())
print(round(jegyek/db, 2))