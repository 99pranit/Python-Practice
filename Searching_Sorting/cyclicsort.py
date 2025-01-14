import numpy as np

def swap(arr, i , index):
    temp = arr[i]
    arr[i] = arr[index]
    arr[index] = temp

def sort(arr):
    i = 0
    while i < len(arr):
        index = arr[i] - 1
        if(arr[index] != arr[i]):
            swap(arr , i , index)
        else:
            i = i + 1
    return arr

arr = np.array([2,4,3,1,5])
print(sort(arr))