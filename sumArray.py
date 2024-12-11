def subarraySum(nums, k):
    prefix_count = {0: 1}  # Initialize with 0:1 to handle cases where the subarray starts from index 0
    prefix_sum = 0
    count = 0

    for num in nums:
        prefix_sum += num  # Update the cumulative sum
        
        # Check if (prefix_sum - k) exists in the hashmap
        # if prefix_sum - k in prefix_count:
        #     count += prefix_count[prefix_sum - k]
        
        # Update the hashmap with the current prefix_sum
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

    return count

subarraySum([1, 2, 3], 2)  # Output: 2