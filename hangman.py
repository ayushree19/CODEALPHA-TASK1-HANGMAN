import random

# List of 5 predefined words
words = ["python", "coding", "laptop", "program", "developer"]

# Select a random word
word = random.choice(words)

# Store the letters guessed by the player
guessed_letters = []

# Count the number of wrong guesses
wrong_guesses = 0

print("===================================")
print("          HANGMAN GAME")
print("===================================")
print("Guess the hidden word!")
print("You can make maximum 6 wrong guesses.")
print()

# Game loop
while wrong_guesses < 6:

    # Display the current word
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)
    print("Wrong guesses:", wrong_guesses, "/ 6")

    # Check if the complete word has been guessed
    if all(letter in guessed_letters for letter in word):
        print()
        print("Congratulations! You won!")
        print("The word was:", word)
        break

    # Take input from the player
    guess = input("Enter a letter: ").lower()

    # Check whether input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        print()
        continue

    # Check whether the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed this letter.")
        print()
        continue

    # Add the guessed letter to the list
    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

    print()

# Game over
if wrong_guesses == 6:
    print("===================================")
    print("            GAME OVER")
    print("===================================")
    print("The correct word was:", word)