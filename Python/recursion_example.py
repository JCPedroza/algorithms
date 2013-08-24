def example(alist):
    print ""
    print "---------------- example call ------------------"
    print "example is being called with: ", alist
    if len(alist) <= 1:
        print "reached base case with: ", alist
        return alist
    middle = len(alist) / 2
    left = alist[:middle]
    right = alist[middle:]
    left = example(left)
    right = example(right)
    print "right is: ", right
    print "left is:", left
    print ""
    print ">>>>>>>>>>>> end of example call <<<<<<<<<<<<<"


example([1, 2, 3, 4, 5, 6])
