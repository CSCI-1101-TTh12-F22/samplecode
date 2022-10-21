# dictionaries

# empty list
list1 = []
list2 = list()

# empty dictionary
dictionary1 = {}
dictionary2 = dict()

# making a dictionary
numbers = {"un":1, "deux":2, "trois":3, "quatre":4}

# or create an empty one and add to it
numbers2 = {}
numbers2["un"] = 1
numbers2["deux"] = 2
numbers2["trois"] = 3
numbers2["quatre"] = 4

# accessing elements
print(numbers["trois"])

# updating elements
numbers["quatre"] = 5


# looping through a dictionary
for k in numbers:
    print(k, "is", numbers[k])


# or use items to loop through a list of key-value tuples
for k,v in numbers.items():
    print(k, "is", v)


# count the numbers of each character
mystring = "aababbcdddddadcdaabbb"

# option 1,  check if key is already there
# if not, add it to the dictionary.
# otherwise increment the current value by 1
mydictionary = {}
for c in mystring:
    if c in mydictionary:
        mydictionary[c] += 1
        # mydictionary[c] = mydictionary[c] + 1  # also okay
    else:
        mydictionary[c] = 1

print(mydictionary)

# option 2: use the get() functions
mydictionary = {}
for c in mystring:
    mydictionary[c] = mydictionary.get(c, 0) + 1

print(mydictionary)

