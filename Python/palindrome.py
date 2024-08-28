# 
def palindrome(string):
    cleaned_string = ''.join(string.split()).lower()
    # cleaned_string = string.replace(" ", "").lower()
    if(cleaned_string == cleaned_string[::-1]):
        print("it is a string")
    else:
        print("its not palindrome")

string = input("enter the string")
print(palindrome(string))


