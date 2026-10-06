class base:
    a = 10
    def getInfo2(self): 
        print('The number is',self.a)
    # it is bound to the class not to the object of the class
    @classmethod
    def getInfo(cls): 
        print('The number is',cls.a)


test = base()
test.a = 100
# print 10 because of class decorator
test.getInfo()
# prints 100 because we have set the value of a as 100 
test.getInfo2()