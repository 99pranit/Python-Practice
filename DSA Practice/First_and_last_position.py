def first_and_last_position(a , start , end , target , first_index , ans):
    ans = ans + 1
    if start > end:
        return ans
    mid = end + ((start - end) // 2)
    if a[mid] > target:
        return first_and_last_position(a , start , mid - 1 , target , first_index , ans)
    elif a[mid] < target:
        return first_and_last_position(a , mid + 1 , end , target , first_index , ans)
    else:
        ans = mid
        if(first_index):
            return first_and_last_position(a , start , mid - 1 , target , first_index , ans)
        else:
            return first_and_last_position(a , mid + 1 , end , target , first_index , ans)

a = [5 , 6 , 6 , 7 , 7 , 7 , 8 , 8 , 9]
target = 7
ans = [-1 , -1]
ans[0] = first_and_last_position(a , 0 , len(a) - 1 , target , True, ans[0])
ans[1] = first_and_last_position(a , 0 , len(a) - 1 , target , False , ans[1])
print(ans)
