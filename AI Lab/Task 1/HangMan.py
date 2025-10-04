import random

print("Welcome to Hangman game")
print("-----------------------------------")
word_dict = ("name", "age", "salary", "ali", "ahmad", "movies", "show")


chosen_word = random.choice(word_dict)

amount_of_times_wrong = 0
current_letter_guessed = []
current_letters_right = 0

def print_hangman(wrong):
    if (wrong==0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("    ===")
    elif (wrong==1):
        print("\n+---+")
        print("o   |")
        print("    |")
        print("    |")
        print("    ===")
    elif (wrong==2):
        print("\n+---+")
        print("o   |")
        print("|   |")
        print("    |")
        print("    ===")
    elif (wrong==3):
        print("\n+---+")
        print(" o  |")
        print("/|  |")
        print("    |")
        print("    ===")
    elif (wrong==4):
        print("\n+---+")
        print(" o  |")
        print("/|\ |")
        print("    |")
        print("    ===")
    elif (wrong==5):
        print("\n+---+")
        print(" o  |")
        print("/|\ |")
        print("/   |")
        print("    ===")
    elif (wrong==6):
        print("\n+---+")
        print(" o  |")
        print("/|\ |")
        print("/ \ |")
        print("    ===")

def printword(guessletter):
    for char in chosen_word:
        if char in guessletter:
            print(char, end=" ")
        else:
            print("_", end=" ")
    print()

def printlines():
    print("\r")
    for char in chosen_word:
        print("\u203E", end=" ")

print(" ".join("_" for _ in chosen_word))

while amount_of_times_wrong != 6 and current_letters_right != len(chosen_word):
    print("\n Letters guessed so far: ")
    for letter in current_letter_guessed:
        print(letter, end=" ")

    # User input
    letter_guessed = input("ENTER YOUR GUESS: ")

    if letter_guessed in chosen_word:
        current_letter_guessed.append(letter_guessed)
        current_letters_right = sum(1 for char in chosen_word if char in current_letter_guessed)
        printword(current_letter_guessed)
    else:
        amount_of_times_wrong += 1
        current_letter_guessed.append(letter_guessed)
        print_hangman(amount_of_times_wrong)
        printword(current_letter_guessed)

print("GAME IS OVER THANKS FOR PLAYING")
