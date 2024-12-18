def ceiling_number(a , target , start , end):
    if start > end:
        return a[start]
    mid = (start + end) // 2
    if target == a[mid]:
        return mid + 1
    elif target < a[mid]:
        return ceiling_number(a , target , start , mid - 1)
    else: 
        return ceiling_number(a , target , mid + 1, end)
    
a = [1,3,6,8,9]
target = 7
ceil = ceiling_number(a , target , 0 , len(a) - 1)
print(f'Ceiling of {target} is {ceil}')