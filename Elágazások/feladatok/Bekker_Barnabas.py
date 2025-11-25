# 100 nap múlva

# két szám --> oszthatóe egymással

# hány fok van --> halmazállapot

# előjel fv

napok=["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]

mainap=input()
hanynapmulva=int(input())

x=napok.index(mainap)

if hanynapmulva%7==0:
    print(mainap)
else:
    y=(hanynapmulva%7)
    if x+y>=6:
        print(napok[(6-(x+y-1))*(-1)])
    else:
        print(napok[x+y])



szam=int(input())
szam2=int(input())
if szam2==0:
    print("Nem osztunk nullával.")
else: 
    print("Osztahtó egymással.")



fok=int(input())
if fok<=0:
    print("fagyos")
elif fok<100:
    print("folyékony")
else:
    print("gőz")



szam3=int(input())
if szam<0:
    print("negatív")
elif szam3==0:
    print("A szám 0 ")
else:
    print("A szám pozitív")