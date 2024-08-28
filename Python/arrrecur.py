# array reverse using recursion
def reverse_array(array):
    if len(array) == 0 and len(array) == 1:
        return array
    else:
        return [array[-1]] + reverse_array(array[:-1])
array = [1, 2, 3, 4, 5]
print(reverse_array(array))

# reverse an array in normal way
# list1 = [12,4,5,2,7,9]
# reverse  = list1[::-1]
# print(reverse)

# reverse an array
def reverse(array):
    list1 = []
    for i in range(len(array)-1, -1, -1):
        list1.append(i)
    print(list1)

def rev(arrays):
    