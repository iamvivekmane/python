from functools import reduce
a = [1,2,3,4,5]

print('List     :   ',a)
square = lambda x:x*x

# map
# it applies the passed function on every element of the list
newList1 = map(square,a)
print('Squares  :   ',list(newList1))

# filter
# it filter outs the element based on the condition in the function
def even(n):
        if(n%2==0):
            return n
newList2 = filter(even,a)
print('Even     :   ',list(newList2))

# reduce
# it returns one value after doing operations on the each element of the list
sum = lambda a,b: a+b
newList3 = reduce(sum,a)
print('Sum      :   ',int(newList3))