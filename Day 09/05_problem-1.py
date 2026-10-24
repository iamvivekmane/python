#  Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’.
# Add a method ‘bark’ to class ‘Dog’.

class animals:
    name = 'default name'
    age = 10
    def __init__(self,name,age):
        print('Constructor of animals class')
        self.name = name
        self.age = age
class pets(animals):
    owner = 'default name'
    adoption = True
    def __init__(self,name,age,owner,adoption):
        print('Constructor of pets class')
        self.owner = owner
        self.adoption = adoption
        super().__init__(name,age)
class dog(pets):
    breed = 'default breed'
    color = 'black'
    def __init__(self,name,age,owner,adoption,breed,color):
        self.breed = breed
        self.color = color
        super().__init__(name,age,owner,adoption)
    def bark():
        print('The dog is barking')
    def showData(self):
        print('The name is ',self.name)
        print('The age is ',self.age)
        print('The owner is ',self.owner)
        print('The adoption is ',self.adoption)
        print('The breed is ',self.breed)
        print('The color is ',self.color)

tom = dog('tom',10,'ron',True,'Rotwiler','black')
dog.bark()
dog.showData()