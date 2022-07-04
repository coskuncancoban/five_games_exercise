from random import choice
from time import sleep

print(" >>> Rock Paper Scissors <<< \nType 'q' for Quit")
options = ["rock", "paper", "scissors"]

computer = choice(options)

while True:
    while True:

        user = input("Please type 'rock' or 'paper' or 'scissors'\n>>>")

        if user == "q":
            break
        elif user not in options:
            print("You typed undefined character!")
            sleep(1)

        else:
            break

    choices = f"Your choice is {user}\nComputer's choise is {computer}\n"

    if user == "q":
        break

    if user == computer:
        print(choices + "It's a Tie!")
        sleep(1)
    elif user == "rock":
        if computer == "paper":
            print(choices + "Paper covers Rock! You Lose.")
            sleep(1)
        else:
            print(choices + "Rock breaks Scissors! You Win.")
            sleep(1)
    elif user == "paper":
        if computer == "rock":
            print(choices + "Paper covers Rock! You Win.")
            sleep(1)
        else:
            print(choices + "Scissors cuts Paper! You Lose.")
            sleep(1)
    elif user == "scissors":
        if computer == "rock":
            print(choices + "Rock breaks Scissors! Lose.")
            sleep(1)
        else:
            print(choices + "Scissors cuts Paper! You Win.")
            sleep(1)
