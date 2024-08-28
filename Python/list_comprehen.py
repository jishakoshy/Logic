#  Using dict comprehension and a conditional argument create a dictionary from 
# the current dictionary where only the key:value pairs with value above 2000 will 
# be taken to the new dictionary.

dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
dict2 = {key:value for key,value in dict1.items() if value > 2000}
print(dict2)


# Write a list comprehension that returns the list
# ["1*2=1", "2*2=4", "3*2=9", ....,      "25*2=625"]
lis = [f"{i} * 2  = {i**2}" for i in range(1,26)]
print(lis)


