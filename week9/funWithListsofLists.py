# make some lists of food you eat at meals
breakfast = ["pizza", "eggs", "cereal", "pancakes", "bacon"]
lunch = ["sandwich", "pasta", "burger", "grilled cheese", "chicken 2 sides"]
dinner = ["steak", "pizza", "soup", "pork chops"]

# create a list of list where each list
# is a list of foods you can eat at that meal
meals = [breakfast, lunch, dinner]

# ugly print with [ ] and '
print(meals)

# pretty print like a human would enjoy
for m in meals:
    for f in m:
        print(f, end=" ")
    print()

# alternatively with indices and range
for i in range(len(meals)):
    for j in range(len(meals[i])):
        print(meals[i][j], end=" ")
    print()

# Here's another way to put all those lists into a LoL
altmeals = []
altmeals.append(breakfast)
altmeals.append(lunch)
altmeals.append(dinner)
print(altmeals)

# Concatenating is *NOT* going to make you a LoL
notalol = breakfast + lunch + dinner
print(notalol)

# Using extend() will *NOT* make a LoL
altnotalol = []
altnotalol.extend(breakfast)
altnotalol.extend(lunch)
altnotalol.extend(dinner)
print(altnotalol)

# populate a list of lists with a for loop and range
mylol = []
for i in range(0,16,4):
    mysublist = [i, i+1, i+2, i+3]
    mylol.append(mysublist)
print(mylol)



