#hangman
#run from terminal to work right
import random
import os

with open("Words.txt",'r') as f:
    words = f.readlines()
    guessed_word = random.choice(words)
    #print(guessed_word)

hidden_word = ''

for i in guessed_word[0:-1]:
    hidden_word += '_'

print(hidden_word)
num_guesses = 5
while True:
    counter = 0
    player_choice = input("Enter a letter: ").lower()

    if player_choice in guessed_word and (len(player_choice)+1) == len(guessed_word):
        hidden_word = guessed_word
    elif player_choice not in guessed_word:
        num_guesses = num_guesses - 1
    else:
        for i in guessed_word:
            if i == player_choice:
                hidden_word = hidden_word[:counter] + player_choice + hidden_word[counter+1:]
            counter += 1

    clear = lambda: os.system('cls')
    clear()
    print(hidden_word)
    if '_' not in hidden_word:
        print(f"You guess the word {hidden_word}")
        break
    elif num_guesses > 0:
        print(f"You have {num_guesses} wrong guesses left!")
        if num_guesses == 4:
            print("        |     ")
            print("        |     ")
            print("        |     ")
        elif num_guesses == 3:
            print("        |     ")
            print("        |     ")
            print("        |     ")
            print("       / \   ")
            print("      /   \   ")
            print("     /     \   ")
        elif num_guesses == 2:
            print(" <----- | ------>    ")
            print("        |     ")
            print("        |     ")
            print("       / \   ")
            print("      /   \   ")
            print("     /     \   ")
        elif num_guesses == 1:
            print("        # ")
            print(" <----- | ------>    ")
            print("        |     ")
            print("        |     ")
            print("       / \   ")
            print("      /   \   ")
            print("     /     \   ")


    elif num_guesses == 0:
        print("        #______________")
        print(" <----- | ------>     |")
        print("        |             |")
        print("        |             |")
        print("       / \            |")
        print("      /   \           |")
        print("    _/     \_         |")
        print("                      |")
        print("______________________|")
        print("You lose")
        print(f"The word was {guessed_word}")
        break







