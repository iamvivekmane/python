# star pattern
n = 3
for i in range(n):
    for j in range(3):
        if(i==1 and j==2):
            continue
        print("*",end="")
    print("")