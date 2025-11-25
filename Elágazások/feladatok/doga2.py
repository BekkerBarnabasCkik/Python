import random
szam=random.randrange(0, 10)
radio=""
if szam==0 or szam==1:
    radio="Retro"
elif szam==2 or szam==3:
    radio="Petőfi"
elif szam==4 or szam==5:
    radio="Cegléd"
elif szam==6 or szam==7:
    radio="Rádió 1"
else:
    radio="BArtók"
print(f"A generált szám: {szam}. A hallgatott rádió: {radio}")

szam=int(input())
if szam<20 or szam>20000:
    print("Az emebri fül számára nem hallható")
else:
    print("Az meberi fül számára hallható")

szam=int(input())
e=abs(szam-2014)
if e%5==0 and e%4==0:
    print("Mindkettő")
elif e%5==0:
    print("Kistérségi")
elif e%4==0:
    print("Országgyűlési")
else:
    print("Egyik sem")