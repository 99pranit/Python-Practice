def swap(arr , i , correct):
    temp = arr[i]
    arr[i] = arr[correct]
    arr[correct] = temp

def search_missing(arr):
    i=0
    missing = []
    while i < len(arr):
        correct = arr[i]
        if arr[i] < len(arr) and arr[i] != arr[correct]:
            swap(arr, i , correct)
        else:
            i += 1
    for j in range(0 , len(arr)):
        if arr[j] != j:
            missing.append(j)
    return missing
        
arr = [4,3,2,7,8,2,3,1]
print(search_missing(arr))