def sort(arr):
    if len(arr) < 1:
        return arr
    else:
        mid = arr[len(arr)//2]

        left_arr = [x for x in arr if x < mid]
        pivot = [x for x in arr if x == mid]
        right_arr = [x for x in arr if x > mid]

    return sort(left_arr) + pivot + sort(right_arr)

arr = [23,54,123,658,1,3]
print(sort(arr))
