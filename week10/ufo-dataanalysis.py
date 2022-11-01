import numpy as np
import matplotlib.pyplot as plt

# read int the data
ufos = np.loadtxt("ufo-data.csv", delimiter=",", dtype="int")

# fields are month, year, time of day
# print out min and max of each column
print(np.min(ufos[:,0]), np.max(ufos[:,0]))
print(np.min(ufos[:,1]), np.max(ufos[:,1]))
print(np.min(ufos[:,2]), np.max(ufos[:,2]))


# make a line plot for sightings per year
years, ycounts = np.unique(ufos[:,1], return_counts=True)
plt.plot(years, ycounts)
plt.title("Sightings per year")
plt.xlabel("year")
plt.ylabel("# sightings")
plt.show()

# do the same but instead of lines do dots
plt.plot(years, ycounts, ".")
plt.title("Sightings per year")
plt.xlabel("year")
plt.ylabel("# sightings")
plt.show()


# get the number of sightings per month
months, counts = np.unique(ufos[:,0], return_counts=True)
print(months, counts)


# make a bar chart by month
month_names=["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"]

plt.bar(months, counts)
plt.xticks(months, month_names)
plt.title("Sightings per month")
plt.ylabel("# sightings")
plt.xlabel("month")
plt.show()


# make a pie chart of sightings per time range
# (midnight-6am, 6am-noon, noon-6pm, 6pm-midnight)

# save out the hours into to its own numpy array
hours = ufos[:,2]

# this is where we were aggregate the sightings per time range
sightings_per_segment = []
segment_labels = []

# for each 6-hour time period...
for i in range(0,24,6):

    # find all the time greater than the lower bound
    matches = hours[hours >= i]

    # among those, find all the times less than the upper bound
    fullmatches = matches[matches < i+6]

    # append the number of elements in that list 
    sightings_per_segment.append(len(fullmatches))

    # and the time range
    segment_labels.append(str(i) + "-" + str(i+6))

print(sightings_per_segment)
print(segment_labels)

# make a pie chart
plt.pie(sightings_per_segment, labels=segment_labels)
plt.title("Distribution of sightings per 6-hour time period")
plt.show()
