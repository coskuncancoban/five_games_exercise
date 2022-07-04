from random import choice
from time import sleep

print(" >>> Magic 8 Ball <<< \nType 'q' for Quit")

answers = ["As I see it, yes.",
           "My sources say no.",
           "Ask again later.",
           "Better not tell you now.",
           "Cannot predict now.",
           "Don't count on it.",
           "It is certain.",
           "Concentrate and ask again.",
           "It is decidedly so.",
           "Most likely...",
           "My reply is no.",
           "Outlook good.",
           "Outlook not so good.",
           "Reply hazy try again",
           "O soru öyle mi sorulur?! "
           "Daly*rak! "
           "Kaç yaşındasın sen???",
           "Signs point to yes.",
           "Very doubtful.",
           "Without a doubt.",
           "Yes.",
           "No.",
           "Yes, definitely.",
           "You may rely on it"]

while True:
    question = input("Ask your question to the Magic 8 Ball, it will answer it!\n>>> ")
    if question == "q":
        break
    print("Thinking...")
    sleep(1)
    print(choice(answers))
    sleep(1)
