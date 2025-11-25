nev1= "Szabó Emánuel"
nev2= "Minta Jakab"
szam=4
print(nev1, " matematika tanár szerint ",szam,"+",szam, "=", szam+szam, ", a ",nev2, " szerint ", szam, "+", szam, "=", szam, szam, ". Melyiküknek van igaza?", sep="" )
print(nev1 + " matematika tanár szerint " + str(szam) + "+" + str(szam) + "=" + str(szam+szam) + ", a " + nev2 + " szerint " + str(szam) + "+" + str(szam) + "=" + str(szam)+str(szam)+". Melyiküknek van igaza?")
# azért kellett str-t elé tenni mert számot meg szöveget nem lehet simán összefűzni, és a számot át kell alakítani szöveggé
print(f"{nev1} matematika tanár szerint {szam}+{szam}={szam+szam}, a {nev2} szerint {szam}+{szam}={szam}{szam}. Melyiküknek van igaza?")
print("{0} matematika tanár szerint {2}+{2}={3}, a {1} szerint {2}+{2}={2}{2}. Melyiküknek van igaza?".format(nev1, nev2, szam, szam+szam))