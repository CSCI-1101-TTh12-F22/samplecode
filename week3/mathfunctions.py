### COOL MATH FUNCTIONS
### SOME DEMONSTRATE IF STATEMENTS
### OTHERS ARE JUST FOR FUN

# This function prints out whether a number is odd or even.
# Argument must be an integer.
def oddoreven(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")

# This function prints out whether a number greater than 10.
# Argument must be numeric.
def biggerthan10(n):
    if n > 10:
        print("bigger than 10")
    elif n < 10:
        print("smaller than 10")
    else:
        print("The number is 10!")

# This function prints out whether a number is +, -, or 0.
# Argument must be numeric.
def posnegzero(n):
    if n > 0:
        print("n is positive")
    elif n < 0:
        print("n is negative")
    else:
        print("n is zero")


        # This function adds 10 to a number.
# Argument should be numeric.
def add10(n):
    print("n starts out as", n)
    n = n + 10
    print("now n is", n)
    n += 10
    print("and now n is", n)


# This function prints out the area of a triangle.
# Arguments must both be numeric: the base and the height.
def trianglearea(base, height):
    area = (base*height)/2
    print("Your triangle has an area of", area)

### MAIN FUNCTION ###   

# Here's my main function that tries out all the above functions.
def main():

    # Get input, turn it into a number.
    a = input("enter a number: ")
    b = int(a)

    # Call the functions.
    oddoreven(b)
    biggerthan10(b)
    posnegzero(b)
    add10(b)
    trianglearea(4, 7)

    # Cool trick!
    # This one line is equivalent to three lines of code above!
    # We "chained" these functions together.
    oddoreven(int(input("enter a number: ")))


    
### CALLING MAIN ###
main()
