szoveg=str(input()).lower()
edb=0
mg=0
for i in range(0, len(szoveg), 1):
    if szoveg[i]=="a" or szoveg[i]=="á" or szoveg[i]=="e" or szoveg[i]=="é" or szoveg[i]=="o" or szoveg[i]=="ó" or szoveg[i]=="ö" or szoveg[i]=="ő" or szoveg[i]=="u" or szoveg[i]=="ú" or szoveg[i]=="ü" or szoveg[i]=="ű" or szoveg[i]=="i" or szoveg[i]=="í":
        mg+=1
        if szoveg[i]=="e" or szoveg[i]=="é":
            edb+=1
print(f"{round(edb/mg*100)}%")
