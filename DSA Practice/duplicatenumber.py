def swap(arr , i , correct):
    temp = arr[i]
    arr[i] = arr[correct]
    arr[correct] = temp

def duplicate(arr):
    i=0
    duplicate = set()
    while i < len(arr):
        correct = arr[i]
        if arr[i] < len(arr) and arr[i] != arr[correct]:
            swap(arr, i , correct)
        else:
            i += 1
    for j in range(0 , len(arr)):
        if arr[j] != j:
            duplicate.add(arr[j])
    return duplicate
        
arr = [0,1,3,4,2,2,3,5]
print(duplicate(arr))
