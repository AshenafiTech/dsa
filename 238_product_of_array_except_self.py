'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

32-bit integer: -2^31 <= x <= 2^31 - 1
64-bit integer: -2^63 <= x <= 2^63 - 1
'''



# Approach:

# The product of all the elements except the current one can be broken down into two parts: the product of all the elements to the left of the current element and the product of all the elements to the right of the current element. For every element, we can find these two products and multiply them to obtain the answer for that element.

# Algorithm:

# Initialize two empty arrays, L and R where for a given index i, L[i] would contain the product of all the numbers to the left of i and R[i] would contain the product of all the numbers to the right of i.

# We would need two different loops to fill in values for the two arrays. For the array L, L[0] would be 1 since there are no elements to the left of the first element. For the rest of the elements, we simply use L[i] = L[i - 1] * nums[i - 1]. Remember that L[i] represents product of all the elements to the left of element at index i.

# For the other array, we do the same thing but in reverse i.e. we start with the initial value of 1 in R[length - 1] where length is the number of elements in the input array, and keep updating R[i] in reverse. Essentially, R[i] = R[i + 1] * nums[i + 1]. R[i] represents product of all the elements to the right of element at index i.

# Once we have the two arrays set up properly, we simply iterate over the input array one element at a time, and for each element at index i, we find the product except self as L[i] * R[i].

# Let's look at a simple example to understand how this works:


# nums:     2    3    4    5

# L:        1    2    6   24

# R:       60   20    5    1

# result: 60   40   30   24

# The product of all the numbers except the number at index i is simply the product of all the numbers to the left of i multiplied by the product of all the numbers to the right of i. We can calculate the product of all numbers to the left of i in the array and the product of all numbers to the right of i in two separate arrays. Then, the product of all the numbers except the number at index i is the product of the two arrays.

# Let's look at a simple example to understand how this works:

# nums:     2    3    4    5

# L:        1    2    6   24

# R:       60   20    5    1

# result: 60   40   30   24

# The product of all the numbers except the number at index i is simply the product of all the numbers to the left of i multiplied by the product of all the numbers to the right of i. We can calculate the product of all numbers to the left of i in the array and the product of all numbers to the right of i in two separate arrays. Then, the product of all the numbers except the number at index i is the product of the two arrays.

# code:

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:

    # The length of the input array
    length = len(nums)

    # The answer array to be returned
    answer = [0]*length

    # answer[i] contains the product of all the elements to the left
    # Note: for the element at index '0', there are no elements to the left,
    # so the answer[0] would be 1
    answer[0] = 1
    for i in range(1, length):
        # answer[i - 1] already contains the product of elements to the left of 'i - 1'
        # Simply multiplying it with nums[i - 1] would give the product of all
        # elements to the left of index 'i'
        answer[i] = nums[i - 1] * answer[i - 1]

    # R contains the product of all the elements to the right
    # Note: for the element at index 'length - 1', there are no elements to the right,
    # so the R[length - 1] would be 1
    R = 1
    for i in reversed(range(length)):
        # For the index 'i', R would contain the product of all elements to the right.
        # We update R accordingly
        answer[i] = answer[i] * R
        R *= nums[i]

    return answer


# Complexity Analysis

# Time complexity: O(N) where N represents the number of elements in the input array. We use one iteration to construct the array L, one to construct the array R and one last to construct the answer array using L and R.

# Space complexity: O(1) since don't use any additional array for our computations. The problem statement mentions that using the answer array doesn't add to the space complexity.

