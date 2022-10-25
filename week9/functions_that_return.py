# Calling functions that return something:
# You have to *do* something!
# What are some options?

mylist = [2, 8, 3, 4, 2, 10]

def myfunc(s1):
    return s1 + " there!"

# print it out
print(len(mylist))
print(myfunc("hello"))

# save it to a variable
mylist_length = len(mylist)
mynewstring = myfunc("hello")

# compare it to something else
if len(mylist) < 10:
    print("This is a short list!")

if "!" in myfunc("hello"):
    print("Yay!!!")

# do some operation on it
newi = len(mylist) + 45
news = myfunc("hello") + "?!?!?!"

# call another function on it
words = myfunc("hello").split()

# pass it in as an argument to another function
print(len(myfunc("hello")))



