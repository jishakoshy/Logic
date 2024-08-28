# an array , if it has 2 target element return true else return false
def present(list1,t1,t2):
    for i in list1:
        if (t1 and t2 in list1):
            return True
        else:
            return False
        
list1 = [2,1,5,8,4,9]
n = len(list1)
t1 = 5
t2 = 8
x = present(list1,t1,t2)
print(x)

