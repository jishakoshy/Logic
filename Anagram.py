# anagram -> length of 2 strings is equal and elements are same

def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # If lengths are not equal, they cannot be anagrams
    if len(str1) != len(str2):
        return False

    # Check each character in str1
    for char in str1:
        # Check if the character is present in str2
        if char not in str2:
            return False
        # If present, remove it from str2
        str2 = str2.replace(char, '', 1)

    # If str2 becomes empty, all characters in str1 were found in str2
    return not str2

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False