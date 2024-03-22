from typing import List


class BuySellInProfit():


    # 1. take two pointers l,r 
    # 2. you buy at l and sell at day r
    # 3. until r is out of range of prices process
    # 4. if profit is negative move l=r and r += 1 
    # 5. other wise just move r by 1
    # 6. res is max of profit and res
    # 7. return res



    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        res = 0
        profit = 0
        while r < len(prices):
            profit = prices[r]-prices[l]
            if profit < 0:
                l = r
            r += 1
            
            res = max(res,profit)

        return res


profit = BuySellInProfit()
num = [1,7,3,8,2,4,7,8,2,4]
profit.maxProfit(num)

        