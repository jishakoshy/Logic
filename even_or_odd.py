# n = int(input("enter the number"))

# if n%2 == 0:
#     print("it is even")
# else:
#     print("it is odd")


# in a list, a num -> has both even and odd then return that   
list1 = [2,54,31,7,1,4]
has_even = False
has_odd = False
for num in range(list1):
    string = str(num)
    for i in string:
        newnum = int(i)
        if i % 2 == 0:
            has_even = True
        else:
            has_odd = True
if has_even and has_odd:
    print(num)



