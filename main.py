import random

import hangman_art
import hangman_words

print(hangman_art.logo)
end_of_game = False
lives = 6

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

chosen_word = random.choice(hangman_words.word_list)

display = []

for i in chosen_word:
  display += "_"

while not end_of_game and lives != 0:
  print(hangman_art.stages[lives])
  print(f"Remaining Lives: {lives}")
  guess = (input("Guess a letter: ")).lower()

  for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
      if display[i] == chosen_word[i]:
        print(f"You have already guessed {guess}")
        break
      else:
        display[i] = chosen_word[i]
        
  if guess not in chosen_word:
    print(f"You guessed the letter {guess}, But that's not in the word.")
    print("You Lose a life.")
    lives -= 1

  if lives == 0:
    print(hangman_art.stages[lives])
    print("You Lose")

  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print(hangman_art.stages[lives])
    print("You Won.")