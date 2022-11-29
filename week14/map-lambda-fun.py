# Fun with list comprehensions, map, and for loops


# Here are two lists
a = [10, 11, 12, 13, 14]
b = [5, 4, 3, 2, 1]

# Task: Create a new list, c, that contains
# [5, 7, 9, 13]
# that is [10-5, 11-4, 12-3, 13-2, 14-1]

###############
## FOR LOOPS ##
###############

# one option
c1 = []
for i in range(len(a)):
    c1.append(a[i] - b[i])

# another option: create a function and apply that
def subtract(x, y):
    return x-y

c2 = []
for i in range(len(a)):
    c2.append(subtract(a[i], b[i]))

# third option: use zip
c3 = []
for i,j in zip(a,b):
    c3.append(i-j)
    # or c3.append(subtract(i,j))


#########################
## LIST COMPREHENSIONS ##
#########################

c4 = [i-j for i,j in zip(a,b)]

c5 = [subtract(i,j) for i,j in zip(a,b)]


####################
## MAP AND LAMBDA ##
####################

c6 = list(map(lambda i,j : i-j, a, b))

c7 = list(map(subtract, a, b))

c8 = list(map(lambda i,j : subtract(i,j), a, b))


print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)
print(c7)
print(c8)


#####################
## upper() example ##
#####################

# make a lowercase version of this list
x = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]


# for loop
x1 = []
for w in x:
    x1.append(w.lower())
print(x1)


# list comprehension
x2 = [w.lower() for w in x]
print(x2)


# map
# note that you have to say str.lower !
# why? because lower() is a function called by a string
x3 = list(map(str.lower, x))
print(x3)


# map and lambda (silly though)
x4 = list(map(lambda w: w.lower() , x))
print(x4)


###################
## pow() example ##
###################

mylist = [1, 2, 3, 4, 5]

# for loop
l1 = []
for i in mylist:
    l1.append(i*i)
print(l1)

l1 = []
for i in mylist:
    l1.append(i**2)
print(l1)

l1 = []
for i in range(1,6):
    l1.append(pow(i,2))
print(l1)


# list comprehension

l2 = [i*i for i in mylist]
print(l1)

l2 = [i**2 for i in mylist]
print(l2)

l2 = [i**2 for i in range(1,6)]
print(l2)

l2 = [pow(i,2) for i in mylist]
print(l2)


# map

l3 = list(map(pow, mylist, [2, 2, 2, 2, 2]))
print(l3)


# map and lambda

l4 = list(map(lambda x: x*x, mylist))
print(l4)

l4 = list(map(lambda x: x**2, mylist))
print(l4)

# silly since you are callng a specific function inside your lambda
l4 = list(map(lambda x: pow(x,2), mylist))
print(l4)

l4 = list(map(lambda x: x*x, range(1,6)))
print(l4)



