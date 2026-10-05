# Create a class “Programmer” for storing information of few programmers working at
# Microsoft
class employee:
    company = 'Microsoft'
    name = 'john'
    language = 'cpp'
    id = 100
    def __init__(self,name,language,id):
        self.name = name
        self.language = language
        self.id = id
    def getInfo(self):
        print('Id       :   ',self.id)
        print('Name     :   ',self.name)
        print('Company  :   ',self.company)
        print('Language :   ',self.language)
raj = employee('raj','python',102)
raj.getInfo()
ram = employee('ram','c',109)
ram.getInfo()
        

