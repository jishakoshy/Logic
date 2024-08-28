def recurfact(num):
    if n == 1:
        return n
    elif n== 0:
        return 1
    return n*(recurfact(num-1 ))
    
# 1
# 12
# 123
# 1234
# 12345
n = int(input("enter the number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()
   

# 1
# 01
# 101
# 0101
# 10101
n = int(input("enter the number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if i % 2!=0:
            print("1",end="")
        else:
            print("0",end="")
    print()


#     1
#    21
#   321
#  4321
# 54321
n = int(input("enter the number"))
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    print()


#     1
#    123
#   12345
#  1234567
# 123456789
n= int(input("enter the number"))
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end="")
    for j in range(1,2*i):
        print(j,end="")
    print()

#     1
#    1 2
#   1 2 3
#  1 2 3 4 
# 1 2 3 4 5
n = int(input("enter the number"))
for i in range(1,n+1):
    for k in range(n-i):
        print("",end="")
    for j in range(1,i+1):
        print(j)
        print(" ")
    print()

# 1
# 2  3
# 4  5  6
# 7  8  9  10
# 11 12 13 14 15

n = int(input("enter the number"))
for i in range(1,n+1):
    for j in range(0,i):
        print(i+1,end=" ")
    print()



# *******
# *    *
# *   *
# *  *
# * *
# *


# ******
# *****
# ****
# ***
# **
# *

