class employee:
    language = 'cpp'
    salary = 120000
    def getInfo(self):
        print('The language is',self.language,'the salary is',self.salary)
    # there is no need to pass object to a static method
    @staticmethod
    def greet():
        print('Welcome')


sin = employee()
sin.language = 'python'
sin.salary = 560000
employee.getInfo(sin)
employee.greet()