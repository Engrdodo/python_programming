import random

word_list = ["baboon", "mouse", "complete"]

chosen_word = random.choice(word_list)
print(chosen_word)

end_of_game = False
display = ['_'] * len(chosen_word)

while not end_of_game:
    guess = input("Guess a letter:\n").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    print(' '.join(display))

    if "_" not in display:
        end_of_game = True
        print("You win")
