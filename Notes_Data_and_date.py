# Import the datetime library to be able to use it:
import datetime
# Set a variable for the current date 
current_date = datetime.datetime.now()
# Print the current date
print(current_date)

# To make this cleaner you can import only a portion of the datetime library: 
from datetime import datetime , timedelta
# Then your varable definition will be simpler
current_date2 = datetime.now()
yesterday = datetime.today() - timedelta(days=1)
# and print the same thing
print(current_date2)
# Let's stack some of out learning from the Variables and Strings lessons and add the 'f' operator
print(f"The current date is {current_date2}")
print(f"Yesterday was: {str(yesterday)}")
print(f"{str(current_date.month)}/{str(current_date.day)}/{str(current_date.year)}")