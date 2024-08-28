#  return common elements in lists 

list1 = [1,3,6,4,8,7]
list2 = [4,23,43,8,7]
for i in list1:
  for j in list2:
    if i == j:
      print(i,end=" ")

# or 

list1 = [1,3,6,4,8,7]
list2 = [4,23,43,8,7]
set1 = set(list1)
result = list(set1.intersection(list2))
result = list(set1.union(list2))
print(result)

# or











