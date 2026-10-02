# replace word in a file
file = open('donkey.txt','r')
content = file.read()
new = content.replace('donkey','#####')
print(new)
file2 = open('donkey.txt','w')
file2.write(new)