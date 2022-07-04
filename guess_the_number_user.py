from random import randint
from time import sleep

print(" >>> Guess The Number <<< ")
sleep(1)

number = randint(1, 10)
print("Computer chose a number between '1' and '10'")

while True:
    guess = (input("What is your guess? >>> "))

    if int(guess) > int(number):
        print("The number is smaller than " + guess)
        sleep(1)

    elif int(guess) < int(number):
        print("The number is greater than " + guess)
        sleep(1)

    else:
        print("You guessed the number!")
        break
