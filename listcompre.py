# list comprehention : filter dicts that don't have a key 




# remove nth element from list
def nth(list1,list2):
    list1.remove(list1[-1])
    list2.pop()

list1 = [23,323,24,2,75,7]
list2 =[5,6,2,7,36,3,17]
nth(list1,list2)

print(list1)
print(list2)

