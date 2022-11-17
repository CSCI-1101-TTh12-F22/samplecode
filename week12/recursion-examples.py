#######################
## GET STRING LENGTH ##
#######################

# iterative: add 1 for each character you go
# through in a for/each loop
def getlengthI1(s):
    mylen = 0
    for i in s:
        mylen += 1
    return mylen

# iterative: add 1 for each character you
# rip off the front of the string until the
# string is empty
def getlengthI2(s):
    mylen = 0
    while s != "":
        s = s[1:]
        mylen += 1
    return mylen

# recursive: we know an empty string has length 0
# so keep calling the function on less and less of
# the stringuntil you get to the empty string
def getlengthR(s):
    if s == "":
        return 0
    return 1 + getlengthR(s[1:])


#########################
## CALCULATE FACTORIAL ##
#########################

# iterative: start with one and keep
# multiplying by larger and larger
# numbers until you get to n
def factorialI(n):
    tots = 1
    for i in range(n):
        tots *= i+1
    return tots

# recursive: we know 1! = 1, so
# keep calling the function on 1 less than
# the currebt number until you get to 1.
def factorialR(n):
    if n == 1:
        return 1
    return n * factorialR(n-1)


####################
## REVERSE STRING ##
####################

# iterative: chop off the first letter, then
# attach it to the end of the new string
# and keep doing that until you run out of letters
def reversestringI(s):
    news = ""
    while len(s) > 0:
        news = s[0] + news
        s = s[1:]
    return news

# recursive: the reverse of a string of length 1
# is just itself, so that's your basecase. Keep
# calling the function on what remains after you chop
# off the first letter
def reversestringR(s):
    if len(s) <= 1:
        return s
    return reversestringR(s[1:]) + s[0]


# main() method to test out the functions
def main():
    print(getlengthI1("elephant"))
    print(getlengthI2("elephant"))
    print(getlengthR("elephant"))

    print(factorialI(5))
    print(factorialR(5))

    print(reversestringI("elephant"))
    print(reversestringR("elephant"))

main()


