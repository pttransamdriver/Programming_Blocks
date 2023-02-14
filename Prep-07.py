"""
File: Prep-07.py
Author: Tim Illguth
Professor: Gabriel Haynie
Purpose: Amusement park ride requirements.
"""

# Enter a orientation text to instruct the user what to do:
print("")
print("################################################################################################")
print("######################   Hello User, this program checks positive numbers  #####################")
print("################################################################################################")
print("")

# Defines the variable 'number' 
number = int(input("Please enter a positive number: "))

while number < 0:
    print("""################################################################################################""")
    print("    *****You have entered a negative number ***** ")
    print("""################################################################################################""")
    print("")
    number = int(input("Let's Try that again: What's the number?: "))

print("")
print("""################################################################################################""")
print("    *****You have entered a positive number ***** ")
print("""################################################################################################""")
print("")
print(f"You have entered the positive number '{number}'")



# Enter a orientation text to instruct the user what to do:
print("")
print("################################################################################################")
print("###################   Now, let's pretend the program becomes a spoiled brat!  ##################")
print("################################################################################################")
print("")

# Defines the variable 'number' 
candy = input("Can I have a peice of candy? ").upper()

if candy != "YES":
    print("PLEEEEEEEEEEESE! ")
    candy = input("I'll really want one: ").upper()

if candy != "YES":
    print("PLEEEEEEEEEEESE! ")
    candy = input("I promise to not make a mess?: ").upper()
if candy != "YES":
    print("PLEEEEEEEEEEESE! ")
    candy = input("What word do you get you take the first 'e' off the word eyes?: ").upper()

if candy != "YES":
    print("PLEEEEEEEEEEESE! ")
    candy = input("I promise to not get a cavity this time...?: ").upper()

while candy != "YES":
    print("PLEEEEEEEEEEESE! ")
    candy = input("Please? Please? can I have one? can I have one? : ").upper()

else: print("Thank you!")
