import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


fields = ["ClassGrade", "Ageyears", "Height_cm", "Sleep_Hours_Schoolnight",
          "Text_Messages_Sent_Yesterday"]


kids = np.loadtxt("schoolkids-simple.csv", delimiter=",", skiprows=1, encoding="utf-8")

print(kids[:,0])

# pie chart of how many kids in each grade
grades, numbers = np.unique(kids[:,0], return_counts=True)
plt.pie(numbers, labels=grades)
plt.pie(numbers, labels=grades)


# average height for each age
# throw out kids who reported < 120 cm
averageheights = []
for g in np.unique(kids[:,1]):
    heights = kids[kids[:,1] == g, 2]
    averageheights.append(np.average(heights[heights > 120]))


plt.plot(np.unique(kids[:,1]), averageheights)
plt.show()

# make a plot of subplots with various interesting things
plt.subplot(1, 3, 1)
plt.hist(kids[:,3])
plt.subplot(1, 3, 2)
plt.boxplot(kids[:,4])
plt.subplot(1, 3, 3)
plt.pie(numbers, labels=grades)
plt.show()

# make a plot with three histograms
for i in [1, 2, 3]:
    plt.subplot(1, 3, i)
    plt.hist(kids[:,i])

plt.show()
    

