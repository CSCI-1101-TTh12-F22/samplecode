import sys

### Example 1: read in a whole file
# open a file for reading
f = open("pandp.txt", "r", encoding="utf-8")

# read the whole file into a variable called text
text = f.read()

# print out the whole contents of the file
print(text)

# close the file
f.close()

### Example 2: read in a line of a file
# open a file for reading
f = open("pandp.txt", "r", encoding="utf-8")

# read in the first line of the file and print it out
text = f.readline()
print(text)

# read in the second line of the file and print it out
text = f.readline()
print(text)

# close the file
f.close()


### Example 3: go through a file line by line with for loop

# open a file for reading
f = open("pandp.txt", "r", encoding="utf-8")

# print out each line of the file, one by one
for line in f:
    print(line)

# close the file
f.close()


### Example 4: using "with" so you don't have to
### remember to close the file

# better: use the with keyword
with open("pandp.txt") as f:
    for line in f:
        print(line)

# Now you don't need to say f.close()!







