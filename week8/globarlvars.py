# demonstrating some global variable

# global variable
myname = "Emily"


def printhi():
    # Python can't find a local variable called myname
    # so it knows I am talking about the global variable.
    print("Hi,", myname)

def printhi2():
    # I might think I am reassigning the global variable
    # but really Python thinks I am creating a local
    # variable that happens to have the same name.
    # This will *not* change the value of the global variable.
    myname = "Prof. Prud'hommeaux"
    print("Hi,", myname)

def printhi3():
    # If I really want to change the value of the global
    # variable, I have to declare that I mean the global
    # variable in this function.
    global myname
    myname = "Prof. Prud'hommeaux"
    print("Hi,", myname)


def main():
    printhi()
    print("Goodbye,", myname)

    printhi2()
    print("Goodbye,", myname)

    printhi3()
    print("Goodbye,", myname)


main()
