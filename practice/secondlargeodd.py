# # second largest odd number

# list1 = [3,5,7,2,24,1,5,3,6,8,4]
# x=[]
# for num in list1:
#     if num%2 != 0:
#         x.append(num)
#     print(x)
#                              # x =[3,5,7,1,5,3]
# if len(list1) < 2:
#     print("there is no larget number")
# else:
#     largest_odd = max(x)

#     for i in x: 
#         if i != largest_odd:
#             if i>i+1:
#                 second_largest = i
#                 print(second_largest)
#             else:
#                 second_largest = i+1
#                 print(second_largest)


list1 = [3, 5, 7, 2, 24, 1, 5, 3, 6, 8, 4]
x = [num for num in list1 if num % 2 != 0]

if len(x) < 2:
    print("There are not enough odd numbers in the list to find the second largest.")
else:
    largest_odd = max(x)
    second_largest_odd = None
    for num in x:
        if num != largest_odd:
            if second_largest_odd is None  or  num > second_largest_odd:
                second_largest_odd = num

    if second_largest_odd is not None:
        print("Second largest odd number is:", second_largest_odd)
    else:
        print("There is no second largest odd number in the list.")
