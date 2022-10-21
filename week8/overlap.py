string1 = "Four score and seven years ago our fathers\
            brought forth on this continent a new nation\
            conceived in liberty and dedicated to the proposition\
            that all men are created equal."

string2 = "Whose woods these are I think I know\
            his house is in the village though\
            he will not mind me stopping here\
            to watch his woods fill up with snow"



# print out all the words that are in both strings

# first turn each string into a list of words with split()
l1 = string1.split()
l2 = string2.split()

# strategy 1: go through one list of words
# and if you find that word in the other list, print!
for w in l1:
    if w in l2:
        print(f"{w} is in both texts")

# strategy 2: turn one list into a set so look up will be faster
s2 = set (l2)

for w in l1:
    if w in s2:
        print(f"{w} is in both texts")

# strategy 3: turn both lists into sets and then take
# their intersection
s1 = set(l1)
common_words = s1.intersection(s2)
print(common_words)

# Note that when you print out common_words
# it's not in any particular order.
# Sets are unordered!
