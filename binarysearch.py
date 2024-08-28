# BINARY SEARCH -> applicable for sorted list

# In a binary search, however, cut down your search to half as soon as 
# you find the middle of a sorted list. The middle element is looked at to check 
# if it is greater than or less than the value to be searched. 
# Accordingly, a search is done to either half of the given list

          #   only on sorted array
def binary_search(target,list1,low,high):
	# here mid, low, high are index of list1
    mid = low + (high - low)//2

    while low < high:
        if list1[mid] == target:
            return target
        elif list1[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binarySearch(array, x, low, high):
	while low <= high:
		mid = low + (high - low)//2
		if array[mid] == x:
			return mid
		elif array[mid] < x:
			low = mid + 1
		else:
			high = mid - 1
	return -1
array = [2, 4, 5, 7, 14, 17, 19, 22]
x = 22
result = binarySearch(array, x, 0, len(array)-1)
if result != -1:
	print(str(result))
else:
	print("Not found")


# recursive binary search
def binary_search(arr, low, high, x):
	if high >= low:
		mid = (high + low) // 2
		if arr[mid] == x:
			return mid		
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)
		else:
			return binary_search(arr, mid + 1, high, x)
	else:
		return -1
# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10
# Function call
result = binary_search(arr, 0, len(arr)-1, x)
if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")




# def bine(low,high,target,list1):
# 	mid = low + (high-low) // 2
# 	while low < high:
# 		if target == mid :
# 			return mid
# 		elif list1[target] < mid:
# 			high = mid-1
# 		else:
# 			low = mid+1

# list1 = [1,3,5,6,7,8,9]
# low = list1[0]
# high = len(list1)-1
# target = 3
# bine(low,high,target,list1)


