# star pattern
n = 3
for i in range(n+3):
    if(i==2 or i ==4):
        continue
    for j in range(i):
        print("*",end="")
    if(i==0):
        continue
    print("")