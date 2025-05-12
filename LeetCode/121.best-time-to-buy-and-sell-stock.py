#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
import numpy as np
# def withNumpy(prices) -> int:
#     while len(prices):
#         imin = np.argmin(prices)
#         imax = np.argmax(prices)
#         if imin < imax:
#             return prices[imax]-prices[imin]
#         else:
#             return max(withNumpy(np.delete(prices, imin)), withNumpy(np.delete(prices, imax)))
#     return 0
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices = np.array(prices)
        best=0
        for i in range(len(prices)):
            new = np.max(prices[i:])-prices[i]
            if new > best:
                best=new
        return int(best)

        # other recursive approach:
        # but first remove some redundant elements
        # p = np.array(prices)
        # rem = []
        # for i in range(1,len(p)-1):
        #     if p[i-1]>=p[i]>=p[i+1]:
        #         rem.append(i)
        # return int(withNumpy(np.delete(p, rem)))
        
# @lc code=end

