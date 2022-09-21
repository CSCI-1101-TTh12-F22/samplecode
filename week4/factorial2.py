# range with one argument
def factorial1(n):
    facnum = 1
    for i in range(n):
        facnum *= (i+1)
    print(facnum)

# range with two argument
def factorial2(n):
    facnum = 1
    for i in range(1, n+1):
        facnum *= i
    print(facnum)

# range with three arguments
def factorial3(n):
    facnum = 1
    for i in range(n, 0, -1):
        facnum *= i
    print(facnum)

# a nice main function to run all our functions
def main():
    factorial1(6)
    factorial2(6)
    factorial3(6)

# don't forget to call main()
main()
