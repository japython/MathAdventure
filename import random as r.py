import random as r

def numberGame():
    #Choose number from 1 to 100
    #Choose the other number manually

    number = r.randint(1, 100)

    print("Guess a particular number")
    guess = int(input("Input the number you guess"))

    while guess:
        if number == guess:
            print("Bingo!")
            break

        elif number > guess:
            print("Boo bigger")

        else:
            print("Boo smaller")
        
        guess = int(input("Input the number you guess"))

numberGame()