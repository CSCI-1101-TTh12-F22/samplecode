import numpy as np
import matplotlib.pyplot as plt

# Doesn't work! :(
# metal = np.loadtxt("metal587.csv", delimiter=",", skiprows=1)

# Use pandas! :)
import pandas as pd
metal = pd.read_csv("metal587.csv")

# print out some stuff about heavy metal bands
print("There are,", len(metal), "bands in the dataset.")    
print("These are the characteristics:", metal.columns)
print("Here's the 27th band on the list:", metal["band_name"][26])


# which band has the most fans?
print(  metal["band_name"][np.argmax(metal["fans"])], "has the most fans")

# which band was formed the earliest?
print(  metal["band_name"][np.argmin(metal["formed"])], "is the oldest")

# Which are the top 5 bands, by numnber of fans?
print("\nThese bands have the most fans: ", end=" ")
mostfans = np.array(np.argsort(metal["fans"]))
for i in range(-1, -6, -1):
    print(metal["band_name"][mostfans[i]], end=" ")
print("\n")

swedish = metal[metal["origin"] == "Sweden"]
print("Here is a list of Swedish metal bands:", list(swedish["band_name"]))
