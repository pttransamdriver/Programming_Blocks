import random

# Define a list of secret words to use in the game
WORDS = ["code", "assignment", "while", "loop", "python", "vscode"]

# Choose a random secret word from the list
secret_word = random.choice(WORDS)

# Define a list to store the user's guesses
guesses = []

# Print the initial hint with underscores
hint = ["_" for letter in secret_word]
print("Hello player, let's play a python wordle!")
print("for this game you will need to guess a word.")
print("I will show you the number of letters in the word with '_' representing each letter.")
print("A Lowercase letter will be seen if the letters you have gessed are in the word.")
print("An Uppercase letter will be shown if you guess the correct letter with the correct placment")
print(" ".join(hint))

# Loop until the user guesses the word
while True:
    # Ask the user to guess the word
    guess = input("Enter your guess: ").lower()

    # Check if the guess has the same length as the secret word
    if len(guess) != len(secret_word):
        print("Your guess must have the same number of letters as the secret word.")
        continue

    # Add the guess to the list of guesses
    guesses.append(guess)

    # Check if the 'guess' is correct
    if guess == secret_word:
        print("Congratulations! You Win! You guessed the word in", len(guesses), "tries.")
        print(f"Here is a list of your valid guesses: {guesses}")
        break

    # Update the hint with correct letters and lowercase letters in the wrong position
    for letter in range(len(secret_word)):
        if guess[letter] == secret_word[letter]:
            hint[letter] = secret_word[letter].upper()
        elif guess[letter] in secret_word:
            hint[letter] = guess[letter]

    # Print the updated hint
    print(" ".join(hint))

