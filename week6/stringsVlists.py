## Strings!

# create a string
mystring = "ding dong call me on my phone ice tea and a game of ping pong"

# print out its length
print(len(mystring))

# print out some characters by index
print(mystring[0])
print(mystring[15])
print(mystring[-1])

# create an uppercase version of the string
# using for/each syntax
newstring = ""
for c in mystring:
    newstring = newstring + c.upper()
print(newstring)

# print out the new string backwards in lowercase 
# using for/range syntax
for i in range(1, len(newstring)+1, 1):
    print(newstring[-i].lower(), end="")
print()


# cool function on strings: split()
# chops string into a *list* of strings
# wherever it sees a space
words = mystring.split()

# another function: put a list back together
back2string = " ".join(words)
print(back2string)

## Lists!

# create a list from scratch
mylist = [7, "W", 4.5, True]
print(mylist)

# add to a list
mylist.append("eleven")
print(mylist)

# access elements of list with indices
print(mylist[0], mylist[-1])

# replace elements of lists
words[0] = "ping"
words[1] = "pong"
print(" ".join(words))

# list slices
print(words[4:8])

print(words[:7])

print(words[8:])

# a few list functions
# lots more described here
# https://www.w3schools.com/python/python_ref_list.asp

# get index of first instance of the item passed in
print(words.index("game"))

# count the number of the intem passed in
print(words.count("ping"))

# sort the list in place
words.sort()
print(words)

# revserse the list in place
words.reverse()
print(words)


