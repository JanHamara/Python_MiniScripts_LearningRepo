#! /usr/bin/env python
""" guessnumbergame.py, by Jan Hamara, 2018-01-10

    This game asks the user to guess number between 1 and 100.
"""

import random as rndm


def new_game():
    main()

def main():
    print(20 * "-")
    print("Guess a number between 1 and 100 !")

    randomNumber = rndm.randint(1,100)
    guessedNumber = False
    newGamePrompt = False

    while not guessedNumber:
        userGuess = int(input("Your Guess: "))

        if userGuess == randomNumber:
            print("Congratulations! It is ", randomNumber)
            break
        elif userGuess > randomNumber:
            print("Try again. Guess Lower..")
        else:
            print("Try again. Guess Higher..")

    while not newGamePrompt:
        newgame = input("Do you want to play again? Y/N")

        if newgame == 'Y':
            new_game()
            newGamePrompt = True
        elif newgame == 'N':
            print("See you later!")
            newGamePrompt = True
        else:
            print("Answer either Y for 'yes' or answer N for 'no'... ")

if __name__ == '__main__':
    main()


