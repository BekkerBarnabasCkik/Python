o1=float(input())
o2=float(input())
o3=float(input())
if o1+o2>o3 and o1+o3>o2 and o3+o2>o1:
    if ((round(o1**2)+round(o2**2)==round(o3**2) or round(o1**2)+round(o3**2)==round(o2**2) or round(o3**2)+round(o2**2)==round(o1**2)) and (o1==o2 or o1==o3 or o2==o3)):
        print("Derékszögű és egyenlőszárú")
    elif(round(o1**2)+round(o2**2)==round(o3**2) or round(o1**2)+round(o3**2)==round(o2**2) or round(o3**2)+round(o2**2)==round(o1**2)):
        print("Derékszögű")
    elif (o1==o2 and o2==o3):
        print("Szabályos háromszög")
    elif (o1==o2 or o1==o3 or o2==o3):
        print("Egyenlőszárú")
    else:
        print("Csak sima háromszög")
else:
    print("Nem háromszög")