# Leetcode: Encode and Decode string 

'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Implement the encode and decode methods.

Note:

The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.



'''

class Codec:
    
        def encode(self, strs):
            return ''.join(f'{len(s)}:' + s for s in strs)
    
        def decode(self, s):
            strs = []
            i = 0
            while i < len(s):
                j = s.find(':', i)
                i = j + 1 + int(s[i:j])
                strs.append(s[j+1:i])
            return strs
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

# Time: O(n)
# Space: O(n)   

# The encode function first encodes the length of each string, then the string itself. The decode function reads the length of the string, then reads the string itself.

# The encode function is O(n) because it iterates through each string in the list. The decode function is also O(n) because it iterates through the encoded string. The space complexity is O(n) because the encoded string will be at most 2n characters long.

