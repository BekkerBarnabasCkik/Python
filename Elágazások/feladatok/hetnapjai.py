nap=int(input())
napmulva=int(input())
x=(nap+napmulva-1)%7
if x==1:
    print("Hétfő")
elif x==2:
    print("Kedd")
elif x==3:
    print("Szerda")
elif x==4:
    print("Csütörtök")
elif x==5:
    print("Péntek")
elif x==6:
    print("Szombat")
else:
    print("Vasárnap")