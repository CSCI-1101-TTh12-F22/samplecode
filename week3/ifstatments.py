# Some more code to demonstrate if statements

# this function tells you whether a > b or b < a or a==b
def smallerorbigger(a,b):
    if a < b:
        print("a is less than b")
        print(a, "is less than", b)
    elif a > b:
        print("b is less than a")
        print(b, "is less than", a)
    else:
        print("they are the same")
        print(b, "is the same as", a)

# this function checks to see if a is a substring of b
# if b is a substring of a or if neither is s substring of the other
def substringcheck(a, b):
    if a in b:
        print("a is a substring of b")
    elif b in a:
        print("b is a substring of a")
    else:
        print("neither b nor a is a substring of the other")
    print("program complete")


# main method: all your code except the function definitions
# and the call to main() go here!!!
def main():
    smallerorbigger(20, 20)
    print()
    smallerorbigger(15, 20)
    print()
    smallerorbigger(20, 15)
    print()

    substringcheck("cat", "catastrophe")
    print()
    substringcheck("dog", "catastrophe")
    print()
    substringcheck("dog", "dog")

main()

        
