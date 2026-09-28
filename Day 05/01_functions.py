# a = int(input("Enter a number : "))
# b = int(input("Enter a number : "))
# c = int(input("Enter a number : "))
# average = (a+b+c)/3
# print("Average is : ",average)
# # if we want to calculate the average multiple times than writing the above piece of code repeatedly is not a good practice thats why functions are used.

# # functions wrap up a piece of code to perform a specific action
# # code written inside indentation is a part of the function

# # function definition
# def average():
#     a = int(input("Enter a number : "))
#     b = int(input("Enter a number : "))
#     c = int(input("Enter a number : "))
#     average = (a+b+c)/3
#     print("Average is : ",average)

# function call
# average()

# function without arguments
def hello():
    print("hello")
hello()

# function with arguments
def greet(name):
    print("Hello",name)
greet("Raj")

# function with default arguments(if we dont pass args then the default ones are used)
def add(a=10,b=20):
    print("Addition is",a+b)
add()
add(20,70)