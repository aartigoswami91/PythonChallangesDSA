from collections import defaultdict 

def groupAnagram(lists):
    res = defaultdict(list)
    for strs in lists:
        count = [0]*26
        
        for s in strs:
            count[ord(s) - ord('a')] += 1
            
        res[tuple(count)].append(strs)
    return res.values()
lists = ['eat','ate','dog','god']            
print(groupAnagram(lists))    