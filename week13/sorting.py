def bubble(mylist):

    # You have to go through the list n times.
    for i in range(len(mylist)):
        print(mylist)

        # Each time throug the list, it might turn out
        # to be sorted already. You can tell it's sorted
        # if the number of swaps made is 0.
        swaps = 0


        # You'll compare each element with the element
        # that comes next, and swap if the former > the latter.
        # That's why you stop at len(mylist)-1
        for j in range(len(mylist)-1):

            # if the current item > next item swap them
            if mylist[j] > mylist[j+1]:
                temp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = temp
                swaps += 1

        # If you get all the way through with no swaps
        # the list is sorted, so you can quit.
        if swaps == 0:
             print(mylist)
             return
    print(mylist)


def selection(mylist):

    # The last element will automatically
    # be right after you find the correct
    # element for the second to last element
    # so you can skip it.
    for i in range(len(mylist)-1):

        # Keep track of the minimum value and
        # the index of the minimum value.
        minval = mylist[i]
        minindex = i
        print(mylist)

        # When you find something smaller than the current
        # mininum, set it as the new minimum.
        for j in range(i+1, len(mylist)):
            if mylist[j] < minval:
                minval = mylist[j]
                minindex = j

        # Swap the new minimum with whatever is in the
        # current position, i.
        temp = mylist[i]
        mylist[i] = mylist[minindex]
        mylist[minindex] = temp
    print(mylist)


def main():
    sortme = [8, 1, 10, 2, 7, 4]
    print("unsorted list", sortme)
    print("Bubble sort")
    bubble(sortme)

    sortme = [8, 1, 10, 2, 7, 4]
    print("Selection sort")
    selection(sortme)

main()
