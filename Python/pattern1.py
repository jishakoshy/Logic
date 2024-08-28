n = int(input("enter the number"))
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end="")
        
    print()
        
# *******
# ******
# *****
# ****
# ***
# **
# *


for i in range(n,0,-1):
    print(i * "*")

# *
# **
# ***
# ****
for i in range(1,n+1):
    print(i * "*")


#    *
#   * *
#  * * *

for i in range(n):
    # Print leading spaces
    print(' ' * (n - i - 1), end='')
    # Print asterisks with spaces in between
    print('* ' * (i + 1))


