
name = "Tristan"
age = 75
color = "blue"


## FANCY PRINTING!
# Basic print: commas between each argument to print
# print() by default separates them with a space and adds a new line
print(name, "is", age, "years old and his favorite color is", color)

# Here, you create a string by concatenating the parts with + operator.
# You need to insert the spaces between components yourself.
# And you need to convert non-strings to strings.
print(name + " is " + str(age) + " years old and his favorite color is " + color)

# print() inserta a new line at the end by default.
# You can suppress that by using the end="" option.
# You can add in your own new line with the special character "\n"
print(name, "is", age, "years old and his favorite color is", color, "\n", end="")

# print() connects elements with a space by default.
# You can suppress that (or use a different separator) using the sep= option.
print(name, " is ", age, " years old and his favorite color is ", color, sep="")

# Getting fancy with f-strings()
# More on this on Thursday.
print(f"{name} is {age} years old and his favorite color is {color}")


## WRITING OUT TO A FILE

# Here we are using the open() function to *write* out to a file.
# The "w" option tells open() we want to write output (rather than read in input).
g = open("myoutput.txt", "w")

# Let's open our excerpt of Great Expectations
with open("greatexpectations.txt") as f:

    # And for each line in P&P...
    for line in f:

        # let's write out that line in a different way to the file
        # stored with our file object g
        g.write(line.upper())

# don't forget to close the file!
g.close();
    
