"""
File: Prove_03.py
Author: Tim Illguth
Professor: Brother Burton

"""
# Pull the Library that we will need to complete this assignment
import math

# functions to calculate the area of a square, the volume of the square and make adjustments for square meters
def square_area(side): #"Def" is a Function. We haven't really covered them yet but they are in the 29th video of the "python for beginners" videos we got links to at the start of the course
    return side ** 2 # This is saying "define 'square_area' as 'side^2' or in otehr words whatever 'side' is squared
def volume(side): #Defines volume as a function that does something to 'side'
    return side ** 3 #Defines 'volume' as 'side^3' or 'side cubed'
def meter_area(side): #Defines 'meter_area' as a function that does something to 'side'
    return side **2 /10000 #defines the function 'meter_area' as somthing that takes 'side' squares it and divides it by 10,000 to get meters from the cetemeters. 

# functions to calculate the area of a rectangle and make adjustments for meters
def rectangle_area(length, width): #Defines the function rectangle_area as something that does stuff to the variables 'width and length'
    return length * width #Defines the function 'rectangle_area' as something that takes 'length' and 'width' as a function that multiplies the variables
def rec_meter(length, width):
    return length * width /10000

# functions to calculate the area of a circle, the Volume of a sphere and adjust for Meters
def circle_area(radius):
    return math.pi*(radius**2)
def sphere(radius):
    return math.pi*(radius**3)*(4/3)
def meter_circ(radius):
    return math.pi*(radius**2)/10000

# prompt for user input of square side then print the area and the volumes
print("Square:")
side = float(input("Enter the side length in centimeters: ")) 
print("The area of the square is" , square_area(side) , "in centimeters squared")
print("The area of the square is", meter_area(side) ," in meters squared ")
print("The Volume of this as a cube would be:",  volume(side))

# prompt for user inputs of the sides of a rectangle and print in meters and centimeter areas  
print("Rectangle:")
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
print("The area of the rectangle is", rectangle_area(length, width) ," in centimeters squared")
print("The area of the rectangle is", rec_meter(length, width) ," in meters squared")

# prompt for user input of circle radius and print out the area, spherical volume and adjust for ssquare meters too. 
print("Circle:")
radius = float(input("Enter the radius: "))
print("The area of the circle is", circle_area(radius) ,"in centimeters squared")
print("The area of the circle is", meter_circ(radius) ," in meters squared ")
print("The Volume of this as a sphere would be", sphere(radius))
