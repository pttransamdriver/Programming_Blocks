"""
File: teach06_sample.py
Author: Tim Illguth
Professor: Gabriel Haynie
Purpose: Amusement park ride requirements.
"""
print("")
print("################################################################################################")
print("Hello and welome to Python Coaster! You will need to meet certain requirments to ride.")
print("Please answer the following questions:")
print("################################################################################################")
print("")
# Input the first rider's age and hight
age1 = int(input("What's the first riders age: "))
height1 = float(input("Enter the first rider's height in inches: "))

# If the first rider's age is between 12 and 17 and their hight is above 36 inches. Check if they have a golden ticket
if age1 >= 12 and age1 < 18:
    golden_pass1 = input("Does the first rider have the infamus 'golden passport'? (Y/N): ").upper()

# Ask if there is a second rider:
rider2 = input("Will there be a second rider? (Y/N): ").upper()
if rider2 == "Y":

    # Input the second rider's age and hight
    age2 = int(input("Enter the second rider's age: "))
    height2 = float(input("Enter the second rider's height in inches: "))

    # If the second rider's age is between 12 and 17 and their hight is above 36 inches. Check if they have a golden ticket
    if age2 >= 12 and age2 <= 17 and height2 >= 36:
        golden_pass2 = input("Does the Second rider have the infamus 'golden passport'? (Y/N): ").upper()
        if golden_pass2 == "Y":
            print("You two have fun on the ride! ")
        elif age2 <= 17 or golden_pass2 =="N":
            print("Sorry, riders don't meet the requirments for this ride")

# Check if the riders meet the requirements to ride
    if height1 >= 36 and height2 >= 36:
        if age1 >= 18 or age2 >= 18:
            print("Riders can ride the ride")
        elif age1 < 18 and age2 < 18:
            print("Riders cannot ride the ride")
    elif age1 >= 12 and golden_pass1 == "Y":
        print("Have fun on the ride!")
    elif age1 <= 17 and golden_pass1 == "N":
        print("Sorry, you don't meet the requirments for this ride :(") 

else:
    print("Sorry, rider(s) don't meet the ride qualifications :(")