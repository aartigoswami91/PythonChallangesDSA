integer= 1234
def reverse_int(nums):
    res = 0
    while nums >0:
        rem = nums % 10
        res = res*10+rem
        nums = int(nums / 10)
        
    return res
        
print(reverse_int(12345))