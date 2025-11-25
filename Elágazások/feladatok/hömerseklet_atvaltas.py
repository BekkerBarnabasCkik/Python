import math
mertekegyseg=str(input())
szam1=float(input())

if mertekegyseg=="c":
    print(math.floor(((szam1*9)/5+32)*10)/10)
else:
    print(math.floor((((szam1-32)*5)/9)*10)/10)
