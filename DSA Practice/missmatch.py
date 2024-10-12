def swap(arr , index , correct):
    temp = arr[index]
    arr[index] = arr[correct]
    arr[correct] = temp

def missmatch(arr):
    i = 0
    while i < len(arr):
        correct = arr[i] - 1
        if 0 <= correct < len(arr) and arr[correct] != arr[i]:
            swap(arr , i , correct)
        else:
            i += 1
    for j in range(0, len(arr) - 1):
        if j+1 != arr[j]:
            return [j+1 , arr[j]]
    return -1

arr = [2,1,4,2,6,5]
print(missmatch(arr))