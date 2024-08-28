# LINEAR SEARCH

# Assume that item is in an array in random order and we have to find an item. 
# Then the only way to search for a target item is, to begin with, the first position 
# and compare it to the target. If the item is at the same, we will return the position
# of the current item. Otherwise, we will move to the next position. If we arrive at the 
# last position of an array and still can not find the target, we return -1. 
# This is called the Linear search or Sequential search.
#                   eg:   1 -> 2-> 3-> 5-> 45-> 0,       target = 8

def linearsearch(target,list1,n):
    for i in range(0,n):
        if list1[i] == target:
            return i
    else:
        return -1
    

target= 7
list1 = [3,9,0,8,7,4]
n = len(list1)
result  = linearsearch(target, list1, n)
if(result == -1):
    print("target not found")
else:
    print("target is founded",result)
