#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

number_gen = random.randint(1, 100)
print("Welcome to the number guessing game")
print(logo)
print("Choose a difficulty. Type 'easy' or 'hard' ")
difficulty = input().lower()
if difficulty == 'easy':
    turns = 10
elif difficulty == 'hard':
    turns = 5
else:
    print("Invalid selection.Choose again")
print(f"You have chosen difficulty={difficulty}")
print(f"You have {turns}chances to guess the number")
while turns > 0:
    guess = int(input("Guess the number:"))
    if guess == number_gen:
        print(f"You guessed it right.The answer was {number_gen}")
        break
    elif guess > number_gen:
        print("Too high")
        turns -= 1
    elif guess < number_gen:
        print("Too low")
        turns -= 1
    if turns == 0:
        print("You lost")
