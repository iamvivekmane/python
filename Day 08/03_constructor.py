class employee:
    language = 'cpp'
    salary = 120000
    # constructor
    # it gets automatically called when the object is being created
    # also called as dunder method which gets automatically called
    def __init__(self,name,salary,language):
        print('An object is being created')
        self.name = name
        self.salary = salary
        self.language = language
    def getInfo(self):
        print('The name is',self.name,'The language is',self.language,'the salary is',self.salary)
    # there is no need to pass object to a static method
    @staticmethod
    def greet():
        print('Welcome')


sin = employee('sin','python',890000)
employee.getInfo(sin)