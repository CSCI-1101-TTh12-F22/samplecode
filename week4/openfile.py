# open a file for reading
f = open("greatexpectations.txt", "r", encoding="utf=8")

# for each line in the file, print it out preceded by
# "Charles Dickens once said: ")
for line in f:
    print("Charles Dickens once said: " + line)
f.close()

# same thing, but using with syntax so you don't
# need to close the file
with open("greatexpectations.txt") as f:
    for line in f:
        print("Charles Dickens once said: " + line)


