# check if a student is pass or fail
marks  = []
total = 0
for i in range(3):
    m =  int(input("Enter marks : "))
    marks.append(m)
    total = total+m

print(total)
percentage = total /3
print(percentage)
result = False
for i in range(3):
    if(percentage>=40 and marks[i]>=33):
        result = True
    else:
        result= False
        break

if(result):
    print("passed")
else:
    print("failed")