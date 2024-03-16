def targetFunct(nums,target):
    hashMap = {}
    for i, num in enumerate (nums):
        diff = target - num
        if diff in hashMap:
            return [hashMap[diff],i]
        else:
            hashMap[num] = i

nums = [2,3,5,5,2,6,2,1]  
target = 4
print(targetFunct(nums,target))       
    