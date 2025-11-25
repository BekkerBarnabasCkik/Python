#Feladata: összegzi a tömb elemeit úgy, hogy egy változó :=0 
#Majd végig megyünk a tömb elemein és rendre hozzáadjuk a tömb értékeét maivel növeljük a változót és a végén kiírjuk
#Példa: Be: t=[1, 5, 6, 1] n=4 Ki: 13

#Algoritmus:
# Program kezdete
#     Be: t, n
#     osszeg=0
#     Ciklus i=0-tól i<n-ig egyesével
#         osszeg=osszeg+t[i]
#     Ciklus vége
#     Ki: osszeg
# Program vége
# Működési táblázat
# i	t[i]=[1,5,6,1]	osszeg=0
# 0 1	 1
# 1 5	 6
# 2 6	 12
# 3 1	 Ki:(13)
# 4		
