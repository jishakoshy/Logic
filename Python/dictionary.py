from collections import Counter
list1=[2,5,2,8,9,6,8,5,2,6,0,1,6,2,8,6,2]
counts = {}
for num in list1:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
maxi = max(counts.values())
max_count = [num for num, count in counts.items() if count == maxi]
print(max_count)

dict2 = {key:value for key,value in list1.items() }

# count = Counter(x)
# print(max(count.values()))


# n = 17, i=0, j = 1




# to run code use -> python dictionary.py

# mydict = [
#     {'name':'ram','place':'pta','address':'fsggsag'},
#     {'name':'ann','place':'klm','address':'fdfg'},
#     {'name':'vani','place':'nae'}
# ]

# dict = mydict[2]
# print("your desired ans is",dict)    

# dict1 = mydict[0]
# name = dict1['name']
# place = dict1['place']
# print(name,place)

# merge 2 dictionaries

# dict1 = {'a':1,'b':2,'c':3}
# merged_dict = {**dict1, **mydict}
# print(merged_dict)

# sorting dictionary
# my_dict = {2:'b',3:'c',1:'a'}
# sorted_dict = sorted(my_dict.items())
# print(sorted_dict)