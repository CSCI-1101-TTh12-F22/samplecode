
# appending will change the list passed in
def changelist1(a):
    a.append("bloop")

# changing individual elements will change the list passed in
def changelist2(a):
    a [0] = "glip"

# reassigning the whole list will *not* change the list passed in
def changelist3(a):
    a = ["moo"]


def main():
    z = ["bleep"]
    print("Starting list: ", z)
    changelist1(z)
    print("After appending in a function:", z)
    changelist2(z)
    print("After changing an element in a function:", z)
    changelist3(z)
    print("After reassigning the whole list in a function:", z)


main()
