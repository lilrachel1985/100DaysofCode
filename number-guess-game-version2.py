from random import randint
""" Set the global variable outside the function """
EASY=10
HARD=5
def set_difficulty():
    level=input("Choose the difficulty. Type 'easy' or'hard': ")
    if level=="easy":
        return EASY
    elif level=="hard":
        return HARD

def check_answer(guess,answer,turns):
    if guess>answer:
        print("Too high")
        return turns-1
    elif guess<answer:
        print("Too low")
        return turns-1
    else:
        print(f"You got it. The answe is {answer}")

def game():
    print("Welcome to the Number Guessing Game")
    print("Im thinking of a number between 1 and 100")
    answer= randint(1,100)
    guess=0
    turns=set_difficulty()
    while guess!=answer:
        guess = int(input("Make a guess"))
        turns=check_answer(guess,answer,turns)
    if turns==0:
        print("You have run out of guesses.You lose")
        return
game()
    
    