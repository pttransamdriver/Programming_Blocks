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
    # Print the 'menuu' list using the 'join()' function so that the '\n' are treated as special characters 
    # and not just part of the strings
    print("".join(menu))

    # Ask the user for the item to add
    choice = input("Please enter a choice 1-5: ")

    if choice == "1":
        item_add = input("What would you like to add to your cart?: ")
        # Ask the user how much the item costs (bad business practice)
        item_cost = float(input("Please enter the cost of the item: "))
        if item_add in cart:
            cart[item_add] += 1
        
        else:
            # List the 'item_add' into the cart dictionary with the associated index number
            cart[item_add] = 1  #could be any number
            # associate the added item with the added cost and place it in the 'cost' list
            cost[item_add] = item_cost

    
    #Prints out the cart contents
    elif choice == "2":
        print("#######################################")
        print("########## Cart contents: #############")
        print(", ".join(cart))
        print("#######################################")

    
    elif choice == "3":
        item_take = input("What item would you like to remove from your cart?: ")
        if item_take in cart:
            # .pop() functions are for adding and removing items from directories
            # This removes the user defined 'item_take' from the directory and 
            # it's associated cost. which is pretty dang cool actually
            cart.pop(item_take)
            cost.pop(item_take)
        else:
            print("There are not items in your cart")
    
    # Boring, just prints the cart contents
    elif choice == "4":
        # Uses 'values()' to pull the associated numerarical values from the direcotry 
        sub_total = sum(cost.values()) 
        print(f"Your subtotal so far is: ${sub_total:.2f}")
    elif choice == "5":
        break
    else:
        print("Please make a valid numarical selection")

