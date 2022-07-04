from random import randint
from time import sleep

print(" >>> Guess The Number <<< ")
sleep(1)

number = (input("Choose a number between '1' and '10'\n"
                "When you chose, press 'Enter'"))

guess = randint(1, 10)

while True:
    print("Computer's guess is " + str(guess))
    result = (input("Is it correct?\n"
                    "'y' for YES  |  '+' for Greater  |  '-' for Smaller\n"
                    ">>>  "))

    if result == "+":
        guess = randint(guess+1, 10)
    elif result == "-":
        guess = randint(1, guess-1)
    elif result == "y":
        print("Computer guessed the number correctly!")
        break
