from collections import defaultdict

class Solution:
    def groupAnagram(self, lists:list[str])->list[list[str]]:
        res = defaultdict(list)
        for strs in lists:
            count = [0]*26
            for s in strs:
                count[ord(s)-ord('a')] += 1
            res[tuple(count)].append(strs)
        return res.values()

sol = Solution()
print(sol.groupAnagram(["eat","tea","tan","ate","nat","bat"]))
                 
##Input: strs = ["eat","tea","tan","ate","nat","bat"]
 #Output: [["bat"],["nat","tan"],["ate","eat","tea"]]#