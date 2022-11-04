import numpy as np
import matplotlib.pyplot as plt


kids = np.loadtxt("schoolkids-simple.csv", delimiter=",", skiprows=1, dtype="int")

classes, counts = np.unique(kids[:,0], return_counts=True)
print(classes, counts)

class_labels = [str(x) + "th grade" for x in classes]
plt.pie(counts, labels=class_labels)
plt.title("Proportion of kids per grade")
plt.show()

average_heights = []
for a in np.unique(kids[:,1]):
    heights = kids[kids[:,1] == a,2]
    aveh = np.average(heights[heights > 120])
    average_heights.append(aveh)

plt.plot(np.unique(kids[:,1]), average_heights)
plt.show()

labels = ["height", "sleep", "texts"]
for i in [2, 3, 4]:
    plt.subplot(1, 3, i-1)
    plt.hist(kids[:,i])
    plt.gca().set_title(labels[i-2])

plt.show()


for i in [2, 3, 4]:
    plt.subplot(3, 1, i-1)
    plt.hist(kids[:,i])
    plt.gca().set_title(labels[i-2])

plt.show()
