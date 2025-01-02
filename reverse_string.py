'''
Description
Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
'''
s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]

l, r = 0, len(s)-1


def reverseString(l, r):
    while l < r:
        s[l], s[r] = s[r], s[l]
        l+=1
        r-=1

reverseString(l, r)

i = 0

for end in range(len(s)):
    if s[end] == " ":
        reverseString(i, end-1)
        i=end+1

reverseString(i, len(s)-1)
print(s)