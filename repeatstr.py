# return the letter that  repeat more
# string = "adfrefgee"
# count = 1
# x={}

# for char in string :
#     if char in x:
#         x[char] += 1
#     else:
#         x[char] = 1

# max_count = 0
# max_repeated_letter = None

# for char,count in x.items():
#     if count > max_count:
#         max_count = count
#         max_repeated_letter = char

# print(f"the most repeated letter is {max_repeated_letter} and with count of {max_count}")


# in list the most repeated number will return
list1 = [2,3,5,3,6,7,8,9,65,4,3,3,3,2,4,3,4]

x = {}

for key in list1:
    if key in x:
        x[key] += 1
    else:
        x[key] = 1

max_count = 0
max_repeated_number = None

for key,count in x.items():
    if count > max_count:
        max_count = count
        max_repeated_number = key

print(f"the number {max_repeated_number} has the max count {max_count}")



# find the duplicate element from the list without modifying the list
list3 = [2,3,5,3,6,7,8,9,65,4,3,3,3,2,4,3,4]
count = 1
for i in list3: