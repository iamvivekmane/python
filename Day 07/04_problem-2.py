# generate and store multiplication tables till 20 in 20 different text files
for i in range(2,21,1):
    file = open(f'file{i}.txt','w')
    for j in range(1,11,1):
        file.write(str(i) + 'X' + str(j) + '='+  str(i*j) + '\n')