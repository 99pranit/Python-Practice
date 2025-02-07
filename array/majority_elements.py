def majority_element(nums):
    current , count = 0 , 0
    for n in nums:
        if not count:
            current = n
            count += 1
        elif current == n:
            count += 1
        else:
            count -= 1
    return current

print(majority_element([1,2,2,3,2,1]))