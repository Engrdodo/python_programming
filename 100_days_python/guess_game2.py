from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_answer(guess, answer, turns):
    """Checks answer against checks. Returns the number of turns remaining"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")




answer = randint(1, 100)

def game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    turns = set_difficulty()
    

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses, you lose!")
            return #stops the game and exit the function
        elif guess != answer:
            print("Guess again.")


game()