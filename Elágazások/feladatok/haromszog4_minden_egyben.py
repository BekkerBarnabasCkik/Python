import math
o1=float(input("Első oldal hossza (cm): "))
o2=float(input("Második oldal hossza (cm): "))
o3=float(input("Harmadik oldal hossza (cm): "))

if o1+o2>o3 and o1+o3>o2 and o2+o3>o1:
    if (round(o1*o1)+round(o2*o2)==round(o3*o3) or round(o1*o1)+round(o3*o3)==round(o2*o2) or round(o2*o2)+round(o3*o3)==round(o1*o1)) and (o1==o2 or o1==o3 or o2==o3):
        # x=o1*o1+o2*o2
        # y=o3*o3
        # print(x, y)
        print("Derékszögű és egyenlőszárú")
    elif o1==o2 or o1==o3 or o2==o3:
        print("Egyenlőszárú")
    elif o1*o1+o2*o2==o3*o3 or o1*o1+o3*o3==o2*o2 or o2*o2+o3*o3==o1*o1:
        print("Derékszögű")
    else:
        print("Csak szerkezthető")
else:
    print("Nem szerkezthető")

halft=(o1+o2+o3)/2
t=math.sqrt(halft*(halft-o1)*(halft-o2)*(halft-o3))

ker=o1+o2+o3

kör=(o1*o2*o3)/(4*t)

belsökör=(2*t)/(o1+o2+o3)

print("Területe: ", round(t, 3), "cm2")
print("Kerülete: ", round(ker, 3), "cm") 
print("Köré írható körnének sugara: ", round(kör, 3), "cm")
print("Beírt körének sugara: ", round(belsökör, 3), "cm")