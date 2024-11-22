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


# Time complexity of slicing a string is O(k) where k is the length of the slice
# So, the time complexity of the above approach is O(n * k), where n is the length of the input string and k is the length of the slice.
# The space complexity of the above approach is O(n), where n is the length of the input string.

def findRepeatedDnaSequences(s):
    if len(s) < 10:
        return []
    result = set()
    seen = set()
    for i in range(len(s) - 9):
        substring = s[i:i + 10]
        if substring in seen:
            result.add(substring)
        else:
            seen.add(substring)
    return list(result)


# Time complexity of slicing a string is O(k) where k is the length of the slice
# So, the time complexity of the above approach is O(n * k), where n is the length of the input string and k is the length of the slice.
# The space complexity of the above approach is O(n), where n is the length of the input string.



'''
Given a string, dna, that represents a DNA subsequence, and a number 
k
k
, return all the contiguous subsequences (substrings) of length 
k
k
 that occur more than once in the string. The order of the returned subsequences does not matter. If no repeated substring is found, the function should return an empty set.
'''


def findRepeatedSubsequences(dna, k):
    if len(dna) < k:
        return set()
    result = set()
    seen = set()
    for i in range(len(dna) - k + 1):
        substring = dna[i:i + k]
        if substring in seen:
            result.add(substring)
        else:
            seen.add(substring)
    return result


