# to print numbers till 5 we can do 
print(1)
print(2)
print(3)
print(4)
print(5)

# same can be done using loops
# for loop
for i in range(1,6):
    print(i)

# same output
# while loop
i = 1
while(i<=6):
    print(i)
    i+=1

# third argument passed is the step size 
# it will jump the amount of steps specified at the third argument in the range function
for i in range(0,10,2):
    print(i)