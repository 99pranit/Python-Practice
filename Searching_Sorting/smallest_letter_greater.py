def smallest_letter_greater_target(a , start , end , target):
    if start > end:
        return a[start]
    mid = (start + end) // 2
    if ord(a[mid]) == ord(target):
        return a[mid]
    elif ord(a[mid]) > ord(target):
        return smallest_letter_greater_target(a , start , mid - 1 , target)
    else:
        return smallest_letter_greater_target(a , mid + 1 , end , target)
    
a = ['a' , 'b' , 'r' , 't' , 'u']
target = 'p'
ceil = smallest_letter_greater_target(a , 0 , len(a) - 1 , target)
print(f'Smallest letter greater than {target} in the array is {ceil}.')