# #könyvelés hamisítás a törvénynek megfelően
# #-----------összegek-------------------
# import math
# import random
# # n=int(input())
# # t=[]
# # kiadasokszama=0
# # bevetekeszama=0
# # elojel=0
# # for i in range(0, n, 1):
# #     elojel=random.randint(1, 10)
# #     if elojel<=6:
# #         t.append(str(random.randint(-999999, -1)))
# #     else:
# #         t.append(str(random.randint(1, 999999)))
# # print(t)
# t = [
#     "1015", "8503", "9646", "5715", "4108", "1706", "9773", "9288", "7029", "5112",
#     "7979", "8431", "1362", "9987", "6629", "2399", "8529", "1918", "8941", "8803",
#     "5204", "1019", "2956", "1678", "1201", "4853", "6504", "7270", "9900", "2998",
#     "1646", "3873", "7125", "6784", "6469", "6463", "2313", "4324", "3246", "5559",
#     "1386", "6516", "2053", "7727", "7037", "5000", "3176", "1526", "1806", "3114",
#     "6182", "4780", "2933", "5887", "2256", "1590", "1135", "2249", "4470", "2138",
#     "3786", "3049", "2857", "5941", "5382", "2784", "1249", "4679", "2222", "1083",
#     "4362", "1880", "4477", "1158", "3934", "2448", "1231", "3355", "4161", "1849",
#     "1992", "4860", "3111", "3816", "3107", "3435", "1616", "2268", "2182", "1862",
#     "3433", "2760", "2848", "1820", "2449", "1699", "1080", "1014", "1053", "1065"
# ]




# #-----------------viszgálat------------------
# szazalekok=[30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
# szamok=[]
# alkalmak=[]
# for i in range(0, len(t), 1):
#     if int(t[i])>0:
#         elsoszam=int(t[i][0])
#     else:
#         elsoszam=int(t[i][1])
#     i=0
#     while i<len(szamok) and szamok[i]!=elsoszam:
#         i+=1
#     if i<len(szamok):
#         if i<len(alkalmak):
#             alkalmak[i]+=1

#     else:
#         szamok.append(elsoszam)
#         alkalmak.append(1)
# print(szamok, alkalmak)
# i=0
# while :
#     i+=1
# if i<len(szamok):
#     print(f"Nem felel meg!")
# else:
#     print(f"Megfelel!")

import random
hossz=1000
szazalekok=[30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
i=0
db=[0,0,0,0,0,0,0,0,0]
ertekek=[]
proba=1
for i in range(hossz):
    szam=random.randint(1, 9)
    while ((db[szam-1]+1)/hossz)*100>szazalekok[szam-1]+0.5:
        szam=random.randint(1, 9)
    proba+=1
    db[szam-1]+=1
    ertekek.append(szam*1000+random.randint(0, 999))
print(ertekek)
print(db)


