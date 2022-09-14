# This function determines whether a number is 
# positive, negative, or 0.
# The parameter, n, is a number (float or int).
def kindofnumber(n):
    if n < 0:
        print("negative")
    elif n > 0:
        print("positive")
    else:
        print("zero")


# Here is the main() function definition.
# It asks the user to enter a number.
# Then it calls the oddeven() function.
def main():

    # I convert the input to float to allow decimal numbers!
    mynumber = float(input("Enter an number: "))

    # Calling my custom function.
    kindofnumber(mynumber)

# Here's where I run the main() function.
main()
