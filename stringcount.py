                            # which char has Max count in a string ?
# string = (input("enter your thing"))
# list1 = list(string)
# x =[]
# length = len(list1)
# count = 1
# for i in range(length):
#     for j in range(i+1,length):
#         if list1[i] == list1[j]:
#             count += 1
#             x.append(i)
# maxcount = max(x)
# print(maxcount)

string = input("Enter your string: ")
list1 = list(string)

char_count = {}

for char in list1:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

max_count_char = max(char_count, key=char_count.get)
max_count = char_count[max_count_char]

print(f"The character '{max_count_char}' has the maximum count of {max_count}.")



