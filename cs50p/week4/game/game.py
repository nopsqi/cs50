import random

while True:
    try:
        number = random.randint(1, int(input("Level: ")))
    except ValueError:
        continue
    break

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    if guess > number:
        print("Too large!")
    elif guess < number:
        print("Too small!")
    else:
        print("Just right!")
        break