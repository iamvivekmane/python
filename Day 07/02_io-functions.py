file = open("random.txt")
# it returns a single line from the file
content = file.readline()

# it returns a all the lines from the file in an list
content2 =  file.readlines()
# print(content2,type(content2))

# using with statement enables us not to close the file explicitly
with open("random.txt","r") as f:
    print(f.read())
    