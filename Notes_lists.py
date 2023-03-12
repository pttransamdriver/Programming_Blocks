"""
Here are some examples of list comprehension in Python that find the absolute value of 
numbers in a list:
"""

# Example 1: Finding the absolute value of each number in a list
# Let's say we have a list of numbers, and we want to create a new list that 
# contains the absolute value of each number in the original list. 
# We can use list comprehension to achieve this like so:

numbers_1 = [-2, 5, -8, 10, -12]
absolute_numbers = [abs(x) for x in numbers_1]
""" 
Here, we are using list comprehension to create a new list called absolute_numbers that 
contains the absolute value of each number in the numbers list. The expression abs(x) computes 
the absolute value of each element x of the original numbers list.
"""
# Example 2: Filtering positive numbers and finding their absolute value

"""
Let's say we have a list of numbers, and we want to create a new list that contains 
only the positive numbers from the original list and the absolute 
value of each of these numbers. We can use list comprehension to achieve this like so:
"""

numbers_2 = [-2, 5, -8, 10, -12]
positive_absolute_numbers = [abs(x) for x in numbers_2 if x > 0]
print(positive_absolute_numbers)

"""
Here, we are using list comprehension to create a new list called 
positive_absolute_numbers that contains the absolute value of each 
positive number in the numbers list. The expression abs(x) computes 
the absolute value of each element x of the original numbers list, 
and the if x > 0 condition filters out any negative numbers 
from the list before applying the abs() function.
"""

# Example 3: Squaring each number in a list
"""
Let's say we have a list of numbers and we want to create a new list that 
contains the squares of each number in the original list. We can use 
list comprehension to achieve this like so:
""" 
numbers_3 = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers_3]
print(squared_numbers)
"""
Here, we are using list comprehension to create a new list called 
squared_numbers that contains the squares of each number in the numbers list. 
The expression x**2 squares each element x of the original numbers list.
"""

#Example 4: Filtering even numbers in a list
"""
Let's say we have a list of numbers and we want to create a new list 
that contains only the even numbers from the original list. 
We can use list comprehension to achieve this like so:
"""
numbers_4 = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers_4 if x % 2 == 0]
print(even_numbers)
"""
Here, we are using list comprehension to create a new list called even_numbers 
that contains only the even numbers from the numbers list. 
The expression x for x in numbers includes each element x of the original numbers list, 
and the if x % 2 == 0 condition only includes the element if it is even.
"""

# Example 5: Calling indicies in the lists
numbers_5 = [5, 10, 15, 20, 25]
# Indexes:   0   1   2   3   4
fruits = ["apple", "banana", "orange", "grape", "pineapple"]
# Indexes:    0       1         2         3          4

# Sync the two lists using the 'zip()' function
for number, fruit in zip(numbers_5, fruits):
    print(f"{number} - {fruit}")


# Interate over a single list 
my_list = ['apple', 'banana', 'cherry']
for i in range(len(my_list)):
    print(f"The element at index {i} is {my_list[i]}")

"""
In this case, the zip() function combines the numbers and fruits lists into a sequence 
of tuples (1, 'apple'), (2, 'banana'), (3, 'cherry'), which we then iterate over using the for loop. 
Inside the loop, we use tuple unpacking to assign the elements of each tuple to the variables number 
and fruit, and then print them out together.

So, in summary, you can use range() to iterate over the indices of a single list, 
and zip() to iterate over two or more lists element-wise.
"""