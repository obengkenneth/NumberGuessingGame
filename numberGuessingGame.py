#  number guessing game

from random import randint

def playAgain():
    game = input("Type yes to play again or no to quit : ").lower()
    if game == "yes" or game == "no":
        return game
    else:
        print("Please enter a valid input")
        playAgain()

# intro
print("*" * 50)
print(" \t Welcome to the Guessing Game! \t")
print("*" * 50)
number = randint(0, 100)
guesses = 0
play = "yes"

# main game loop
while play == "yes":
    try:
        print("Try to guess the number I'm thinking of! The number is between 0 and 100.")
        ans = input("Type the number : ")
        guesses += 1 
        if int(ans) == number:
            print("Congrats! You guessed the number correctly.")
            print(f'It took you {guesses} guesses')
            print("*" * 50)
            print("\tThank you for playing the Guessing Game!\t")
            print("*" * 50)
            play = playAgain()
            
        elif int(ans) > number:
            print("The number is lower than the number you guessed.")
        else:
            print("The number is bigger than the number you guessed.")
    except:
        print("Please type a valid number!")



