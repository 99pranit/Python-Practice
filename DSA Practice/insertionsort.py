import numpy as np

def swap(arr , i , j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def sort(arr):
    for i in range(0, len(arr) -1):
        for j in range(i+1 , 0, -1):
            if (arr[j] < arr[j-1]):
                swap(arr , j , j-1)
            else:
                break
    return arr

arr = np.array([12,21,12,43,14,54])
print(sort(arr))