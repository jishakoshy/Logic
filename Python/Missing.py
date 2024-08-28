# how to find out the missing and duplicate element in a series  of an array

array = [3,5,7,5,8,10]
list1 = []
n= len(array)

for num in array:
for i in range(0,n-1):
    if (array[i+1] != array[i] + 1 ):
        list1.append(array[i] + 1)
print(list1)



# for i in range(0,n-1):
#         for array[i] in array:
#             if array[i+1] != array[i] + 1:
#                 list1.append(array[i] +1)

# for i in range(n - 1): 
#     current = array[i]
#     next_value = array[i + 1]
#     for missing in range(current + 1, next_value):
#         list1.append(missing)
# print("Missing elements:", list1)
