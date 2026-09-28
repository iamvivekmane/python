# sum of first n natural numbers using recursion
number = int(input("Enter a number : "))
def sum(n):
    if(n == 1):
        return 1
    elif(n==0):
        return 0
    return n + sum(n-1)
print(sum(number))