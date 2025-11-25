# mainap=input()
# hanynapmulva=int(input())
# napok=["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]
# x=napok.index(mainap)
# y=0
# z=0
# if hanynapmulva%7==0:
#     print(mainap)
# else:
#     y=hanynapmulva%7
#     if x+y>=len(napok):
#         z=(len(napok)-(x+y))*(-1)
#         print(napok[z])
#     else:
#         print(napok[x+y])

mainap=int(input("Hanyadik nap van a héten? "))-1
napok=["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap", "Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]
hanynapmulva=int(input("Hány nap múlva?" ))
print(napok[(mainap+hanynapmulva)%7])