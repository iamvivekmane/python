# # single inheritence 
# class Employee:
#     name  = 'Default name'
#     company = 'TCS'
#     def getEmployeeInfo(self):
#         print('The name of employee is ',self.name,'The company of the employee is ',self.company)

# class Coder(Employee):
#     language = 'python'
#     experience = 4
#     def getCoderInfo(self):
#         print('The language of employee is ',self.language,'The experience of the employee is ',self.experience)

# john = Coder()
# john.getEmployeeInfo()
# john.getCoderInfo()



# multiple inheritence
# class Employee:
#     name  = 'Default name'
#     company = 'TCS'
#     def getEmployeeInfo(self):
#         print('The name of employee is ',self.name,'The company of the employee is ',self.company)

# class Company:
#     location ='Pune'
#     noOfEmployees= 1000
#     def getCompanyInfo(self):
#         print('The location of company is ',self.location,'The count of the employee is ',self.noOfEmployees)

# class Coder(Employee,Company):
#     language = 'python'
#     experience = 4
#     def getCoderInfo(self):
#         print('The language of employee is ',self.language,'The experience of the employee is ',self.experience)

# john = Coder()
# john.getEmployeeInfo()
# john.getCoderInfo()
# john.getCompanyInfo()



# multilevel inheritence
# class Employee:
#     name  = 'Default name'
#     company = 'TCS'
#     def getEmployeeInfo(self):
#         print('The name of employee is ',self.name,'The company of the employee is ',self.company)

# class Company(Employee):
#     location ='Pune'
#     noOfEmployees= 1000
#     def getCompanyInfo(self):
#         print('The name of the employee is',Employee.name,'The name of the company is ',Employee.company,'The location of company is ',self.location,'The count of the employee is ',self.noOfEmployees)

# class Coder(Company):
#     language = 'python'
#     experience = 4
#     def getCoderInfo(self):
#         print('The language of employee is ',self.language,'The experience of the employee is ',self.experience)
# john = Coder()
# john.getCoderInfo()
# john.getCompanyInfo()

# super keyword
# it is used to access the methods of the super class in the derieved class
class Employee:
    name  = 'Default name'
    company = 'TCS'
    def __init__(self,name,company):
        print('Constructor of employee')
        self.name = name
        self.company = company
    def getEmployeeInfo(self):
        print('The name of employee is',self.name,'The company of the employee is',self.company)

class Company(Employee):
    location ='Pune'
    noOfEmployees= 1000
    def __init__(self, name, company):
        print('Constructor of company')
        super().__init__(name, company)
    def getCompanyInfo(self):
        print('The name of the employee is',Employee.name,'The name of the company is ',Employee.company,'The location of company is ',self.location,'The count of the employee is ',self.noOfEmployees)

class Coder(Company):
    language = 'python'
    experience = 4
    def __init__(self, name, company):
        print('Constructor of coder')
        super().__init__(name, company)
    def getCoderInfo(self):
        print('The language of employee is',self.language,'The experience of the employee is',self.experience)


john = Coder('John','Google')
john.getEmployeeInfo()