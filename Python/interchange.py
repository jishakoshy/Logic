# python program to interchange first and last element in a list

# def interchange(list1):
#     temp = list1[0]
#     list1[0] = list1[-1]
#     list1[-1] = temp
    
# list1 = [23,4,6,78,43,54]
# interchange(list1)
# print(list1)



# using tuple variable -> when assign more than 1 value to a variable python assign it as a tuple
def swaplist(list):
    get = list[-1],list[0]
    list[0],list[-1] = get
    return list
list = [12,5,6,4,8]
print(swaplist(list))