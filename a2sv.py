"""
Given a matrix mat where every row is sorted in strictly increasing order, return the smallest common element in all rows.
If there is no common element, return -1.
 
Example 1:
Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5

 
Constraints:
1 <= mat.length, mat[i].length <= 500
1 <= mat[i][j] <= 10^4
mat[i] is sorted in strictly increasing order.

"""
# time complexity: O(n^2)
# Space complexity : O(n^2)

from collections import Counter

def matrixMat(mat):

    freq = Counter(mat[0])


    for row in mat:
        for num in row:
            freq[num]+=1
            
    for num in sorted(freq.keys()):
        if num == len(mat):
            return num
    return -1

print(matrixMat([[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]))