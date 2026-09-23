# accept marks of 6 students and sort them in ascending order
marks  = []

for i in range(6):
    temp = int(input("Enter marks : "))
    marks.append(temp)

marks.sort()
print(marks)