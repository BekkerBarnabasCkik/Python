f=open("proba.txt")
t=f.readlines()
f.close()
s="alma"
# print(s[1:])
hely=50
irany=0
for i in t:
    i=i.strip()
    ertek=(i)
    szam=int(ertek[1:])
    if ertek[0]=="R":
        irany=-1
    else:
        irany=1
    hely+=irany*szam
print(hely)
    
# print(tjo)
# for i in range(len(tjo)):
#     ertek=t[i[2:]]
#     print(ertek)
