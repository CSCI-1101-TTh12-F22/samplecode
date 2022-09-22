name = "Harold"
year = 2023
major = "Chemistry"

# different ways to print out the same thing
print(name, "|||", year, "|||", major)
print(name + " ||| " + str(year) + " ||| " + major)
print(name, year, major, sep=" ||| ")
print(f"{name} ||| {year} ||| {major}")
print("{} ||| {} ||| {}".format(name,year,major))
print(name, "|||", year, "|||", major, "\n", end="")


# open the file for writing (use the "w" argument!)
g = open("myout.txt", "w")

g.write(name + " ||| " + str(year) + " ||| " + major + "\n")
g.write(f"{name} ||| {year} ||| {major}\n")

mystring = name + " ||| " + str(year) + " ||| " + major + "\n"
g.write(mystring)


# NOTE This line below won't work! Why?
# Because write() is not the same as print()!
# write() can take only one argument: a string.
# print() can take multiple string arguments, plus things like sep and end.
# g.write(name, "|||", year, "|||", major)

# Don't forget to close your file!
g.close()

