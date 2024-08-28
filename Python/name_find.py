# find the missing element in a list
name = ["a","","i","","h"]

starting = "a"
middle = "i"
ending = "h"
total = ["b","c","d","e","f","g","h","j","k","l","m","n","o",
         "p","q","r","s","t","u","v","w","x","y","z"]

for second in total:
    for fourth in total:
        possible = [starting + second + middle + fourth + ending]
        print(possible)

