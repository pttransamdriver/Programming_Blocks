# Import the datetime library to be able to use it:
import datetime
# Set a variable for the current date 
current_date = datetime.datetime.now()
# Print the current date
print(current_date)

# To make this cleaner you can import only a portion of the datetime library: 
from datetime import datetime , timedelta
# Then your varable definition will be simpler
today = datetime.now()
yesterday = datetime.today() - timedelta(days=1)
next_week = datetime.today() + timedelta(weeks=1)
# and print the same thing
print(today)
# Let's stack some of out learning from the Variables and Strings lessons and add the 'f' operator
print(f"The current date is {current_date}")
print(f"The current date is {today}")
print(f"Yesterday was: {str(yesterday)}")
print(f"Next week is: {str(next_week)}")
print(f"The more readable today: {str(current_date.month)}/{str(current_date.day)}/{str(current_date.year)}")
print(f"The more readable Next Week: {str(next_week.month)}/{str(next_week.day)}/{str(next_week.year)}")


# Let's do something with this. Ask the user for a birthday and format it
bday = input("when is your birthday in mm/dd/yyyy?: ")
# Now use the 'strip time' function to pull the Month, Day and Year out of the sring so we can manipulate it with the datetime function
bday_date = datetime.strptime(bday, "%m/%d/%Y")
print(f"Your Birthday is {bday_date}")
bday_eve = bday_date - timedelta(days=1)
print(f"The day before your birthday is {bday_eve}")

