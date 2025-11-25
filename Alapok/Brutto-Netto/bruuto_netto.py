import random

n=int(input())
m=int(input())
brutto=random.uniform(n, m)
brutto=brutto//1000
brutto=round(brutto*1000)
netto=brutto-(round(brutto*0.335))
print(f"A brutto bér: {brutto} Ft")
print(f"A nettó bér: {netto} Ft")
print(f"Munkaeró-piaci járuléj (1,5%): {round(brutto*0.15)} Ft")
print(f"Egészségbiztosítási járulék (7%): {round(brutto*0.07)} Ft")
print(f"Nyugdíjjárulék (10%): {round(brutto*0.1)} Ft")
print(f"Személyi jövedelemadó (15%): {round(brutto*0.15)} Ft")
