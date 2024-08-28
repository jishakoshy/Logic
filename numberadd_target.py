# adding any 2 element in lis give the value 
# equal to the target
lis = [9,5,12,8,1,3,7,2]
target =18

for i in range(len(lis)):
    for j in range(i + 1, len(lis)):
        if lis[i] + lis[j] == target:
            print(f"{lis[i]} + {lis[j]} = {target}")

        

