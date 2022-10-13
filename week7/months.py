months = ["January", "February", "March", "April",
          "May", "June", "July", "August", "September",
          "October", "November", "December"]


# print out months with 31 days
print(months[0], months[2], months[4], months[6], months[7], months[9], months[11])

# print out months in each season
print(months[:3])  
print(months[3:6])
print(months[6:9])
print(months[9:])

# alternative way of printing out each season
for i in range(0,len(months),3):
    print(months[i], months[i+1], months[i+2])


# one way to change July to Quintember:

months[6] = "Quintember"

months = ["January", "February", "March", "April",
          "May", "June", "July", "August", "September",
          "October", "November", "December"]

# another way to change July to Quintember:
months.remove("July")
months.insert(6, "Quintember")

months = ["January", "February", "March", "April",
          "May", "June", "July", "August", "September",
          "October", "November", "December"]

# even better way change July to Quintember:
months[months.index("July")] = "Quintember"

months = ["January", "February", "March", "April",
          "May", "June", "July", "August", "September",
          "October", "November", "December"]

# add some new months onto the end, option 1
newmonths = ["Undecember", "Duodecember"]
months = months + newmonths

months = ["January", "February", "March", "April",
          "May", "June", "July", "August", "September",
          "October", "November", "December"]

# add some new months onto the end, option 2
months = months.extend(newmonths)


months = ["January", "February", "March", "April",
          "May", "June", "July", "August", "September",
          "October", "November", "December"]

# Create list of uppercase months with a for loop
newmonths = []
for m in months:
    newmonths.append(m.upper())
print(newmonths)

# Create list of uppercase months with list comprehension
newmonths = [m.upper() for m in months]
print(newmonths)

# Create list of A and J months with a for loop
newmonths2 = []
for m in months:
    if m[0] == "A" or m[0] == "J":
        newmonths2.append(m)
print(newmonths2)

# Create list of A and J months with a list comprehension
newmonths2 = [m for m in months if m[0] == "A" or m[0] == "J"]
print(newmonths2)


