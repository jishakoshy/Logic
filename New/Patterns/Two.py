# Pascal's Triangle
# Pattern
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
n = int(input("Enter the size: "))

for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    row_value = 11**(i - 1) 
    print(' '.join(str(row_value)))

       

# have an input field and if enter string then it shows 
# an error message otherwise print the integer value

# n = int(input("enter integer"))
# if isinstance(n,int):
#     print(n)

# raise("please enter integer value")


