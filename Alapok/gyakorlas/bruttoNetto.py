import random
also=int(input())
felso=int(input())
brutto=(random.randrange(also, felso)//1000)*1000

print(f"A brutto bér:{brutto}Ft")
print(f"A nettó bér:{round(brutto*0.665)}Ft")
print(f"Munkaeró-piaci járuléj (1,5%):{round(brutto*0.015)} Ft")
print(f"Egészségbiztosítási járulék (7%):{round(brutto*0.07)} Ft")
print(f"Nyugdíjjárulék (10%):{round(brutto*0.1)} Ft")
print(f"Személyi jövedelemadó (15%):{round(brutto*0.15)} Ft")