# sorted_list = sorted(my_list)  -----> Return a new sorted list
# my_list.sort()  ----->   Sort the list in-place

# list1=[2,5,6,3,0]
# list1.sort()
# print(list1)

#   to find n prime numbers:-

# prime = 2,3,5,7,11,13,17,19,23    
# def isPrime(n):
#     if(n<=1):  return False
#     for i in range(2,n):
#         if(n%i==0):
#             return False
#     return True

# N = 100
# for i in range(1,N+1):
#     if(isPrime(i)):
#         print(i,end="   ")




# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,n):
#         if n%i == 0:
#             return False

# N = 100
# for i in range(1,N+1):
#     if is_prime(i):
#         print(i,end=" ")



# def prime(n):
#     if n <= 1:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#         return True
    
# number = int(input("enter a num"))
# if prime(number):
#     print()


def sort_max(list1):
    list1 = sorted(list1)
    print(list1)
    x = max(list1)
    
list1 = [2,3,1,7,4,5]

sort_max(list1)
