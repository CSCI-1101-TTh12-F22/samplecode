# tuples

thing1 = "a"
thing2 = "a",
thing3 = ("b",)
print(type(thing1))  # will be string
print(type(thing2))  # will be tuple because of comma!
print(type(thing3))  # will be tuple - parens are optional

# empty tuples
tup1 = ()
tup2 = tuple()

# different from empty lists!
list1 = []
list1 = list()

# making a tuple
student1 = ("George", 2021, 3.4)
student2 = ("Martha", 2022, 3.9)

# accessing elements in a tuple
print("Name: ", student1[0])
print("Year of graduation: ", student1[1])

# you cannot change elements in a tuple!
# student1[2] = 3.1  # tuples are immutable

# but you can change elements in a list
mylist = [1, 2, 3, 4]
mylist[2] = 7

# looping through a tuple
for z in student1:
    print(z)

# other functions
len(student1)


# when you return more than one thing in a function
# you are returning a tuple

def myfun(x, y):
    mysum = x+y
    myprod = x*y
    return mysum, myprod

# you can save out what gets returned as two separate variables
s, p = myfun(10,3)

# or you can save it to a single variabl that is a tuple
stuff = myfun(10,3)

print(s, stuff[0])
print(p, stuff[1])


