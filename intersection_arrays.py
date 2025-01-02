arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]

win = []

i, j, k = 0, 0, 0

while i < len(arr1) :
    if arr1[i] == arr2[j] == arr3[k]:
        win.append(arr1[i])
        i+=1
        j+=1
        k+=1
    else:
        if arr1 <


print(win)