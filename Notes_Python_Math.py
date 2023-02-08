# Declares varible 'pi' to be 3.1415
pi = 3.1415
# Prints declaired variable 'pi'
print (pi)



## Math operators translations:
# + Addition
# - Sutraction
# * Multiplecation
# / Division
# ** Exponents

#Declairs the first_num variable to be 4
first_num = 4
#Declares the second_num variable to b 2
second_num = 2

# Prints addition of 'first_num' and 'second_num'
print(first_num+second_num)
# Prints subtraction of 'second_num' from 'first_num'
print(first_num-second_num)
# Prints multiplecation of 'first_num' and 'second_num'
print(first_num*second_num)
# Prints 'first_num' raised to the power of 'second_num'
print(first_num**second_num)

#########################################################################################################

# Type Conversion Example: 
# If I put a number and a string(word or words) together in the same line like this: 
# print(first_num + "days till the weekend") Python doesn't know how to add numbers to words and breaks
# You need to use 'str' to tell python "hey, treat the variable 'first_num' (which is the number 4 in this example) as a string.
# 'str' basically says treat the variable or number as a string. 

# Here it is in practice: 
# Declare Variable:
days_till_the_weekend = 4
print(str(days_till_the_weekend)+" Days till the weekend and I can hardly wait! ")


# When you declare a variable with quotes, that is a number it's seen as a string(word or words)
str_num1 = '4'
str_num2 = '5'
# If you try to apply the math the sam as above you actaully get the two numbers printed next to each other
print(str_num1+str_num2)
# So if you use the 'input' function the number will always return as a string
str_num3 = input("Enter a number: ")
str_num4 = input("Enter another number: ")
print(str_num3+str_num4)

# So how do you use the strings from the input as math? 
# For this you use 'float' (why it's called that I have no idea) or the more aptly named 'int' for integer. 
print(int(str_num3)+int(str_num4))
# or
print(float(str_num3)+float(str_num4))
# 'int' will only work for whole numbers. For decimals like 3.1415 you'll need to use 'float' 

#############################################################################################################