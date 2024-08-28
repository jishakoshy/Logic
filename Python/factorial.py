num = int(input("enter the number"))
if num != 0:
    factorial =1
    for i in range(num,0,-1):
        factorial *= i
    print(f"the factorial of {num} is {factorial}")
else:
    print("the factorial of 0 is 1")


# factorial of a number
# x = int(input("enter a number"))
# factorial=1
# for x in range(x,1,-1):
#     factorial = factorial*x
# print(factorial)