#Be: m1 dm1 cm1 m2 dm2 cm2
#Ki: összeg
#Példa: 1 9 9 2 2 2 = 4 2 1

m1=int(input("m "))
dm1=int(input("dm "))
cm1=int(input("cm "))
m2=int(input("m "))
dm2=int(input("dm "))
cm2=int(input("cm "))
osszeg=m1*100 + dm1*10 + cm1 + m2*100 + dm2*10 +cm2
print(f"{osszeg//100}m {(osszeg%100)//10}dm {osszeg%10}cm")