# find 2nd largest odd number from a list?
# newlist = []
# def secodd(list1):
#     for num in list1:
#         if num % 2 != 0:
#             newlist.append(num)
#     x = sorted(newlist)
#     print(x)
#     print(x[1])
# list1 = [12,4,11,5,6,7,88,90]
# secodd(list1)

# find 2nd largest odd number from a list without using sort?
def secondlargestodd(list1):
    largest = None
    secondlargest = None
    for num in list1:
        if num % 2 != 0:
            if largest is None or num > largest:
                secondlargest = largest               
                largest = num
            elif secondlargest is None or num > secondlargest:
                secondlargest = num
    if secondlargest is not None:
        print(secondlargest)
    else:
        print("no second largest odd number")
list1 = [12,4,11,5,6,7,88,90]
secondlargestodd(list1)

# swap the key and value in a dictionary without creating new dictionary