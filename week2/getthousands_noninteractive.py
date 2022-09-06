# getthousands_noninteractive.py

### To run this program, go to Run-> Run... Customized ###
### Then enter the integer you want to test in the box ###

# This is called importing a library.
# The sys library lets us read command line arguments.
import sys

# Here's how I get the first command line argument.
# You can memorize this syntax for now.
# To get the first actual argument, you need to use index 1.
myint = sys.argv[1]

# Here's how to get the thousands place mathematically.
option1 = (int(myint) // 1000) % 10

# Here's how to do it using string indexing.
option2 = myint[-4]

# Printing out both.
print("The thousands place is: ", option1) # mathematical operations
print("The thousands place is: ", option2) # string indexing

