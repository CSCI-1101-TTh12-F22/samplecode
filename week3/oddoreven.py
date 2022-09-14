# This function determines whether a number is odd or even.
# The parameter, n, should be an int.
def oddeven(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")


# Here is the main() function definition.
# It asks the user to enter a number.
# Then it calls the oddeven() function.
def main():

    # Converting input to an int since odd/even is an int thing.
    mynumber = int(input("Enter an integer: "))

    # Calling my function.
    oddeven(mynumber)

# Here's where I run the main() function.
main()
