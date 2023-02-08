
"""
File: teach04_sample.py
Author: Brother Burton

Purpose: Calculate the speed of a falling object using the formula:

v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)*t))

"""
import math

# Print a welcome message
print("Welcome to the velocity calculator! Lets' have fun with some physics!")

# Get input from user
mass = float(input("Enter the mass of the object (in kg): "))
gravity = float(input("Enter the gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time = float(input("Enter the time (in seconds): "))
density = float(input("Enter the density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
area = float(input("Enter the cross sectional area (in m^2): "))
drag_constant = float(input("Enter the drag constant (0.5 for sphere, 1.1 for cylinder): "))

# Calculate the velocity
c = (1 / 2) * density * area * drag_constant # The 'c' is the drag co-efficient 
velocity = math.sqrt(mass * gravity / c) * (1 - math.exp((-math.sqrt(mass * gravity * c) / mass) * time))

# Display the results
print(f"The inner value of c is: {c:.3f}")
print(f"The velocity after {time} seconds is: {velocity:.3f} m/s")

print("")
print(''' #######################################################################################################
#######################################################################################################''')
print("")

# Print a welcome message
print("Lets' have fun with some physics and a skydiver!")

# Get input from user
mass_skydiver = float(input("Enter the mass of your skydiver (in kg): "))
gravity_skydiver_earth = 9.8
gravity_skydiver_jupiter = 24
time_skydiver = float(input("Enter the time_skydiver (in seconds): "))
density_skydiver = float(input("Enter the density_skydiver of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
area_skydiver = float(input("Enter the cross sectional area of your skydiver (in m^2) .17 for diving and 2 for laying flat and spread out: "))
drag_constant_skydiver = 1.1

# Calculate the velocity_skydiver
c_skydiver= (1 / 2) * density_skydiver * area_skydiver * drag_constant_skydiver # The 'c' is the drag co-efficient 
velocity_skydiver_earth = math.sqrt(mass_skydiver * gravity_skydiver_earth / c_skydiver) * (1 - math.exp((-math.sqrt(mass_skydiver * gravity_skydiver_earth * c) / mass_skydiver) * time_skydiver))
velocity_skydiver_jupiter = math.sqrt(mass_skydiver * gravity_skydiver_jupiter / c_skydiver) * (1 - math.exp((-math.sqrt(mass_skydiver * gravity_skydiver_jupiter * c) / mass_skydiver) * time_skydiver))


# Display the results
print(f"The inner value of c for your skydiver on earth is: {c_skydiver:.3f}")
print(f"The velocity of your skydiver on Earth after {time_skydiver} seconds is: {velocity_skydiver_earth:.3f} m/s")
print(f"The velocity of your skydiver onJupiter after {time_skydiver} seconds is: {velocity_skydiver_jupiter:.3f} m/s")

print("")
print('''#######################################################################################################
#######################################################################################################''')
print("")

# Print a welcome message
print("Lets' have fun with some physics adn a loaf of bread!")

# Get input from user
mass_bread = float(input("Enter the mass_bread of the object (in kg): "))
gravity_bread_earth = 9.8
gravity_bread_jupiter = 24
time_bread = float(input("Enter the time that the bread will be falling (in seconds): "))
density_bread = float(input("Enter the density of the fluid the bread is falling through (in kg/m^3, 1.3 for air, 1000 for water): "))
area_bread = .07
drag_constant_bread = 1.1

# Calculate the velocity_bread
c_bread= (1 / 2) * density_bread * area_bread * drag_constant_bread # The 'c' is the drag co-efficient 
velocity_bread_earth = math.sqrt(mass_bread * gravity_bread_earth / c_bread) * (1 - math.exp((-math.sqrt(mass_bread * gravity_bread_earth * c) / mass_bread) * time_bread))
velocity_bread_jupiter = math.sqrt(mass_bread * gravity_bread_jupiter / c_bread) * (1 - math.exp((-math.sqrt(mass_bread * gravity_bread_jupiter * c) / mass_bread) * time_bread))


# Display the results
print(f"The inner value of c for the bread on earth is: {c_bread:.3f}")
print(f"The velocity_bread on earth after {time_bread} seconds is: {velocity_bread_earth:.3f} m/s")
print(f"The velocity_bread on Jupiter after {time_bread} seconds is: {velocity_bread_jupiter:.3f} m/s")

print("")
print('''#######################################################################################################
#######################################################################################################''')
print("")

# Print a welcome message
print("Lets' have fun with some physics and a bowling ball!")

# Get input from user
mass_bowlingball = float(input("Enter the mass_bowlingball of the object (in kg): "))
gravity_bowlingball_earth = 9.8
gravity_bowlingball_jupiter = 24
time_bowlingball = float(input("Enter the time_bowlingball (in seconds): "))
density_bowlingball = float(input("Enter the density_bowlingball of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
area_bowlingball = float(input("Enter the cross sectional area_bowlingball (in m^2): "))
drag_constant_bowlingball = .5

# Calculate the velocity_bowlingball
c_bowlingball= (1 / 2) * density_bowlingball * area_bowlingball * drag_constant_bowlingball # The 'c' is the drag co-efficient 
velocity_bowlingball_earth = math.sqrt(mass_bowlingball * gravity_bowlingball_earth / c_bowlingball) * (1 - math.exp((-math.sqrt(mass_bowlingball * gravity_bowlingball_earth * c) / mass_bowlingball) * time_bowlingball))
velocity_bowlingball_jupiter = math.sqrt(mass_bowlingball * gravity_bowlingball_jupiter / c_bowlingball) * (1 - math.exp((-math.sqrt(mass_bowlingball * gravity_bowlingball_jupiter * c) / mass_bowlingball) * time_bowlingball))

# Display the results
print(f"The inner value of c for the bowlingball on earth is: {c_bowlingball:.3f}")
print(f"The velocity of the bowlingball on Earth after {time_bowlingball} seconds is: {velocity_bowlingball_earth:.3f} m/s")
print(f"The velocity of the bowlingball on Jupiter after {time_bowlingball} seconds is: {velocity_bowlingball_jupiter:.3f} m/s")

print("")
print('''#######################################################################################################
#######################################################################################################''')
print("")
