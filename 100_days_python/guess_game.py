import random



print("Welcome to DaveTech Number Guess")
print("I'm thinking of a number between 1 and 100 ")

level = input("Choose a difficulty: Type 'easy' or 'hard': ")

numbers = []
for number in range(1, 101):
    numbers.append(number)

secret_num_list = numbers

secret_num = random.choice(secret_num_list)
print(secret_num)


guess_count = 1
guess_limit = 0
if level == "easy":
    guess_limit = 10
elif level == "hard":
    guess_limit = 5


while guess_count <= guess_limit:
    
    print(f"You have {guess_limit} attempts remaining to guess the number")

    
    guess = int(input("Make a guess: "))
    
    def guess_number():

        if secret_num == guess:
            print("You win")
        
        elif secret_num > guess:
            print("Too Low")
        else:
            print("Too High")
        return "guess again"
    print(guess_number())
    guess_limit -= 1
    
    
# name = "Oladipupo"
# first_name = "Olanipo"

# num_of_student = 34
# favorite_color1 = "Black"
# favorite_color2 = "Red"

# True = "Johnson"
# break
# for
# list
# continue
# True
# print
# input

