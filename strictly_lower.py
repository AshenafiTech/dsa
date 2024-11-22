'''
You are given two arrays, sorted in non-decreasing order. For each element of the second
array, find the number of elements in the first array are that strictly less than it.
Input
Two sorted arrays.
Output
A single sorted array containing all elements from both arrays.

'''

from typing import List

def strictly_lower(arr1: List[int], arr2: List[int]) -> List[int]:
    res = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            j += 1
    while i < len(arr1):
        res.append(arr1[i])
        i += 1
    return res
