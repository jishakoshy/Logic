lis = [4,2,1,2,8,5,7,11]
lis = set(lis)
lis1 = []
for i in lis:
    if i % 2 != 0:
        lis1.append(i)
print(lis1)

largest = lis1[0]
for i in lis1:
    if i > largest:
        second = largest
        largest = i       
print(second)