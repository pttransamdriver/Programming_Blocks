# Create an empty list to store friends
numbers = []

# Loop until the user types '0' or the program hits 'break'
print("Welcom to python number list maker!")
while True:
    # Ask the user for a number
    number = int(input("Enter a number (type '0' to stop): "))

    # Check if the user typed '0' to exit the loop
    if number == 0:
        # Break the while loop if the user types '0'
        break

    # Append the number to the list
    numbers.append(number)

# Display the list of numbers
print("The numbers you entered are:")

for number in numbers:
    print(number)
average = sum(numbers) / len(numbers)
print(f"The sum of the numbers you entered is {sum(numbers)}")
print(f"The Average of the numbers you entered is {(average)}")
sorted = sorted(numbers)
# Find the smallest positive number
positive_numbers = [x for x in numbers if x > 0]
if positive_numbers:
    smallest_positive = min(positive_numbers)
    print(f"The smallest positive number is {smallest_positive}")
else:
    print("There are no positive numbers in the list.")
print(f"Sorted numbers list is: {sorted}")