# if else statement
number = int(input("Enter any number : "))
if(number>=0):
    print("The number is positive")
else:
    print("The number is negative")

age = int(input("Enter your age : "))

if(age>18):
    print("You are able to drive")
elif(age==0):
    print("You are just born")
elif(age<0):
    print("Age can't be negative")
else:
    print("You are not able to drive")