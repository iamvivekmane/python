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


# for loop with else
# when the execution of for loop completes it executes the code inside the else statement
for i in range(4):
    print(i)
else:
    print('done')

# break
# as its name suggests it exits the execution of the loop when encountered an break statement
for i in range(0,10):
    print(i)
    if(i==3):
        break

# continue
# as its name suggests it skips the current iteration in the loop and executes from the next iteration as it is
for i in range(1,10):
    if i==2:
        continue
    print(i)


# pass
# it is a null statement which is used to do nothing in the code, it is mostly used to use to indicate to write that piece of code later, it is like a placeholder
for i in range(1,10):
    pass
