"""
File: Group_project-09.py
Author: Tim Illguth
Purpose: Practice using listseses
"""


# Create an empty list to store numbers
numbers = []

# Loop until the user types '0' or the program hits 'break'
print("Welcom to python number list maker!")
while True:
    # Ask the user for a number
    number = int(input("Enter a number (type '0' to stop): "))

    # Check if the user typed '0' to exit the loop
    if number == 0:
        # Break the while loop if the user types '0'
        break

    # Append the number(input from the user) to the list called 'numbers'
    numbers.append(number)

# Display the list of numbers
print("The numbers you entered are:")
for number in numbers:
    print(number)

# Find the smallest positive number and set that to 'positive_numbers' by using the
# LIST COMPREHENSION feature in Python. This takes a list and evaluates 
# This works by saying I want a new list called 'positive_numbers' 
# To build this list use the number (first x) for every position (second 'x') in the list called
# 'numbers' only if that number is greater than 0 (third x, 'if x>0' part)
positive_numbers = [x for x in numbers if x > 0]

# If Else statment for positive and negative numbers
if positive_numbers:
    # Defines 'smallest_positive' by taking the 'min()' of the 'positive_numbers' list
    smallest_positive = min(positive_numbers)
    print(f"The smallest positive number is {smallest_positive}")
else:
    print("There are no positive numbers in the list.")


# Set the average variable by using the sum() divided by len() functions in python.  
average = sum(numbers) / len(numbers)
# Set the Sort variable from the sorted function
sorted = sorted(numbers)

# Printing the sorted, sum and averages listseses
print(f"Sorted numbers list is: {sorted}")
print(f"The sum of the numbers you entered is {sum(numbers)}")
print(f"The Average of the numbers you entered is {(average)}")
