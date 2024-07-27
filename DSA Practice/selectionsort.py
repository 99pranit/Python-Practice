import numpy as np
def maximum(arr , start , end):
    maximum = arr[0]
    index = 0
    for i in range (0 , end):
        if maximum < arr[i]:
            index = i
            maximum = arr[i]
    return index

def swap(arr , max_val_index , end):
    if arr[max_val_index] > arr[end]:
        temp = arr[max_val_index]
        arr[max_val_index] = arr[end]
        arr[end] = temp

def selection(arr):
    for i in range (0 , len(arr) - 1):
        max_val_index = maximum(arr , 0 , len(arr) - (i + 1))
        swap(arr , max_val_index , len(arr) - (i + 1))
    return arr

arr = np.array([12,21,12,43,14,54])
print(selection(arr))
    
