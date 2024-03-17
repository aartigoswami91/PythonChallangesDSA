from ast import List


class RotateArray:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        k = k % len(nums)
        l ,r = 0, len(nums)-1
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1,r-1
        
        
        l ,r = 0, k-1
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1,r-1
        

        l ,r = k, len(nums)-1
        while l < r:
          nums[l],nums[r] = nums[r],nums[l]
          l,r = l+1,r-1

rotat1 = RotateArray()
nums = [1,2,3,4,5,6,7]
k = 3
print(rotat1.rotate(nums, k))