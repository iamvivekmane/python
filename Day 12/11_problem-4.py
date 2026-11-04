# print infinite if user enter 0 as the second number otherwise print the division
try:
    number1 = int(input("Enter first number     :"))
    number2 = int(input("Enter second number    :"))
    result = number1/number2
    print('The division is ',result)
except:
    print('Infinite')
