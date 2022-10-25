import random

# here's the range of numbers to try to guess
low = 1
high = 100

# select a random number to try to guess
guessme = random.randint(low,high)
print("Shh... the secret number is", guessme)

# take your first guess, halfway between the top
# and the bottom of the range
myguess = (high+low)//2
print("I am guessing", myguess)

# while your guess is wrong...
while myguess != guessme:

    # the computer will tell you if it's too big or too small

    # if it's too small, you can throw out the low end of
    # the range by resetting low to your guess plus 1
    if myguess < guessme:
        print("your guess is too small")
        low = myguess+1

    # if it's too big, you can throw out the high end of
    # the range by resetting high to your guess minus 1
    if myguess > guessme:
        print("your guess is too big")
        high = myguess-1

    # make a new guess halfway in the new range
    myguess = (high+low)//2
    print("\nNow I am guessing", myguess)

print("Yay, your guess was finally right!")

    
