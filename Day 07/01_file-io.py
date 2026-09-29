# reads data from a text file
file = open("random.txt")
data = file.read()
print(data)
file.close()

# writes data to a text file
# if the file dosent exist it will create the file
content = input("Enter content : ")
file1 = open("written.txt","w")
file1.write(content)
file1.close()

