def revstr(s):
    if len(s) <=1:
        return s
    return revstr(s[1:]) + s[0]

s = "hello"
print(revstr(s))


# reverse a recursion using string

def recur_string(str1):
    if len(str1) <=  1:
        return str1
    else:
        return recur_string(str1[-1]) + recur_string(str1[:-1])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

str1 = "meena"
x= recur_string(str1)
print(x)


# Correct Recursive Process:
# Initial Call:

# recur_string("hello")
# str1[-1] is "o".
# str1[:-1] is "hell".
# Result: "o" + recur_string("hell")

# Next Call:

# recur_string("hell")
# str1[-1] is "l".
# str1[:-1] is "hel".
# Result: "l" + recur_string("hel")

# Next Call:

# recur_string("hel")
# str1[-1] is "l".
# str1[:-1] is "he".
# Result: "l" + recur_string("he")

# Next Call:

# recur_string("he")
# str1[-1] is "e".
# str1[:-1] is "h".
# Result: "e" + recur_string("h")

# Next Call:

# recur_string("h")
# Base case: len(str1) == 1
# Result: "h"

# The recursive calls build the reversed string step-by-step: "o" + "l" + "l" + "e" + "h", resulting in "olleh".

# Summary:
# Original Code: Causes an infinite loop by continually reversing the string without reducing its length.
# Corrected Code: Properly reduces the problem size in each recursive call, eventually reaching the base 
# case and building the reversed string step-by-step.







# the below code make recurssion error because it cause infinite loops
# def recur_string(str1):
#     if len(str1) ==  1:
#         return str1
#     else:
#         return  recur_string(str1[::-1])

# print(recur_string("meena"))
