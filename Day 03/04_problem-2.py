# print unique elements entered by the user
numbers = set()

for i in range(8):
    inp = int(input("Enter number : "))
    numbers.add(inp)

print("Unique elements are : ",numbers)