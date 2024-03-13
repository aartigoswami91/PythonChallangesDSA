def twoSum(nums):
    hashMap = {}
    for i ,num  in enumerate(nums):
        diff = target - num
        if diff in hashMap:
            return [hashMap[diff],i]
        hashMap[num] = i
    return 
        
nums = [2,7,4,6,3,8,1]

target = 9
print(twoSum(nums))