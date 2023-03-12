"""
File: Prove-09.py
Author: Tim Illguth
Purpose: Shopping Cart Program
"""

print("#####################################################################################")
print("#######################  Welcome to Python shopping cart  ###########################")
print("#####################################################################################")
print("What would you like to do?")
print("Please choose from the following options:")

# Define the 'menu' variable to be a list of the user's choices
menu = ["1. Add Item\n" "2. View Cart\n" "3. Remove Item\n" "4. Compute Total\n" "5. Done/Quit"]

# Define dictionaries (a thing that like a list but indexable) for the cart and associated costs
cart = {}
cost = {}

# Start a while loop to get the shopping cart app started 
while True:
    # Print the 'menu' list using the 'join()' function so that the '\n' are treated as special characters 
    # and not just part of the strings
    print("".join(menu))

    # Ask the user for the item to add
    choice = input("Please enter a choice 1-5: ")

    if choice == "1":
        # Introduce variable 'item_add' that is user defined in the input
        item_add = input("What would you like to add to your cart?: ")
        # Ask the user how much the item costs (bad business practice)
        # using a float variable so the user can enter decimals
        item_cost = float(input("Please enter the cost of the item: "))

        # If the 
        if item_add in cart:
            cart[item_add] += 1
        
        else:
            # List the 'item_add' into the cart dictionary with the associated index number
            cart[item_add] = 1  #could be any number
            # associate the added item with the added cost and place it in the 'cost' list
            cost[item_add] = item_cost

    
    #Prints out the cart contents
    elif choice == "2":
        print("########## Cart contents: #############")
        # Using a for loop to read through the dictionaries. Since I couldn't find
        # another way to do so (shug). The items() function takes the two 
        # direcotries cost and cart and combines them into a list of tuples.
        # tuples are orderes pairs that are normally immutable but are editable
        # in lists. 
        for item, quantity in cart.items():
            print(f"{quantity} {item} - ${cost[item]*quantity:.2f}")
        print("#######################################")

    
    elif choice == "3":
        # Define the item to take from the cart
        item_take = input("What item would you like to remove from your cart?: ")
        if item_take in cart:
            # .pop() functions are for removing items from directories
            # This removes the user defined 'item_take' from the directory and 
            # it's associated cost. which is pretty dang cool actually
            cart.pop(item_take)
            # Removes the assiciated cost using 'item_take' for an index
            cost.pop(item_take)
        else:
            print("That item isn't in your cart. Please choose again")
    
    # Boring, just prints the cart contents
    elif choice == "4":
        # Uses 'values()' to pull the associated numerarical values from the
        # costs direcotry and prints it. 
        #sub_total = sum(cost.values()) 
        print(f"Your subtotal so far is: ${sum(cost.values()):.2f}")

    elif choice == "5":
        print("Thanks for using python cart")
        print(f"Your total comes to ${sum(cost.values()):.2f}")
        # Yes, yes this is a copy paste from choice 2. shhh
        for item, quantity in cart.items():
            print(f"{quantity} {item} - ${cost[item]*quantity:.2f}")
            # Add a flairwell with a moose ACSII 
            print("Have a moose't wonderful day! :D ") 
            print(" ___            ___")
            print("/   \          /   \ ")
            print("\_   \        /  __/ ")
            print(" _\   \      /  /__ ")
            print(" \___  \____/   __/ ")
            print("     \_       _/ ")
            print("       | @ @  \_ ")
            print("       |         ")
            print("     _/     /\   ")
            print("    /o)  (o/\ \_ ")
            print("    \_____/ /    ")
            print("      \____/     ")
        break
    else:
        print("Please make a valid numarical selection")

