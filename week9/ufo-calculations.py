import numpy as np
import matplotlib.pyplot as plt

# Using np.loadtxt
npufo = np.loadtxt("ufo-data.csv", delimiter=',',
                   skiprows=1, dtype="int")

# Using the old-fashioned way
ufodata = []
with open("ufo-data.csv") as f:
    labels = f.readline()
    for line in f:
        parts = line.rstrip().split(",")
        ufodata.append([int(x) for x in parts])
npufo = np.array(ufodata)



# years
# earliest sighting
print("Earliest sighting: ", np.min(npufo[:,1]))

# plot sightings over years
years, sightings = np.unique(npufo[:,1], return_counts=True)

# line plot
plt.plot(years,sightings)
plt.title("UFO sightings by year")
plt.xlabel("Year")
plt.ylabel("# sightings")
plt.show()


# Same thing if I wanted unconnected red points instead of a line
plt.plot(years,sightings, "o", color="red")
plt.title("UFO sightings by year")
plt.xlabel("Year")
plt.ylabel("# sightings")
plt.show()


# months: use unique to get the number of sightings per month
months, sightings = np.unique(npufo[:,0], return_counts=True)

# make bar chart with sightings per month 
plt.bar(months, sightings)
plt.xlabel("Month")
plt.ylabel("# sightings")
plt.title("Total UFO sightings for each month")
plt.xticks(months, ["J", "F", "M", "A", "M", "J",
                    "J", "A", "S","O", "N", "D"])
plt.show()


# month with most sightings
maxsightingsmonth = months[np.argmax(sightings)]
print("Month number", maxsightingsmonth, "has the most UFO sightings")

# hours
hours = npufo[:,2]
hoursightings = []

# aggregate sightings per 6-hour chunk starting at midnight (0)
for i in range(0,24,6):

    # find everything < i+6
    matches = hours[hours < i+6]

    # of those, find everything >= i
    othermatches = matches[matches >= i]

    # count them up with len
    hoursightings.append(len(othermatches))

# make a pie chart!
plt.pie(hoursightings, labels=["12am-6am", "6am-12pm", "12pm-6pm", "6pm-12am"])
plt.title("UFO sightings by time of day")
plt.show()

# Alternative way of aggregating sightings by 6-hour chunk
# using list comprehensions.
hoursightings = []
for y in range(0,24,6):
    ycount = [1 for x in hours if x >= y and x < y+6]
    hoursightings.append(sum(ycount))

plt.pie(hoursightings, labels=["12am-6am", "6am-12pm", "12pm-6pm", "6pm-12am"])
plt.title("UFO sightings by time of day")
plt.show()

