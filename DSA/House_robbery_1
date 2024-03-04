class HouseRobbery:
    def robery(self, nums: list[int]) -> int:
        #rob1,rob2,n,n+1
        rob1,rob2 = 0,0
        for n in nums:
            res = max(n+rob1,rob2)
            rob1 = rob2
            rob2 = res
        return res
    
rob = HouseRobbery()
nums = [1,2,3,1]
print(rob.robery(nums))