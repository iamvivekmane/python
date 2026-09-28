# prime or not
number = int(input("Enter a number : "))
flag = True;
if number<=1:
    flag = False
for i in  range(2,number-1):
    if(number%i==0):
        flag = False
if flag:
    print("Yes")
else:
    print("No")