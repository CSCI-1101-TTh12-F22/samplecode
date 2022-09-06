# findthousands.py
# Emily Prud'hommeaux
# September 6, 2022

# Get a number from the user using input.
a = input("Enter a big integer: ")

# Get and print the thousands place using string indexing.
b = a[-4]
print("The thousands place is:", b)

# Get and print the thousands place using math operations.
# Remember, input gives you back a string. You need to convert
# the string to an integer.
c = (int(a) // 1000) % 10
print("The thousands place is:", c)
