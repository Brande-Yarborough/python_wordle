import random

print("WORDLE!")
print("How to Play: ")
print("Guess a 5 letter word in 6 tries")

# use ANSI color codes for background color
BG_GREEN = "\u001b[42m"
BG_YELLOW = "\u001b[43m"
RESET = "\u001b[0m"

# implement random.choice list for word list
correct_word = random.choice(["HOUSE", "SUGAR", "BLACK", "SLEEP", "GRAZE"])
# gives 6 guesses
for guesses in range(6):
    guess = input("Guess a 5 letter word: ").upper()

    # check each letter
    # create for loop to iterate through each character in word at specific index
    for i in range(0, 5):
        if guess[i] == correct_word[i]:
            print(f"{BG_GREEN}{guess[i]}{RESET}",
                  end="")  # end prints horizontal
        elif guess[i] in correct_word:
            print(f"{BG_YELLOW}{guess[i]}{RESET}", end="")
        else:
            print(guess[i], end="")
    # add print at end of for loop, so goes to next line for next round
    print("")

    # check if guess is correct
    if guess == correct_word:
        print("You win!")
        exit()

# if guess not correct
print("Your guess was not correct.")
print(f"The correct word was {correct_word}.")
