# changing a string does not change it outside the function
# strings are passed by value
def updatestring(s1):
    s1 = s1 + "!!!"
    print("Here's what the string looks like in the function:", s1)

# reassigning a string does not change it outside the function
# strings are passed by value
def updatestring2(s1):
    s1 = "hey there"
    print("Here's what the string looks like in the function:", s1)


def main():

    # mystring does not change after you
    # pass it in as an argument to the function.
    # strings are passed by value
    mystring = "foo"
    print("Here is the string before calling updatestring() " + mystring)
    updatestring(mystring)
    print("Here is the string after calling updatestring(): " + mystring)
    print()
    print("Here is the string before calling updatestring2(): " + mystring)
    updatestring2(mystring)
    print("Here is the string after calling updatestring2(): " + mystring)

main()
