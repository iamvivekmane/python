# find the maximum number in a list using reduce
from functools import reduce 
a = [1,2,4,5,6234,9909999,100,210]

def max(a,b):
    if(a>b):
        return a
    else:
        return b



c = reduce(max,a)

print((c))