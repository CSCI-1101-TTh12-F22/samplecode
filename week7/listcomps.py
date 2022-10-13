### List comprehension examples from class on 7.2 with months

months = ["January", "February", "March", "April",
          "May", "June", "July", "August", "September",
          "October", "November", "December"]

# Create list of uppercase months with a for loop
newmonths = []
for m in months:
    newmonths.append(m.upper())
print(newmonths)

# Create list of uppercase months with list comprehension
newmonths = [m.upper() for m in months]
print(newmonths)

# Create list of A and J months with a for loop
newmonths2 = []
for m in months:
    if m[0] == "A" or m[0] == "J":
        newmonths2.append(m)
print(newmonths2)

# Create list of A and J months with a list comprehension
newmonths2 = [m for m in months if m[0] == "A" or m[0] == "J"]
print(newmonths2)

# for fun, put these back together into a single string

print(" ".join(newmonths2))



### Other list comprehension examples.

# Make a list containing the square of each integer
# between 0 and 5.

# for loop
squares = []
for i in range(6):
    squares.append(i*i)
print(squares)

# list comprehension
squares = [i*i for i in range(6)]
print(squares)


# Generate a list containing 15 random integers
# between -10 and 10.
import random

# for loop
randos = []
for i in range(15):
    randos.append(random.randrange(-10, 10))
print(randos)

# list comprehension
randos = [random.randrange(-10, 10) for i in range(15)]
print(randos)


# Create a new list from the above where positive integers
# stay the same but negative integers are replaced with 0.

# for loop
randoextra = []
for i in randos:
    if i > 0:
        randoextra.append(i)
    else:
        randoextra.append(0)
print(randoextra)

# list comprehension
randoextra = [i if i>0 else 0 for i in randos]
print(randoextra)
