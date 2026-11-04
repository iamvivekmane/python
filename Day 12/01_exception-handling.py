# try except
try:
    number = int(input('Enter a number please   :   '))
    print('The number is ',number)
except Exception as e:
    print(e)


# raising exception explicitly
number1 = int(input("Enter first number     :"))
number2 = int(input("Enter second number    :"))
if(number2==0):
# this is the explicit exception that we can raise
    raise ZeroDivisionError('Cannot divide by zero')
print('The division is ',number1/number2)


# else with try
try:
    number = int(input('Enter a number please   :   '))
    print('The number is ',number)
except Exception as e:
    print(e)
else:
# when the try block runs successfully then the execution enters the else block
# it shows that the exection of try block is successul without any exception
    print('Inside the else block')