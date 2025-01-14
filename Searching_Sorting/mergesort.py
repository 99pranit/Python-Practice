def sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        left_arr = arr[:mid]
        right_arr = arr[mid:]

        sort(left_arr)
        sort(right_arr)

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] > right_arr[j]:
                arr[k] = right_arr[j]
                j += 1
            else:
                arr[k] = left_arr[i]
                i += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            k += 1
            i += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            k += 1
            j += 1

arr = [24,2,6,8,6,32,56,21]
sort(arr)
print(arr)