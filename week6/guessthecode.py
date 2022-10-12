import random

### generate a random 3-letter code with ABCD
def generate_code():
    # possible letters in a code
    letters = "ABCD"

    # start off with an empty code
    mycode = ""

    # a code has three letters
    for i in range(3):

        # select a random letter from set of possible letters
        lett = letters[random.randint(0,3)]

        # add it to the random code
        mycode = mycode + lett

    return mycode

### guess a random 3-letter code with ABCD
def guess_the_code(the_code):

    # start off with empty guess and 0 guesses
    guesscode = ""
    guesses = 0

    # nested for loops!
    # go through each possibility for the first letter,
    # the second, the third letter...
    for i in "ABCD":
        for j in "ABCD":
            for k in "ABCD":
                guesses += 1

                # make a guess
                guesscode = i + j + k

                # if you guess right, return the number of guesses!
                if guesscode == the_code:
                    return (guesses)

    # if you got all the way through without guessing correctly
    # return an error code, -1
    return -1

#  main method
def main():

    # TRY TO GUESS THE CODE VIA BRUTE FORCE
    # Let's do in 1000 times and see how long
    # it takes us on average to crack the code

    totalguesses = 0

    for i in range(1000):
        mycode = generate_code()
        totalguesses += guess_the_code(mycode)
 
    print("On average, it takes {} guesses to crack the code".format(totalguesses/1000))
                
main() 

