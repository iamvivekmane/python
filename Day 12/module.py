def myfunc():
    print('Hello world')
    
myfunc()
# it will print main if we run this file
# and if we import this file in another program and then run it then it will print the name of this file

if __name__ =='__main__':
    print(__name__)
    print('This code is getting executed using this file')