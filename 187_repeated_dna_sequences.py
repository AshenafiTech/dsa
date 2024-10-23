'''
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
'''

# Approach: Using Hash Map
# 1. Create a dictionary to store the substring and its frequency
# 2. Traverse through the string and store the substring in the dictionary
# 3. If the substring is already present in the dictionary, increment the frequency
# 4. If the frequency is greater than 1, append the substring to the result list
# 5. Return the result list

# Complexity Analysis
# The time complexity for this approach is O(n), where n is the length of the input string.
# The space complexity for this approach is O(n), where n is the length of the input string.

def findRepeatedDnaSequences(s):
    if len(s) < 10:
        return []
    result = []
    substring_freq = {}
    for i in range(len(s) - 9):
        substring = s[i:i + 10]
        if substring in substring_freq:
            substring_freq[substring] += 1
            if substring_freq[substring] == 2:
                result.append(substring)
        else:
            substring_freq[substring] = 1
    return result