name = "shantanu"
print(name[2:8:2])

# name = "shantanu"
# print(name[2:8:-2])

# in python duplicate keys doesnot exit so len(my_dict) is 2
my_dict = {"jay":89,"viru":81,"jay":52}
print(len(my_dict))

# merge 3 lists -> output is [(1,4,7),(2,5,8),(3,6,9)]
# by using zip() the o/p will get
a = [1,4,7]
b = [2,5,8]
c = [3,6,9]

print(list(zip(a,b,c)))

name = 'swapnali walke'
name1 = 'Swapnali walke'
name == name1
# the name == name1 output is false because the ord('s') = 115 and ord('S') = 83
# so  115 != 83

name >= name1
# the o/p is True


# Ternary Operator in c / c++

# condition ? value_if_true : value_if_false

# Ternary Operator in python 
    # value_if_true if condition else value_if_false
# eg:
age = 20
message = "you can vote" if (age>=18) else "you cannot"
print(message)

