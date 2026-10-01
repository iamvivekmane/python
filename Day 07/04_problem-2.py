for i in range(2,20,1):
    for j in range(1,10,1):
        file = open(f'file{i}.txt','w')
        file.write(str(i) + 'X' + str(j) + '='+  str(i*j))