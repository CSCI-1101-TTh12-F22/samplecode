# open the csv file for reading
f = open("state_us.csv")

# create an empty dictionary
abbrev = {}

# for each line in the file...
for line in f:

    # split the line on comma
    # (I also chop off the new line with rstrip()
    parts = line.rstrip().split(",")

    # map the abbreviation to the state
    abbrev[parts[1]] = parts[0]

# close the file
f.close()

# print out the dictionary
print(abbrev)

# loop through and print them out
for k,v in abbrev.items():
    print(f"{k} is the abbreviation for {v}")
