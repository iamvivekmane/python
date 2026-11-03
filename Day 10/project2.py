import random
computer = random.randint(1,100)
print(computer)
guesses = 1
while(True):
    user = int(input('Guess the number  :   '))
    if(user==computer):
        print('You won!!!')
        print('You required',guesses,'guesses')
        print('The number is',user)
        break
    elif(user>computer):
        guesses+=1
        print('Its lower')
    elif(user<computer):
        guesses+=1
        print('Its greater')