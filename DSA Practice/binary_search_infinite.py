def binary_search(a , start , end , target):
    if start > end:
        return
    mid  = end - ((end - start) // 2)
    if a[mid] > target:
        return binary_search(a , start , mid - 1, target)
    elif a[mid] < target:
        return binary_search(a , mid + 1, end , target)
    else:
        return mid + 1
    
def get_start_end(a , start , end , target , size):
    if a[end] == target:
        return end + 1
    if a[end] > target:
        return binary_search(a , start , end , target)
    else:
        return get_start_end(a , end + 1 , end + size + 1 , target,  size*2)
    
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
target = 11
print(get_start_end(a , 0, 1 , target , 2))