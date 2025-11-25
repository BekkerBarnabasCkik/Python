# 60 perc van
# 1perc=6fok
# 1 óra között hány perc vonalka van? 5
# 1 óra 30 fok
# Nagy mutató
# 3 óra 20 perc
# 3 óra alatt a kis mutató 90 fokot tesz meg
# 20 perc alatt még plusz 10 fokot tesz meg --> 100 fok
# 20 perc alatt a nagymutató hány fokot tesz meg? 120
# 120-100=20 fok

ido=input()
perc=int(ido[3]+ido[4])
ora=int(abs(ido[0]+ido[1]-12))
orafok=ora*30+(perc/60*30)
percfok=perc*6
print(abs(percfok-orafok))

#Délutánra is legyen jó