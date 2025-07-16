import random
from hangman_words import word_list

HANGMANPICS = [
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\ |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\   |
 / \\   |
      |
========='''
]

print('''
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\\__,_|_| |_|\__, |_| |_| |_|\\__,_|_| |_|
                      __/ |                      
                     |___/                       
''')

chosen_word = random.choice(word_list)
placeholder = ""

for position in range(len(chosen_word)):
  placeholder += "_ "

print(placeholder)

correct_letters = []
game_over = False
lives = 6
stage = 0

while not game_over:
  display = ""
  guess = input("Guess a Letter: ").lower()

  if guess in correct_letters:
    print(f"You've already guessed {guess}")

  for letter in chosen_word:
    if letter == guess:
      display += letter
      correct_letters.append(guess)
    elif letter in correct_letters:
      display += letter
    else:
      display += "_ "

  print(display)

  if "_" not in display:
    game_over = True
    print("You win!")

  if guess not in chosen_word:
    lives -= 1
    stage += 1

    print(HANGMANPICS[stage])
    print(f"**************************<> {lives} LEFT <>********************************")

    if lives == 0:
      print("You Lose")
      print("The word is " + chosen_word)
      game_over = True
