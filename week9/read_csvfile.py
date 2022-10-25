## Read the csv file into a list of lists

# create your empty list of lists
mylol = []

# open the csv file
f = open("pretendgrades.csv")

# read in the first line, which are the headers
header = f.readline().rstrip().split(",")

# now read in line by line
for line in f:

    # strip off the newline, and split on comma
    grades = line.rstrip().split(",")

    # add that list to the listof lists
    mylol.append(grades)

f.close()
print(mylol)


## Calculate the quiz average for each student

# for each list (row) in your list of lists
for row in mylol:

    # the name is the first element
    name = row[0]

    # turn the rest of the row (row[1:]) to ints
    grades = [int(x) for x in row[1:]]

    # calculate the average of those grades
    average = sum(grades) / len(grades)
    print(f"{name}: {average:.2f}")


## Calculate the average score on each quiz

# Here we have to accumulate score for each
# quiz row by row.
listofsums = [0, 0, 0, 0, 0, 0]

# for each row
for row in mylol:

    # convert the grades to ints
    grades = [int(x) for x in row[1:]]

    # for each quiz grade, add it to the
    # element in listofsums for that quiz
    for i in range(len(grades)):
        listofsums[i]+=grades[i]

# Finally, print out the average for each quiz
for i in range(len(listofsums)):
    print(f"{header[i]}: {listofsums[i]/len(mylol):.2f}")

    
