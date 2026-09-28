# star pattern
n = 3
for i in range(n+1):
    for j in range(i):
        print("*",end="")
    if(i==0):
        continue
    print("")