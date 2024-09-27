def sort(arr , n , i):
    if(n == 0):
        return arr
    elif(n < i):
        if(arr[i] > arr[i + 1]):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            return sort(arr , n , i + 1)
    else:
        return sort(arr  , n -1 , 0)
    
arr = [1,4,2,3]
print(sort(arr , len(arr) - 1 , 0))