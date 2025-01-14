import numpy as np


def bubble(arr):
    temp = 0
    for i in range(0 , len(arr)):
        swap = False
        for j in range(1 , len(arr) - i):
            if (arr[j] < arr[j - 1]):
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
                swap = True
        if(swap == False):
           return arr
    return arr

arr = np.array([34,67,34,565,88234,36])
print(bubble(arr))