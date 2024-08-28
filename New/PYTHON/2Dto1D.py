# flatten array - 2D to 1D and 3D to 1D

# array = [[1,2,3,4],[5,6,7,8]]   ---->  result = [1,2,3,4,5,6,7,8] 
def flatten(array):
    result = []
    for row in array:
        for element in row:
            result.append(element)
    return result
array = [[1,2,3,4],[5,6,7,8]] 
print("result of 2D flatten array is",flatten(array))


# array = [[[1,2,3,4],[5,6,7,8]]]   ---->  result = [1,2,3,4,5,6,7,8] 
def threeD(array):
    result = []
    for row in array:
        for coloumn in row:
            for element in coloumn:
                result.append(element)
    return result
array = [[[1,2,3,4],[5,6,7,8]]] 
print("result of 3D flatten array is",threeD(array))

# output -> [1, 2, 3, 4, 5, 6, 7, 8]



