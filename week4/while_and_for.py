
## Demonstrating how to do for in range loops with while


# one arguments
for i in range(10):
    print(i, end=" ")
print()

# remember: with while loops *you* keep track
# of how often you iterated through the loop!
i = 0
while i < 10:
    print(i, end=" ")
    i += 1
print()



# two arguments
for i in range(3, 10):
    print(i, end=" ")
print()

# for the while version, you just need
# to start your counter at whatever
# the first argument of range was
i = 3
while i < 10:
    print(i, end=" ")
    i += 1
print()




# three arguments
for i in range(3,10,2):
    print(i, end=" ")
print()

# for the while version, you just increment your counter
# variable by whatever you had in the third argument of range
i = 3
while i < 10:
    print(i, end=" ")
    i += 2
print()


