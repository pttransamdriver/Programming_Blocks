"""
File: teach06_sample.py
Author: Tim Illguth
Professor: Gabriel Haynie
Purpose: Amusement park ride requirements.
"""
# Input the first rider's age
age1 = int(input("Enter the first rider's age: "))

# Input the first rider's height
height1 = int(input("Enter the first rider's height in inches: "))

# Input the second rider's age
age2 = int(input("Enter the second rider's age: "))

# Input the second rider's height
height2 = int(input("Enter the second rider's height in inches: "))

# Check if the riders meet the requirements to ride
if height1 >= 36 and height2 >= 36:
    if age1 >= 18 or age2 >= 18:
        print("Riders can ride the ride")
    elif age1 < 18 and age2 < 18:
        print("Riders cannot ride the ride")
else:
    print("Riders cannot ride the ride")
