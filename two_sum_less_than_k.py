# nums = [34,23,1,24,75,33,54,8] 
nums = [10,20,30]
k = 15

def two(nums):
    nums.sort()
    maxN = 0
    l, r = 0, len(nums) - 1

    while l < r:
        curr = nums[l] + nums[r]

        if curr < k:
            l+=1
            maxN = max(curr, maxN)
        else:
            r-=1

    return maxN if maxN != 0 else -1

print(two(nums))
    