breakfast = ["cereal", "yogurt", "toast"]
lunch = ["sandwich", "soup", "salad"]
dinner = ["hamburger", "pizza", "pad thai"]

# list of lists
allmeals = [breakfast, lunch, dinner]

# print out breakfast foods
print(allmeals[0])

# print out the third lunch food
print(allmeals[1][2])


print(allmeals)

# this is different from concatenation
allfood = breakfast + lunch + dinner
print(allfood)


# For loops
for meal in allmeals:
    for food in meal:
        print(food, end=" ")
    print()


for i in range(len(allmeals)):
    for j in range(len(allmeals[0])):
        print(allmeals[i][j], end=" ")
    print()

# populating a list with a for loop
myLoL = []
for i in range(0,15,3):
    myLoL.append([i, i+1, i+2])

print(myLoL)

grades = []
f= open("pretendgrades.csv")
labels = f.readline().rstrip().split(",")
for line in f:
    parts = line.rstrip().split(",")
    grades.append([int(p) for p in parts[1:]])
f.close()

print(grades)

for g in grades:
    print(sum(g)/len(g))
    

    
    


