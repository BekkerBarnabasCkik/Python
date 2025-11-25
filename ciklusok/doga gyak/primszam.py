import math
szam=abs(int(input()))
i=3
if szam==1:
    print("Nem prímszám")
else:
    if szam==2:
        print("Prímszám")
    else:
        if szam%2==0:
            print("Nem prímszám")
        else:
            while i<=szam/2 and szam%i!=0:
                i+=2
            if i<=round(math.sqrt(szam)):
                print("Nem prímszám")
            else:
                print("Prímszám")