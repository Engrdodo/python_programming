import random
from hangman_words import word_list
from hangman_art import logo, stages
# from replit import clear

print(logo)
print("Welcome to DAVETECH HANGMAN GAME, You've got six chances to save your man")
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f"The word is '{chosen_word}':(testing purpose)")
display = []
end_of_game = False
lives = 6
for _ in range(word_length):
    display += "_"
while not end_of_game:
    guess = input("Guess a letter:\n").lower()
    
    # clear()-----clear function from replit to clear hangman art stages backlog
    if guess in display:
        print(f"You've already guessed {guess}")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
  
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])
