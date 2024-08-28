#     string.split()
#     "race a car"
#  => ["race", "a", "car"]

# " ".join(string.split()).lower()


# 1.# input => string = "geeks for geeks idea"
  # output => string = "idea geeks for geeks"

# def revstring(string):
#     list1 = []
#     str = string.split()[::-1]
#     for element in str:
#         list1.append(element)

# string = input("enter the string")
# revstring(string)


# 2.# input => string = "geeks for geeks idea"
  # output => string = "aedi skeeg rof skeeg"
# def reversestr(input_string):
#     words = input_string.split()
#     # words = ["geeks","for","geeks","idea"]
#     revword = [word[::-1] for word in words]
#     # revword = ["skeeg","rof","skeeg","aedi"]
#     final_rev = " ".join(revword[::-1])
#     return final_rev
# input_string = input("enter thr string")
# reversestr(input_string)

# how to remove letters from a string
def removechar(string):
    remove = input("enter the element")
    result = " ".join(char for char in string if char not in remove)
    print(result) 
string = input("enter the input")
removechar(string)


