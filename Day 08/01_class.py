# class
class employee:
    language = 'cpp' # this is class attribute
    salary = 120000
    def getInfo(self):
        print('The language is',self.language,'the salary is',self.salary)

# object
john = employee() # this is instance attribute
john.name = 'john'
print(john.language)
print(john.salary)
print(john.name)

john.salary =20000
# output: 20000
# because the instance attribute take preference over class attributes during assignment and retrieval
print(john.salary)

employee.getInfo(john)