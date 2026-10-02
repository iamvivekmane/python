# find out the line number in which the target word is present
file = open('python.txt')
lineNumber = 0
index = 0
for content in file:
    lineNumber +=1
    if 'python' in content:
        index = lineNumber
        break
if index==0:
    print("not found")
else:
    print("fount at line number",index)
