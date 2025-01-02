from collections import Counter
arr = [1,2, 3]
s = set()
mp = Counter(arr)
count = 0

for num in arr:
    if num+1 in mp and num not in s:
        count+=mp[num]
        s.add(num)

print(count)