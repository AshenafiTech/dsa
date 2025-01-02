n, s = map(int, input().split())
array = list(map(int, input().split()))
max_len = 0
curr_s = 0
start = 0
 
for end in range(len(array)):
    curr_s +=  array[end]
    
    while curr_s > s:
        curr_s -= array[start]
        start+=1
    max_len = max(max_len, end-start+1)
    
print(max_len)