#Be: cm
#Ki: m dm cm
#Példa
# Be: 4567
# Ki: 45 m 6 dm 7 cm

cm=int(input())
print(f"{cm//100} m {(cm%100)//10 } dm {cm%10} cm") 
# print(f"{int(cm//91.44)} yard {int((cm%91.44)//30.48)} láb {int((cm%30.48)//2.54)} hüvelyk")

# angolsász mértékegység egész értékben
# 1 yard = 3 foot = 91,44 cm
# 1 foot = 12 inch = 30,48 cm
# 1 inch = 10 line = 2,54 cm
# /=rendes osztás 7/2=3.5 //=egész számos osztás 7//2=3 %=maradékos osztás 7%2=5
