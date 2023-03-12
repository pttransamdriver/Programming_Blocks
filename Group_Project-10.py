"""
File: Group_project-09.py
Author: Tim Illguth
Purpose: Make syncing lists
"""
# Define Bank accounts and balances variables as lists
bank_accounts = []
balances = []

# Print the introduction
print("Hello user, we are going to try some bank account syncing")
print("Please enter the different accounts you have and their respective balanaces")

# Start the first while loop that will populate the 'bank_accounts' and 'balances' 
while True:
    account_name = input("Please enter an account name and 'quit' when done: ").lower()
    if account_name == "quit":
        break
    balance = float(input(f"Please enter your {account_name} balance: "))
    bank_accounts.append(account_name)
    balances.append(balance)

sum_of_accounts = sum(balances)
average_balance = sum_of_accounts / len(balances)
largest_balance = balances.index(max(balances))
max_account_nme = bank_accounts[largest_balance]
print()
print("Here are your Accounts: ")
for x in range(len(bank_accounts)):
    print(f"{bank_accounts[x]} - ${balances[x]:.2f}")

print(f"Your lagest account is: '{max_account_nme}' with ${balances[largest_balance]:.2f}")
print(f"The total balance is ${sum_of_accounts:.2f}")
print(f"The average amount in the accounts is ${average_balance:.2f}")

but_wait_theres_more = input("Would you like to update any of the accounts? (yes/no)").lower()

while but_wait_theres_more == "yes":
    account_update = input("Which account would you like to update? ").lower()
    if account_update in bank_accounts:
        index_of_account = bank_accounts.index(account_update)
        new_balance = float(input(f"Please enter the new balance for {account_update}: "))
        balances[index_of_account] = new_balance
        sum_of_accounts = sum(balances)
        average_balance = sum_of_accounts / len(balances)
        largest_balance = balances.index(max(balances))
        max_account_nme = bank_accounts[largest_balance]
        print()
        print("Here are your Accounts: ")
        for x in range(len(bank_accounts)):
            print(f"{bank_accounts[x]} - ${balances[x]:.2f}")
        print(f"Your largest account is: '{max_account_nme}' with ${balances[largest_balance]:.2f}")
        print(f"The total balance is ${sum_of_accounts:.2f}")
        print(f"The average amount in the accounts is ${average_balance:.2f}")
        but_wait_theres_more = input("Would you like to update any other accounts? (yes/no)").lower()
    else:
        print(f"{account_update} is not a valid account name.")
        but_wait_theres_more = input("Would you like to try again? (yes/no)").lower()

print("Thank you for using python bank balancer. Now go use mint, it's waaaay better. ") 

