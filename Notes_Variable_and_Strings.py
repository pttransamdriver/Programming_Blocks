# Declares 'first_name' variable to be "Dan"
first_name = "dan"
# Declares 'last_name' variable to be "Druff"
last_name = "druff"

# Prints Variable 'first_name'
print (first_name)
# Prints variable 'last_name'
print (last_name)

# Prints 'first_name' and 'last_name' with no spaces
print (first_name + last_name)

# Prints 'first_name' and 'last_name' with spaces
print (first_name + " " + last_name)

# Prints "Hello 'first_name' 'last_name'" without spaces
print ("Hello" + first_name + last_name)

# Prints "Hello 'first_name' 'last_name'" with spaces
print ("Hello " + first_name + " " + last_name)

# Prints "Hello 'first_name' 'last_name'" with spaces and capitalizes the first letter of each
print ("Hello " + first_name.capitalize() + " " + last_name.capitalize())


# Asks for user input for name1 and name2 to define name1 and name2 as varables to use in the subsiquent code
name1 = input("Please enter your first name: ")
name2 = input("Please enter your last name: ")

# Prints "Hello, 'name1' 'name2'" with spaces and capitalizes the first letter of each
print("Hello, "+name1.capitalize()+" "+name2.capitalize())
# Prints "Hello, 'name1' 'name2'" with spaces and capitalizes the first letter of each using the 'f' operator
print(f"Hell0, {name1.capitalize()} {name2.capitalize()}")
# When using the 'f' operator the spaces are actualy visible in output

############################################################
#############   Strings and variable notes   ###############
############################################################
# Here are five examples of using f-strings in Python:

# Displaying a variable:
name = "John"
print(f"My name is {name}")
# This will output My name is John.

# Formatting numbers:
x = 3.14159
print(f"Pi is approximately {x:.2f}")
# This will output Pi is approximately 3.14.

# Mathmatical expressions:
a = 5
b = 10
print(f"{a} + {b} = {a + b}")
# This will output 5 + 10 = 15

# Using function calls:
import datetime
now = datetime.datetime.now()
print(f"The current date and time is {now}")
# This will output something like The current date and time is 2021-11-15 12:34:56.789012

# String formatting and concatenation
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old")
# This will output My name is John and I am 30 years old