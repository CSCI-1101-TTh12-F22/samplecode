# function with default parameters defined
def printstuff(s="Herbert", i=10, l=["a", "b", "c"]):
    print("Hello " + s) # s must be a string
    print(i/3) # i must be a number
    print(l[0]) # l must be something that allows indexing (e.g., list, tuple)

# call with all positional args
printstuff("Bob", 4, [1, 2, 3])

# call with all keyword args
printstuff(l=[1, 2, 3], s="Bob", i=4)

# call that relies on default params
printstuff()

# mix and match!
printstuff(l=[1, 2, 3], s="Bob")
printstuff("Bob", 15)
printstuff(s="Bob", i=4)
printstuff(l=[1, 5, 2, 7])

