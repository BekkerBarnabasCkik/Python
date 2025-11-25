ev1=int(input("Melyik évben születtél? "))
honap1=int(input("Melyik hónapban születtél? "))
nap1=int(input("Hányadikán születtél? "))
ev2=int(input("Milyet évet írunk most? "))
honap2=int(input("Milyet hónapot írunk most? "))
nap2=int(input("Hányadika van ma? "))
evek=ev2-ev1
honapok=0
napok=0

if honap2-honap1>=0:
    honapok=honap2-honap1
else:
    evek=evek-1
    honapok=12-((honap2-honap1)*(-1))

if nap2-nap1>=0:
    napok=nap2-nap1
else:
    honapok-=1
    napok=30-((nap2-nap1)*(-1))

print(evek)
print(honapok)
print(napok)
print(f"Születésünk óta eltelt napok szaáma: {evek*365+honapok*30+napok}")