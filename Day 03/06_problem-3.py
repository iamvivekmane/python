# find greatest of four number
numbers = []
for i in range(4):
    num = input("Enter a number : ")
    numbers.append(num)

greater = numbers[0]
print(greater)

for i in range(4):
    if(numbers[i]>greater):
        greater = numbers[i]

print("The greatest number is ",greater)