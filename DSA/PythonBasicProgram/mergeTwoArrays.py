def mergeSort(nums1,m,nums2,n):
    leng =  min(m,n)
    l,r = 0,0
    arr = []
    while l < m and r < n:

        if nums1[l] <= nums2[r]:
            arr.append(nums1[l])
            l += 1
        else:
            arr.append(nums2[r])
            r += 1
            
    print(l,r)
    
    if l < m:
        arr.extend(nums1[l:])  
    else:
        arr.extend(nums2[r:])

    return arr
                
                
 #1.  
                
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3            
print(mergeSort(nums1,m,nums2,n))   