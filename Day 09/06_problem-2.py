# Create a class ‘Employee’ and add salary and increment properties to it. Write a method
# ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes
# the value of increment based on the salary
class employee:
    name = 'default'
    salary = 10000
    increment = 9
    @property
    def salaryAfterIncreament(self):
         return self.salary * (1 + self.increment / 100)


harry = employee()
print('The salary is ',harry.salary)
print('The increment percentage is ',(harry.increment))
print('The salary after increment is ',f"{harry.salaryAfterIncreament:.0f}")
