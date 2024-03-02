


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        #buccketSortAlogorithem
        #bucket[0]--> 0 repeatation, bucket[1]--> 1 repeatation
        bucket = [[] for i in range(len(nums)+1)]
    
        counts = {}
        for num in nums:
            counts[num] =  1 + counts.get(num,0)
        for s,v in counts.items():
            bucket[v].append(s)
        print(bucket)
        print(counts)

        arr =[]
        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                arr.append(n)
                if len(arr) == k:
                    return arr
                

sol1 = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(sol1.topKFrequent(nums,k))


           


##Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]