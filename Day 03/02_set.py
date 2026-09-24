# it will be considered as an empty dictionary not a set
a = {}
print(type(a))

# syntax to create an empty set
b = set()
print(type(b))

c = {1,2,3,4,2,1,11}
# output : 1,2,3,4,11 because it will ignore all the repeated values
print(c)

# it will add a passed value in the set
c.add(10)

# it will return the length of the set
print(len(c))

# it will remove the passed value from the set
c.remove(1)

# it will remove arbitary (random) element from the set
c.pop()

# it will make the set empty by removing all the elements from it
c.clear()
 
a1 = {1,2,4,12,28}
a2 = {1,4,56,121}

# it will return all the values from both sets
print(a1.union(a2))

# it will return common values from both sets
print(a1.intersection(a2))

# it will return the values that are present in first but not in the second
print(a1.difference(a2))
