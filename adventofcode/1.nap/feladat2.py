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
    # if hely+(irany*szam)<=0 or hely+(irany*szam)>=100:
        
    # atlepes+=abs(hely+irany*szam)//100
    db+=szam//100
    szam%=100
    #Az utolsónál (14+82==96) nme teljesül a 100-as feltétel
    # if hely<0+(abs(hely+szam)-abs(hely+szam)//100*100) and irany==-1 and hely+szam<100 and hely+(irany*szam)>-100 and atlepes==0 and hely!=0:
    #     while szam>=100:
    #         szam-=100
    #         atlepes+=1
    #     atlepes+=1
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

