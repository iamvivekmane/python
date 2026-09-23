friends = ["apple","akash",False,9,9.212,"orange"]
print(friends)

# lists are mutable
friends[0] = "banana"

# when we run this function it changes the existing list rather than returning a new list
friends.append("pineapple")
print(friends)

l1 = [100,12,1,723,9,23]
print(l1)

# sort list in ascending order
l1.sort()

# sort list in descending order
l1.reverse()

# insert a new element at the specific index
l1.insert(3,213)

# delete element at the specific index and return its value
l1.pop(2)

# delete the specific value from the list
l1.remove(1)

print(l1)