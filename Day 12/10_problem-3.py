# print multiplication table of a number entered by the user using list comprehension
number = int(input('Enter a number  :   '))
myList = [1,2,3,4,5,6,7,8,9,10]
multiplicationList = [number*i for i in myList]
print(multiplicationList)
