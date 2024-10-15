'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''

# Approach:

# The brute force approach would be to check every possible sequence of consecutive numbers starting from each number in the array. If we find a sequence longer than the current longest sequence, we update the length of the longest sequence. This approach would take O(n^3) time complexity.

# To optimize this, we can use a HashSet to store the numbers in the array. This will allow us to quickly check if a number is part of a sequence or not. We can then iterate over the array and for each number, check if the number is the start of a sequence. If it is, we can then check how long the sequence is by checking the next consecutive numbers in the HashSet. If the sequence is longer than the current longest sequence, we update the length of the longest sequence.

# Algorithm:

# Create a HashSet to store the numbers in the array.
# Iterate over the array and add each number to the HashSet.
# Initialize a variable to store the length of the longest sequence.
# Iterate over the array again and for each number, check if it is the start of a sequence.
# If the number is the start of a sequence, check how long the sequence is by checking the next consecutive numbers in the HashSet.
# If the sequence is longer than the current longest sequence, update the length of the longest sequence.
# Return the length of the longest sequence.

# Let's look at an example to understand how this works:

# nums: [100, 4, 200, 1, 3, 2]

# HashSet: {100, 4, 200, 1, 3, 2}

# longest_sequence: 4

# In this example, the HashSet contains all the numbers in the array. We iterate over the array and for each number, we check if it is the start of a sequence. We find that 1 is the start of a sequence, and we check how long the sequence is by checking the next consecutive numbers in the HashSet. We find that the sequence is 1, 2, 3, 4 so the length of the sequence is 4. Since this is longer than the current longest sequence, we update the length of the longest sequence to 4.

# code:

from typing import List

def longestConsecutive(nums: List[int]) -> int:
    
        # Create a HashSet to store the numbers in the array
        num_set = set(nums)
    
        # Initialize a variable to store the length of the longest sequence
        longest_sequence = 0
    
        # Iterate over the array and for each number, check if it is the start of a sequence
        for num in nums:
            # If the number is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_sequence = 1
    
                # Check how long the sequence is by checking the next consecutive numbers in the HashSet
                while current_num + 1 in num_set:
                    current_num += 1
                    current_sequence += 1
    
                # If the sequence is longer than the current longest sequence, update the length of the longest sequence
                longest_sequence = max(longest_sequence, current_sequence)
    
        # Return the length of the longest sequence
        return longest_sequence

# complexity analysis:

# The time complexity for this approach is O(n) where n is the number of elements in the array. This is because we iterate over the array twice, once to add the numbers to the HashSet and once to find the length of the longest sequence.

# The space complexity for this approach is O(n) where n is the number of elements in the array. This is because we use a HashSet to store the numbers in the array.