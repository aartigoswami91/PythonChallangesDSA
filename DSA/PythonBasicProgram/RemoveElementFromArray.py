def removeElement(nums,val):
    arr = []
    for i in nums:
        if i != val:
            arr.append(i)
    return arr
    
    
    
nums = [3,2,2,3]
# 0,1,2,3
#num[0] == 3
val = 3
print(removeElement(nums,val))