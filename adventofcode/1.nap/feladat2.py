f=open("be2.txt")
t=f.readlines()
f.close()

hely=50
irany=0
db=0
for i in t:
    i=i.strip()
    ertek=(i)
    szam=int(ertek[1:])
    if ertek[0]=="L":
        irany=-1
    else:
        irany=1
    db+=szam//100
    szam%=100
    if hely!=0:
        hely=hely+irany*szam
        if hely==0:
            db+=1
        elif hely>=100:
            db+=1
            hely-=100
        elif hely<0:
            db+=1
            hely+=100
    else:
        hely=hely+irany*szam
        if hely<0:
            hely+=100
print(db)

