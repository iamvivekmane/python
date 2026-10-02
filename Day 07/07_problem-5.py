# make a copy of a text file
file1 = open('python.txt')
content = file1.read()
file2 = open('copy.txt','w')
file2.write(content)
print(content)