# Snake, Water, Gun game (CLI based)
import random
play = 1

while(play !=0):
    print("Welcome to Snake, Water, Gun game")
    print("1. Snake\n" 
    "2. Water\n" 
    "3. Gun\n")
    choice = int(input("Enter any choice : "))
    user = None

    if(choice == 1):
        user = 'Snake'
    elif(choice ==2):
        user = 'Water'
    elif(choice ==3):
        user = 'Gun'
    else:
        print("Invalid choice")
        break

    com = random.choice(['Snake','Water','Gun'])

    print("User choice      : ",user)
    print("Computer choice  : ",com)

    if(user == 'Gun' and com == 'Snake'):
        print("You won")
    elif(user == 'Water' and com == 'Gun'):
        print("You won")
    elif(user == 'Snake' and com == 'Water'):
        print("You won")
    elif(user == 'Snake' and com == 'Gun'):
        print("You lost")
    elif(user == 'Gun' and com == 'Water'):
        print("You lost")
    elif(user == 'Water' and com == 'Snake'):
        print("You lost")
    else:
        print("Its a draw")
    print("1. Restart")
    print("0. Stop")
    play =int(input())

print("See you again!")