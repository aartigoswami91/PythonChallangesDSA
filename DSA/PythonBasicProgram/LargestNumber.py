#Write a Python program to find the largest element in a list.

def longest_number(nums):
    max_num = 0 
    res = 0
    for num in range(len(nums)-1): 
        if max_num < nums[num]:
            #range operation return index not value of the array
            max_num = nums[num]
            res = max_num
        else:
            res = max(res,max_num)
        
    return res
    
nums = [10, 5, 8, 20, 3]
print(longest_number(nums))