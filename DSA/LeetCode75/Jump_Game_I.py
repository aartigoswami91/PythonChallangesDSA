
def Jump_Game(nums):
    pointer = len(nums)-1
    res = 0
    for i in range(len(nums)-1,-1,-1):
        if i + nums[i] >= pointer:
            pointer = i
            
    return True if  pointer == 0 else False  
            
        
            
        

        
nums = [2,4,0,0,0,2]
num2 = [3,2,1,0,4]
print(Jump_Game(num2))