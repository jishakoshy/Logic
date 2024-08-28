# in a digit having both odd and even numbers will return that digit otherwise not
def is_odd_or_even(num):
    digit = str(num)
    has_odd = False
    has_even = False
    for char in digit:
        change = int(char)
        if digit%2 == 0:
            has_even = True
        else:
            has_odd = True

        if has_odd  and has_even:
            return True
        
    return False
        

list = [12,3,4,95,33,22,10]
