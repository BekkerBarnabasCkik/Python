# nev=input()  #B e k k e r   B a r n a b á s
#              #0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
# elso=nev[0]
# utolso=nev[len(nev)-1]
# szokoz=nev.find(" ")
# print(f"{elso}.{nev[szokoz+1]}")

# nev=input()
# elso=nev[0]
# masodik=nev.find(" ")
# harmadik=nev.find(" ", masodik+1)
# negyedik=nev.find(" ", harmadik+1)
# ötödik=nev.find(" ", negyedik+1)
# print(f"{elso}.{nev[masodik+1]}.{nev[harmadik+1]}.{nev[negyedik+1]}.{nev[ötödik+1]}")

nev=input()
darab=nev.split(" ")
print(darab)
print(f"{darab[0][0]} {darab[1][0]} {darab[2][0]} {darab[3][0]}")