# store the multiplication table created in the 3rd problem in a file named Tables.txt
number = int(input('Enter a number  :   '))
myList = [1,2,3,4,5,6,7,8,9,10]
multiplicationList = [number*i for i in myList]
print(multiplicationList)

file1 = open('Tables.txt','w')
file1.write(str(multiplicationList))