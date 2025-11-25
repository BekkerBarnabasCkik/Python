# Feladata:
# Meghatározza az első legnmagyobb elem helyét.
# Meghatározás: Az első elemet megjelöljük legnagyobbnak majd a rákövetkező elemet megjelöljük a tömbön és megnézzük,
# hogy az aktuális elem nagyobb e mint a megjelölt elem és ha igen akkor megjelöljük legnagyobbnak.
# Példa: t[1, 3, 2, 6, 8, 5] n=6 Ki: 4
t=[1,3,2,6,8,5]
legnagyobb=t[0]
for i in range(1, len(t), 1):
    if t[i]>legnagyobb:
        legnagyobb=i
print(legnagyobb-1)
# Eljárás kezdete
# Be: (t, legnagyobb, n)
# Ciklus kezdete
# Ciklus i=1-től i<n-ig egyesével
#     Elágazás kezdete
#     Ha t[i] művelet legnagyobb:
#         legnagyobb:=i
#     Elágazás vége
# Ciklus vége
# Ki:legnagyobb
# Eljárás vége

