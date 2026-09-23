# tuple is same as list but the only change is that the tuples are immutable
from itertools import tee


a = (1,2,3,4)
print(type(a))

# it will be considered as an integer instead of a tuple with a single value in it
b = (1)
print(type(b))

# if we add comma after single element then it will be considered as a tuple with a single element
b = (1,)
print(type(a))

e = (1,22,2341,False,"jon",1,22,1)

# it returns the occurence of the passed value in the tuple
count = e.count(1)
print(count)

# it returns the first occurence index of the passed value in the tuple
index = e.index(1)
print(index)

# it returns the length of the tuple 
length = len(e)
print(length)

