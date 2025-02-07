def merge(nums1 , m , nums2 , n):
    end = len(nums1) - 1
    while n and m:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[end] = nums1[m - 1]
            m -= 1
        else:
            nums1[end] = nums2[n - 1]
            n -= 1
        end -= 1
    
    while n:
        nums1[end] = nums2[n - 1]
        n -= 1
        end -= 1
    
    return nums1

print(merge([1,2,3,0,0,0] , 3 , [2,5,6] , 3))