# print a message if one of the file do not exist while opening multiple files
try:
    file1 = open("1.txt")
    file2 = open("2.txt")
    file3 = open("3.txt")
    file4 = open("4.txt")
except:
    print('Some of the file is missing')

