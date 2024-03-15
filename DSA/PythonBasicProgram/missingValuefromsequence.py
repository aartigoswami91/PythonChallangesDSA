def missing_value1(nums):
    x = len(nums)
    for i in range(x):
        if i not in nums:
            return i

number = [3,0,1]
print(missing_value1(number))