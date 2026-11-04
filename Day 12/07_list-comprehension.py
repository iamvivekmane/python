myList = [1,2,3,4,5]
squaredList = []
for i in myList:
    squaredList.append(i*i)
# we can perform same task using the list comprehension
squaredList2 = [i*i for i in myList]
print(squaredList2) 