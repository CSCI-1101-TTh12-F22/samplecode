# These functions demonstrate how for loops can be
# used to do some of the functionality of while loops.

# Print "happy birthday" as many times as the user requests.

# First with a while loop
def bday():
    bdaynum = int(input("How many times? "))
    counter = 1
    while counter <= bdaynum:
        print("Happy birthday")
        counter = counter + 1

# Second with a for loop
def bday2():
    mynum = int(input("How many times "))
    for i in range(mynum):
        print(i)
        print("Happy birthday!")

# Third with a for loop, but where you set the
# number of times in the main() function and
# then pass it in as an argument when you call bday3
def bday3(mynum):
    for i in range(mynum):
        print("Happy birthday!")

########################

# Calculate n!

# for loop:
def myfactorial(n):
    facn = 1
    for i in range(n):
        print(i)
        facn = facn * (i+1)
    print(facn)

# while loop
def myfactorial2(n):
    facn = 1
    while n > 0:
        facn = facn * n
        n = n-1
    print(facn)

########################


# Two different ways to print out
# each character in a string with a for loop.

def printchar(s):
    for i in range(len(s)):
        print(i, s[i])

def printchar2(s):
    for c in s:
        print(c)

########################


# Use a while loop (for now) to print out the
# characters of a string backwards.
# (More on how to do this with for loop next week)
def printbackwards(s):
    counter = len(s) - 1
    while counter >= 0:
        print(s[counter])
        counter = counter - 1


##################

# Function definitions go *outside* main
# Call to main() goes *outside* main
# All other code for now should go *inside* main
def main():
    bday()
    print()
    bday2()
    print()
    bday3(5)
    print()

    myfactorial(5)
    print()
    myfactorial2(5)
    print()

    printchar("tomato")
    print()
    printchar2("tomato")
    print()
    printbackwards("tomato")


# call main() to make it run!
main()
