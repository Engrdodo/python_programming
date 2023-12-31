import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

# checks the user's input
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Players must be 2- 4")
    else:
        print("Invalid, try again.")


max_score = 50
player_scores = [3 for i in range(players)]
print(player_scores)





