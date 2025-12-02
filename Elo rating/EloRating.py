# #-----------------------Ea kiszámítása    1.1 Feladat------------------------------
# # szamok=str(input()).split(",")
# # ra=int(szamok[0])
# # rb=int(szamok[1])
# # ea=1/(1+pow(10, (rb-ra)/400))
# #print(ea)
# #-----------------------------1.2 Feladat-----------------------------------
# import random
# szam=random.randint(0, 9)
# if szam<9:
#     s=1
# else:
#     s=0
# # k=31
# # print(f"A bekövetkezik, új értéke: {round(ra+(k*(1-ea)), 2)}")
# # rUjNem=ra+(k*(0-ea))
# # if rUjNem>=0:
# #     print(f"A nem bekövetkezik új értéke: {round(rUjNem, 2)}")
# # else:
# #     print(f"A nem bekövetkezik új értéke: {0}")
# # print()
# #----------------------2.1 Feladat------------------------------------
# hossz=10
# t=[]
# t2=[]
# for i in range(hossz):
#     ertek=random.uniform(0, 1000)
#     t.append(round(ertek, 2))
#     t2.append(round(ertek, 2))
# #     print(f"{t[i]}_{i+1}")
# # print()
# #--------------------2.2 Feladat-----------------------------------
# # for i in range(hossz):
# #     print(f"{i+1}: {t[i]} pont")
# #--------------------3.Feladat--------------------------------------
# poz=[0,0,0,0,0,0,0,0,0]
# for i in range(len(t)-1, 0, -1):
#     szam=0
#     while szam!=i:
#         if t[i]<t[szam]:
#             t.insert(szam, t[i])
#             t.pop(i+1)
#         else:
#             szam+=1
# # print(t)
# # print(t2)
# poz=[]
# for i in range(0, len(t), 1):
#     j=0
#     while t[i]!=t2[j]:
#         j+=1
#     poz.append(j)
# # for i in range(0, len(t), 1):
# #    print(f"{poz[i]+1}: {t[i]} pont")
# #-------------------4. Feladat-------------------------------------
# # szam=int(input())
# # i=0
# # while szam!=poz[i]+1:
# #     i+=1
# #print(i)

# mecsekszama=int(input())
# hossz=10
# id=0
# for i in range(0, hossz, 1):
#     print(f"{poz[i]+1}: {t[i]} pont")
# for i in range(0, mecsekszama, 1):
#     id=random.randint(0,9)
#     ra=id
#     id=random.randint(0,9)
#     rb=id
