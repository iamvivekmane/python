# Write a class “Calculator” capable of finding square, cube and square root of a number
import math
class calculator:
    number = 0
    def __init__(self,number):
        self.number = number
    @staticmethod
    def greet():
        print('Hello user!')
    def square(self):
        self.greet()
        print('Square       : ',self.number*self.number)
    def cube(self):
        print('Cube         : ',self.number*self.number*self.number)
    def squareRoot(self):
        print('Square root  : ',int(math.sqrt(self.number)))
number = int(input('Enter a number  :   '))
test = calculator(number)
test.square()
test.cube()
test.squareRoot()