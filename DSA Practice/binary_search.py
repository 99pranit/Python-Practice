def binary_search(a , target , start , end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if target == a[mid]:
        return mid + 1
    elif target < a[mid]:
        return binary_search(a , target , start , mid - 1)
    else: 
        return binary_search(a , target , mid + 1, end)
    
a = [1,3,6,8,9]
target = 6
index = binary_search(a , target , 0 , len(a) - 1)
print(f'{target} is present at {index}')