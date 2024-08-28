# my_dict = {1:'fa',2:'fesaf',3:'vdf'}
# x = my_dict.pop(2)
# x = my_dict.pop(3)
# print(my_dict)

# # reverse a string
# x = input("enter you string")
# y = x[::-1]
# print(y)

# swapping
# list1 = [1,3,4,5,6]
# temp = list1[0] 
# list1[0]= list1[4]
# list1[4] = temp
# print(list1)

# check if it is palindrome or not
def palindrome():
    x = input("enter a string")
    y = x[::-1]
    if y != x:
       print("not palindrome")
    else:
        print(" palindrome")
    
palindrome()
    
