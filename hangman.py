from random import choice
from time import sleep

print(" >>> Hangman <<< \n")
sleep(1)
words = ["minimum", "visible", "expend", "interface", "continental", "sense",
         "detail", "personal", "designer", "bee", "finish", "radiation",
         "peak", "shadow", "medieval", "kill", "corpse", "application", "cheap",
         "point", "record", "fire", "contrast", "tourist", "suffer", "exotic",
         "photograph", "look", "even", "personality", "movie", "broccoli",
         "therapist", "hardware", "shape", "bird", "intelligence", "patience"]

word = choice(words)
word_ = word
question = len(word) * "_"
print("You have 6 chances!")
sleep(1)


def wrong(q, a=" ", b=" ", c=" ", d=" ", e=" ", f=" "):
    print("    _______")
    print("    |     |")
    print(f"    |     {a}")
    print(f"    |    {b}{c}{d}")
    print(f"    |    {e} {f}")
    print(f"    |___________")
    print(f"    ||||||||||||        word >   {q}")


wrong(question)
used = set(())
index = -1
wrong_answer = 0

while True:

    letter = input(64 * "-" + "\nGuess a letter >>> ")
    if len(letter) > 1:
        print("You shold type only one letter!")
        sleep(1)
        continue
    index = -1
    while True:
        if letter in word_:
            index = int(word_.find(letter))
            question = question[:index] + letter + question[(index + 1):]
            word_ = word_[:index] + " " + word_[(index + 1):]
            print("word > " + question)
        else:
            break

    if letter in used:
        print("You already used that letter!")

    elif letter not in word:
        print(f"The word doesn't have '{letter}' letter!")
        wrong_answer += 1

    used.add(letter)
    print("used letters")
    print(used)
    sleep(1)

    if "_" not in question:
        print(f"You won! The word was {word}.")
        print("    \\O/" + "\n     |" + "\n    / \\")

        break

    if wrong_answer == 1:
        wrong(question, a="O")
    elif wrong_answer == 2:
        wrong(question, a="O", c="|")
    elif wrong_answer == 3:
        wrong(question, a="O", b="/", c="|")
    elif wrong_answer == 4:
        wrong(question, a="O", b="/", c="|", d="\\")
    elif wrong_answer == 5:
        wrong(question, a="O", b="/", c="|", d="\\", e="/")
    elif wrong_answer == 6:
        wrong(question, a="O", b="/", c="|", d="\\", e="/", f="\\")
        print(f"\nThe word was '{word}',Game Over...")
        break
