# These functions demonstrate how while loops work
# properly instead of that weird running thing in the reading!

# Force the user to enter an even number.
def evennum():
    number = int(input("Enter an even number: "))
    while number % 2 != 0:
        number = int(input("Try again. Enter an even number: "))
    print("Thank you for entering an even number.")


# Wish someone a happy birthday as many times as they specify.
def happbday():
    number = int(input("How many times? "))
    counter = 0
    while counter < number: 
        print("Happy birthday!")
        counter = counter + 1

# Version 2
def happbday2():
    number = int(input("How many times? "))
    counter = 0
    while counter != number: 
        print("Happy birthday!")
        counter = counter + 1

# Version 3
def happbday3():
    number = int(input("How many times? "))
    counter = 1
    while counter <= number: 
        print("Happy birthday!")
        counter = counter + 1

# Version 4
def happbday4():
    number = int(input("How many times? "))
    counter = number
    while counter > 0: 
        print("Happy birthday!")
        counter = counter - 1


# Make the user try to guess your number and don't
# stop till they get it right.
def guessmynumber():
    mynumber = 7
    guess = int(input("Guess my number between 1 and 10: "))
    while guess != mynumber:
        guess = int(input("Nope! Guess my number between 1 and 10: "))

    print("Great job! You guessed my number, which was", mynumber)

def main():
    evennum()
    print()
    happbday()
    print()
    happbday2()
    print()
    happbday3()
    print()
    happbday4()
    print()
    guessmynumber()
    


main()
