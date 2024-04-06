## 4. Number Guessing Game
# Create a number guessing game where the computer generates a random number, and the user tries to guess it. The program should:
# Generate a random number between 1 and 100
# Prompt the user to enter their guess
# Provide feedback if the guess is too high or too low
# Allow the user to keep guessing until they guess the correct number
# Display the number of attempts it took to guess the number

import random

random_number = random.randint(1,1000)

tries = 0

while True:
    try:
        answer = int(input("Please enter your guess: "))
        tries += 1

        if answer < random_number:
            print("Higher!")
        elif answer > random_number:
            print("Lower!")
        else:
            print(f"Correct! You took {tries} to guess it.")
            break
    except ValueError:
        print("enter a number lol")