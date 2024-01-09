import random
word_list = ["baboon", "mouse", "complete"]

chosen_word = random.choice(word_list)
print(chosen_word)
display = []
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter:\n").lower()
    
    chosen_word_list = list(chosen_word)
    print(chosen_word_list)
    for char in chosen_word:
        if char == guess:
            display.append(guess)
        else:
            display.append('_')
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win")
#     else:
#         print("You win")
# # for 

# guess = input("Guess a letter:\n").lower()

# for letter in chosen_word:
#     if letter == guess:
#         print("right")
#     else:
#         print("wrong")
