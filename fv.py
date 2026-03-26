def proba(n):
    eredetin=n
    if n!=4:
        for i in range(eredetin):
            print("", end="\t")
        print(f"mostani szint: {n}")
        proba(n+1)
        for i in range(eredetin):
            print("", end="\t")
        print(f"visszalépett szint: {eredetin}")
    else:
        for i in range(eredetin):
            print("", end="\t")
        print(f"Elértük a célt!")

proba(0)

def KristalyFeltores(n, pont, elozoDarab, eredetiN):
    pont=0
    if n!=0:
        if eredetiN-n!=0:
            pont+=elozoDarab*(eredetiN-n)*10
        else:
            pont+=n*10
        pont+=KristalyFeltores(n-1, 0, elozoDarab*2, eredetiN)
    else:
        return pont

print(KristalyFeltores(3, 0, 1, 3))

# 3.szint
# 3.szinten    3* 10 = 30TB
# 2.szinten 2* 2* 10 = 40TB
# 1.szinten 4* 1* 10 = 40 TB