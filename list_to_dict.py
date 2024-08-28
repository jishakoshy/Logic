list1 = [1,2,2,2,3,3,4,5,5,5,5,5]
dict1 = {key: value for key,value in enumerate(list1)}
print(dict1)



# a list has duplicate, in that highest count of duplicate using dict
list1 = [1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5]

# Step 1: Count the occurrences of each element in list1
count_dict = {x: list1.count(x) for x in set(list1)}


# Step 2: Find the element with the highest count
max_count_element = max(count_dict, key=count_dict.get)
max_count = count_dict[max_count_element]

print("Count dictionary:", count_dict)
print("Element with highest count:", max_count_element)
print("Highest count:", max_count)





list2 = [3,2,5,6,3,6,2,6,7,9,5,32,2,5,3]
dict = {}

for key,value in enumerate(list2):
    if value in dict1:
        value[list2] += 1
    value[list2] = 1
print(dict)