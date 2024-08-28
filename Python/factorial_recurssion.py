# recursion must need base condition
def recurfact(num):
    if num == 0:
        return 1
    else:
        return num * recurfact(num - 1)
result = recurfact(6)
print(result)

# def factorial(num):
#     fact = 1
#     for x in range(num,1,-1):
#         fact *= x
#     return fact
    
# result = factorial(6)
# print(result)