"""
File: Group_Project-07.py
Author: Tim Illguth
Professor: Gabriel Haynie
Purpose: Guess the random generated number.
"""

# This stanza imports the random number generator function native to python
import random

# This is the outer loop for the user to play again if they would like
while True:
    # Defines the 'number' variable as the random integer between 1 and 100
    number = random.randint(1, 100)
    # Defines the 'guesses' variable starting at 0 for the purpose of counting guesses
    guesses = 0

    # This is an internal while loop to help guide the guesses of the user until the right guess is achieved
    while True:
        # This defines the users guess at the magic number
        guess = int(input("Guess the magic number between 1 and 100: "))
        # This adds '1' to each 'guesses' variable eaach the loop run. 
        guesses += 1
        # If the guess is outside the 100 limit it remindes the user to guess between 1 and 100
        if guess < 1 or guess > 100:
            print("Sorry, plese enter a number between 1 and 100")
        # Gives the hint to guess higher 
        elif guess < number:
            print("Guess needs to be higher")
        # Gives the hint to guess lower
        elif guess > number:
            print("Guess needs to be lower")
        # If the guess doesn't fit the above criteria it will naturally be the answer and therefore 'else'
        else:
            print(f"Good job you guessed the number! You used {guesses} guesses!")
            break
    # Now that the inside 'while True' loop is broken (at 'break') the outer loop asks for a "Y" to play again
    play_again = input("Would you like to play again? (Y/N): ")
    # If the play again veriable is 'Y' the outer loop with its inner loop runs again
    if play_again.upper() != "Y":
        print("Thanks for playing! ")
        break
