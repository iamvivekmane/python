class number:
    def __init__(self,n):
        self.n = n
    def __add__(self, other):
        return self.n + other.n

a = number(10)
b = number(20)
# without operator overloading it will throw an error becuase in python everything is a class & to use these operators with the classes we need to use operator overloading
c = a + b
print(c)