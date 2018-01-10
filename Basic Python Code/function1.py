def list(mylist):
    print("After adding in mylist\n")
    mylist.append(10)
    yourlist=[9,96,93]
    mylist.append(yourlist)
    return mylist
mylist=[1,2,3,4]
print(list(mylist))
