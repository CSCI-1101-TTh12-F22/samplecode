import numpy as np

# get header labels
f = open("pretendgrades.csv")
headers = f.readline().rstrip().split(",")
headers = headers[1:]
f.close()

# get the names of the students as numpuy array
names = np.loadtxt("pretendgrades.csv", delimiter=",",
                  skiprows=1, usecols=(0), dtype="str")

# get grades themselves as numpy array
grades = np.loadtxt("pretendgrades.csv", delimiter=",",
           skiprows=1, usecols=(1,2, 3, 4, 5, 6))

for n in names:
    print(n)

print(grades)

# access the grade of quiz #5 for person #3
print(f"The grade for {names[2]} for {headers[4]} is {grades[2][4]}")
print(f"The grade for {names[2]} for {headers[4]} is {grades[2,4]}")


# get the average quiz grade of the 1st person
print(f"The average quiz grade for {names[0]} is {np.mean(grades[0,:]):.2f}")

# get the average of quiz #1 over all people
print(f"The average grade on Quiz #{headers[0]} is {np.mean(grades[:,0]):.2f}")

# print out the average of each quiz
for m in np.mean(grades, axis=0):
    print(f"{m:.2f}", end=" ")
print()

# print out the quiz average of each person
n = 0
for m in np.mean(grades, axis=1):
    print(f"{names[n]}: {m:.2f}")
    n += 1
    

# print out the person with the highest grade Quiz 2
# note: if there are multiple max values, it returns the first one
print(f"{names[np.argmax(grades[:,1])]} got the highest grade on {headers[1]}")


# print out the person with the highest grade on each quiz
print(names[np.argmax(grades, axis=0)])

