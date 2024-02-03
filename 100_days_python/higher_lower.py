from art import logo, vs
from game_data import data
import random
print(logo)
score = 0
game_should_continue = True
 account_b = random.choice(data)

def format_data(account): 
    """formats the account_data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Takes the guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
while game_should_continue:
    #generates random account from the game data
    account_a = account_b
    account_b = random.choice(data)
   
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    #ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    ## Get follower account of each follower
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #CLEAR()
    print(logo)

    #Give user feedback on their guess.
    if is_correct:
        print(f"You are right! Current score: {score}")
        score += 1
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
