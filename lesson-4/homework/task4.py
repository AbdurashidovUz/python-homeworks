import random

number = random.randint(1, 100)
attempts = 10

while attempts > 0:
    guess = int(input(f"You have {attempts} attempts left. Enter your guess: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You guessed it right!")
        break

    attempts -= 1

if attempts == 0:
    print("You lost.")
