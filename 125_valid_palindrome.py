# How to remove panctuations and whitespaces from a string

import string

def is_palindrome(s):
    s = s.lower()
    s = ''.join([c for c in s if c not in string.punctuation + string.whitespace])
    return s == s[::-1]



# another approach

def is_palindrome(s):

    s = s.lower()
    s = ''.join([c for c in s if c.isalnum()])
    return s == s[::-1]


# explain s[::-1]

# s[::-1] is a Python slice that reverses the string. It is a common Python idiom to reverse a string. For example, if s = "hello", then s[::-1] will return "olleh". This is because the slice notation s[i:j:k] means get the substring of s starting at index i and ending at index j in steps of k. If i is not provided, it defaults to 0. If j is not provided, it defaults to the length of the string. If k is not provided, it defaults to 1. If k is negative, it reverses the string. So s[::-1] means get the substring of s starting at the end and ending at the beginning in steps of -1, which effectively reverses the string.


# Time complexity : O(n), where n is the length of the input string s. We iterate through the string once to remove the punctuation and whitespace characters and once to check if it is a palindrome.

# Space complexity : O(n), where n is the length of the input string s. We create a new string with the punctuation and whitespace characters removed, which has a length of at most n.

