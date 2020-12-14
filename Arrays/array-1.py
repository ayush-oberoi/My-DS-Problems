myarray = ['a','b','c','d']

#push
myarray.append('e')  #O(1)

#push
myarray.pop()     #O(1)

#inserting at first
myarray.insert(0,'t')   #O(n)
myarray = ['u'] + myarray #O(1)

#inserting at middle
myarray.insert(2,'o')    #O(n)

#deleting at first
myarray.pop(0)           #O(n)

