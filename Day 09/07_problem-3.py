# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators
# ‘+’ and ‘*’ which adds and multiplies them
class complex:
    real = 1
    imag = 4
    e = 0
    def __init__(self,a,b):
        self.real = a
        self.imag = b         
    def getData(self):
        print(self.real , self.imag)
    def __add__(self, other):
        return complex(self.real + other.real , self.imag + other.imag)
    def __mul__(self, other):
        return complex(self.real * other.real , self.imag * other.imag)
    def __str__(self):
        return f"{self.real} + {self.imag}i"
    

c = complex(8,1)

d = complex(4,7)

print(c+d)
print(c*d)