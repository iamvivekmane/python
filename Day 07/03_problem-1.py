# find out wheather it contains the word or not
file = open('random.txt')
content = file.read()
if content.find('twinkle')!=-1:
    print('Found twinkle')
else:
    print('Not found')