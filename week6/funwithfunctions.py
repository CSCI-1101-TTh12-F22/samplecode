

###################################
### VOID VS. NOT VOID FUNCTIONS ###
###################################

# print the area of a triangle
def triarea(b, h):
    area = (b*h) / 2
    print(area)

# *return* the area of a triangle
def triarea2(b, h):
    area = (b*h) / 2
    return area


#####################################
### FUNCTIONS RETURNING ONE VALUE ###
#####################################


## Return an int
# return the length of a string
# (obviously a silly function to write :)
def stringlength(s1):
    return len(s1)

## Return a float
# return the average length of three strings
def averagelength(s1, s2, s3):
    average = (len(s1) + len(s2) + len(s3))/3
    return average

## Return a string
# return backwards version of a string
def backwards(s1):
    s2 = ""
    for i in s1:
        s2 = i + s2
    return(s2)

## Return a bool (three options)

# return true if it's a palindrome
# option 1: if/else
def palindrome(s1):
    s2 = backwards(s1)
    if s1 == s2:
        return True  # this will terminate the function
    return False

# option 2: if only
def palindrome2(s1):
    s2 = backwards(s1)
    if s1 == s2:
        return True
    else:
        return False

# option 3: just return the condition itself
def palindrome3(s1):
    s2 = backwards(s1)
    return s1 == s2  # s1==s2 has a boolean value: True or False!


###########################################
### FUNCTIONS RETURNING MULTIPLE VALUES ###
###########################################

# return the sum and the product of two numbers
def getinfo(a, b):
    return (a+b), (a*b)


# return backwards version of a string *plus* its length
def backwards2(s1):
    s2 = ""
    for i in s1:
        s2 = i + s2
    return(s2, len(s2))


# return the average length of three strings
# plus the length of the longest string
def averagelength_and_max(s1, s2, s3):
    average = (len(s1) + len(s2) + len(s3))/3
    maxlen = len(s1)
    if len(s2) > maxlen:
        maxlen = len(s2)
    if len(s3) > maxlen:
        maxlen = len(s3)
    return average, maxlen


############
### MAIN ###
############

# testing out the above functions
def main():

    base = 10
    height = 5

    # does not save out area
    print(triarea2(base, height))

    # does save out the area!
    myarea = triarea2(base, height)
    print(myarea)

    # get backwards string
    newstring = backwards("tree")
    print(newstring)

    # average string length
    avlen = averagelength("dog", "banana", "computer")
    print(avlen)

    # palindrome check
    yesorno = palindrome("bob")
    print(yesorno)


    # showing how boolean function are cool!
    word = input("Keep entering palindromes, please: ")

    # palindrome returns True or False, so you can use it as a condition!    
    while palindrome(word):
        word = input("Keep entering palindromes, please: ")
    print("Thanks for all those palindromes!")
 

    # showing how to get values back from a function that 
    # returns multiple values
    s, p = getinfo(10, 5)
    print(s, p)

    avlen, maxlen = averagelength_and_max("dog", "banana", "computer")
    print(avlen, maxlen)

    
main()
    
