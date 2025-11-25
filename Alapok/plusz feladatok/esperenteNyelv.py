# szöveg=input()
# eszperente="e".join(szöveg.split("a"))
# eszperente="e".join(szöveg.split("á"))
# eszperente="e".join(szöveg.split("o"))
# eszperente="e".join(szöveg.split("ó"))
# eszperente="e".join(szöveg.split("u"))
# eszperente="e".join(szöveg.split("ú"))
# eszperente="e".join(szöveg.split("ö"))
# eszperente="e".join(szöveg.split("ő"))
# eszperente="e".join(szöveg.split("ü"))
# eszperente="e".join(szöveg.split("ű"))
# eszperente="e".join(szöveg.split("é"))
# print(eszperente)

#------------------------------------------------- 1. próbálkozás----Nem sikerült----------------------------------------

# szöveg=input()
# eszperente=szöveg.translate(str.maketrans("aáéiíoóöőüűuú", "eeeeeeeeeeeee"))
# print(eszperente)

#------------------------------------------------- 2. próbálkozás-----Sikerült----------------------------------------------



# import re
# szöveg=input()
# eszperente=re.sub("[aáéiíoóuúöő]", "e", szöveg)
# print(eszperente)

#-------------------------------------3.próbálkozás------Sikerült----------------------------------------------------

szöveg=str(input())
szöveg = szöveg.replace("a", "e")
szöveg = szöveg.replace("á", "e")
szöveg = szöveg.replace("é", "e")
szöveg = szöveg.replace("o", "e")
szöveg = szöveg.replace("ó", "e")
szöveg = szöveg.replace("ö", "e")
szöveg = szöveg.replace("ő", "e")
szöveg = szöveg.replace("u", "e")
szöveg = szöveg.replace("ú", "e")
szöveg = szöveg.replace("ü", "e")
szöveg = szöveg.replace("ű", "e")
szöveg = szöveg.replace("i", "e")
szöveg = szöveg.replace("í", "e")
print(szöveg)