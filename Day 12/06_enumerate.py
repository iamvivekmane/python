l = [1,22,432,1123]
index = 0
for item in l:
    print('Item at the index',index,'is ',item)
    index +=1

# the above code can be simplified using enumerate function
for index,item in enumerate(l):
    print('Item at the index',index,'is ',item)

