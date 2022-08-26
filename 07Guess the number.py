# example number 1 very ease very funny
from random import randint

guess=randint(1,50)
print(guess)
my_answer=''
while my_answer != 'd':
    my_answer=input()
    if my_answer=="l":
        n=randint(guess,50)
        print(n)

    elif my_answer=='s':
        m=randint(1,guess)
        print(m)
    else:
        print('done')
        
################################# example number 2##############other face of the game#############################

import random

class NumberGuessingGame:

    def __init__(self):
        ## define the range
        self.LOWER = 1
        self.HIGHER = 20

    ## method to generate the random number
    def get_random_number(self):
        return random.randint(self.LOWER, self.HIGHER)

    ## game start method
    def start(self):
        ## generating the random number
        random_number = self.get_random_number()

        print(
            f"Guess the randomly generated number from {self.LOWER} to {self.HIGHER}")

        ## heart of the game
        chances = 0
        while True:
            user_number = int(input("Enter the guessed number: "))
            if user_number == random_number:
                print(
                    f"-> Great! You got it in {chances + 1} step{'s' if chances > 1 else ''}!")
                break
            elif user_number < random_number:
                print("-> Your number is less than the random number")
            else:
                print("-> Your number is greater than the random number")
            chances += 1

## instantiating and starting the game
numberGuessingGame = NumberGuessingGame()
numberGuessingGame.start()