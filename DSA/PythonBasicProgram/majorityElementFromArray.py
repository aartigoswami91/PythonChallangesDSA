from typing import List


class majorityEle():
    def majorityElement(self, nums: List[int]) -> int:
        hm ={}
        for i in nums:
            if i in hm:
                hm[i] +=1
            else:
                hm[i] = 1
        return max(hm,key=hm.get)

ele = majorityEle()
num= [3,3.5,5.6,6,7,7,7]
ele.majorityElement(num)

        