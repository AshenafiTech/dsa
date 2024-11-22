from typing import List
from itertools import accumulate
from bisect import bisect_right


heroes = [1, 4, 2]
monsters = [1, 1, 5, 2, 3]
coins = [2, 3, 4, 5, 6]


# Iterate over heroes
# for each heroes
# Initialize sum
# check if each value in monsters is less than or equal to heroes
# if condition is met
# sum the values at which the values of heroes is greater than or equal to the value of monsters
# append the sum to result


# return result
res = []
for i in heroes:
    s = 0
    for j in range(len(monsters)):
        if i >= monsters[j]:
            s+=coins[j]
    res.append(s)

print(res)

# Time: O(n*m) where n i len or heroes and m is len of monsters
# Space: O(n) where n is length of heroes


def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        m = len(monsters)
        idx = sorted(range(m), key=lambda i: monsters[i])
        s = list(accumulate((coins[i] for i in idx), initial=0))
        ans = []
        for h in heroes:
            i = bisect_right(idx, h, key=lambda i: monsters[i])
            ans.append(s[i])
        return ans

