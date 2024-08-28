def decorator(sub):
    def extra(a,b):
        print(a+b)
        return sub(a,b)
    return extra
@decorator
def sub(a,b):
    print(a-b)

s = sub(10,7)
print(s)

# or

def decorator(sub):
    def extra(a,b):
        print(a+b)
        return sub(a,b)
    return extra

z =decorator(sub)

def sub(a,b):
    print(a-b)

z = z(10,7)
print(s)


