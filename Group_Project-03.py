"""
File: Prove_03.py
Author: Tim Illguth
Professor: Gabriel Haynie
Purpose: Calculate a grade
"""

# Starting off with a message to the user about what the program does
print("Hello user, this python program will help you see the letter grade")
print("Please, enter the number of the percent grade you recived")
grade = float(input("> "))
if grade >= 90:
    letter = "A"
    print(f"Congradulations! you got an {letter}!")
elif grade >= 80:
    letter = "B"
    print(f"Not bad, you got a {letter}.")
elif grade >= 70:
    letter = "C"
    print(f"Hey, don't sweat it, {letter}'s get degrees")
elif grade >= 60:
    letter = "D"
    print(f"You can get some help at the study hall. {letter}'s mean you're missing somthing")
else:
    letter = "F"
    print(f"No way to sugar coat it, you failed the class with an {letter}. Sorry")

print("If you're interested to see you plus or minus grade, see below:")

# Setting the variables for '+' and '-'