import random
szam=int(input())
dobas=0
hatos=0
for i in range(szam):
    dobas=random.randint(1, 6)
    if dobas==6:
        hatos+=1
    print(dobas, end=" ")
print()
print(hatos)