import numpy as np
import matplotlib.pyplot as plt

# What percent in the survey are in each grade? (pie chart)
kids = np.loadtxt("schoolkids-simple.csv", delimiter=",", dtype="int", skiprows=1)
print(kids)

grades, counts = np.unique(kids[:,0], return_counts=True)
grade_labels = [str(x)+"th grade" for x in grades]
plt.pie(counts, labels=grade_labels, autopct='%1.0f%%')
plt.show()

# Average height

# store the average heights
aveheights = []

# go through each age
for a in np.unique(kids[:,1]):

    # get their heights
    heights = kids[kids[:,1] == a, 2]

    # get average of those values
    # but throw out ones < 120
    average = np.average(heights[heights > 120])

    # append tht average to the list above
    aveheights.append(average)

plt.plot(np.unique(kids[:,1]), aveheights)
plt.show()

# Histogram of age, height, sleep as subplots side by side
labs = ["height", "sleep", "texts"]
for i in [2, 3, 4]:
    plt.subplot(1, 3, i-1)
    plt.hist(kids[:,i])
    plt.gca().set_title(labs[i-2])

plt.show()

# stacked subplots
for i in [2, 3, 4]:
    plt.subplot(3, 1, i-1)
    plt.hist(kids[:,i])
plt.show()
