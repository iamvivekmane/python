a = 10
def func():
# when we use global keyword it refers to the variable that we crated at the module level
    global a 
    a = 12
    print(a)

func()
print(a)