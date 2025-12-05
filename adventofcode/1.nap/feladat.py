f=open("proba.txt")
t=f.readlines()
f.close()
s="alma"
# print(s[1:])
hely=50
irany=0
db=0
for i in t:
    i=i.strip()
    ertek=(i)
    szam=int(ertek[1:])
    if ertek[0]=="R":
        irany=-1
    else:
        irany=1
    hely+=(irany*szam)-((hely+(irany*szam))//100*100)
    if hely==0:
        db+=1
print(db)
