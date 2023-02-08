# Greet the user
print("Hello, Welcome to Python Burger. I'll total up your meal price of your imaginary meal for you")

# Ask for the User defined variables
child_meal = float(input("What is the price of a children's meal you would like?: "))
adult_meal = float(input("What is the price of an Adult meal you would like?: "))
kid_num = int(input("How many chidlren will be getting the chosen meal?: "))
adult_num = int(input("How many adults will be getting the chosen meal?: "))
tax_rate = float(input("What is your sales tax rate?: "))

# Start doing that math and print out the required fields
subtotal = (child_meal*kid_num)+(adult_meal*adult_num)
print(f"The subtotal is: ${subtotal:.2f}")
sales_tax = subtotal*(tax_rate/100)
round_sales_tax = round(sales_tax, 2)
print(f"The sales tax is: ${round_sales_tax:.2f}")
total = subtotal+sales_tax
round_total = round(total, 2)
print(f"The Total cost of your meal is: ${round_total:.2f}")
payment = float(input("What is your payment amount?: "))  
change = payment-total
round_change = round(change, 2)


# Add some flair and sarcasm with an if then statment
print(f"The total change is $ {round_change:.2f} ")
donate = input("would you like to donate your change? (yes/no): ").lower()
if donate == "yes":
    print("Sucker, I'm keeping this!")
elif donate == "no":
    print("Correct Answer!")
else:
    print("I'll put you down for a no.")
print("Thanks for shopping at Python burger! Don't have a good day, have a great day! ")

