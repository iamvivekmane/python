# property decorator is used to define a method that is behaves like an attribute
class base:
    name = 'random'
    @property
    def name(self):
        return f'{self.fname},{self.lname}'
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
    
test = base()
test.name = "Alaistar cook"
print('The first name is',test.fname,'The last name is',test.lname)
