import random

def randomMI():
    MIk=["gemini", "chatGPT", "deepSpeek", "copilot"]
    szam=random.randint(0, 999)
    nullak=0
    if len(str(szam))!=3:
        nullak+=3-(len(str(szam)))
    for i in range(len(str(szam))):
        if str(szam)[i]=="0":
            nullak+=1
    
    return MIk[nullak].upper(), szam, nullak

elem, szam, nullak=randomMI()
print(f"GEnerált száma: {szam}, nullak száma {nullak}, a legjobb MI: {elem.lower()}")

hossz=int(input())
while hossz<2:
    hossz=int(input())

def fibonacci(hossz):
    elemek=[0, 1]
    for i in range(hossz-2):
        elemek.append(elemek[i-1]+elemek[i-2])

    return elemek
#2/b
# def Eldont(tomb, hossz):
