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
# Input the first rider's age
age1 = int(input("What's the first riders age: "))

if age1 >= 12 and age1 <= 18:
    input("Does the first rider have the infamus 'golden passport'? (Y/N): ").upper()

# Input the first rider's height
height1 = float(input("Enter the first rider's height in inches: "))

# Input the second rider's age
age2 = int(input("Enter the second rider's age: "))

# If the second riders age is 
if age2 >= 12 and age2 <=18:
    input("Does the first rider have the infamus 'golden passport'? (Y/N): ").upper()

# Input the second rider's height
height2 = float(input("Enter the second rider's height in inches: "))

# Check if the riders meet the requirements to ride
if height1 >= 36 and height2 >= 36:
    if age1 >= 18 or age2 >= 18:
        print("Riders can ride the ride")
    elif age1 < 18 and age2 < 18:
        print("Riders cannot ride the ride")
   # elif gold_pass == "Y" and age1 >= 12 or age2 >= 12:
    #    print("Riders can ride this ride! ")
else:
    print("Sorry, riders do nott meet the ride qualifications :()")
