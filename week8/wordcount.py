# read all of Moby-Dick into a string
# then split that string into a list of words
f = open("mobydick.txt")
text = f.read().split()
f.close()

# make an empty dictionary
counts = {}

# for every word in the list of words in Moby-Dick...
for w in text:

    # increase the count for that word by 1
    counts[w] = counts.get(w,0) + 1

# print out all the words whose count is > 1000
for k,v in counts.items():
    if v > 1000:
        print(k,v)

