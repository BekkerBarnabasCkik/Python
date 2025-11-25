import random
alsohatar=int(input())
felsohatar=int(input())
szam=random.randrange(alsohatar, felsohatar+1)
print(szam)

szoveg=str(input())
print(szoveg[szam-1].upper())