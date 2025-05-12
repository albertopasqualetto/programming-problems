#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
from typing import List

# @lc code=start

class Solution:
    profit = 0
    bought = False

    def buy(self, amount):
        self.profit -= amount
        self.bought = True
        # print("buying:", amount, "current profit:", self.profit)

    def sell(self, amount):
        self.profit += amount
        self.bought = False
        # print("selling:", amount, "current profit:", self.profit)


    def maxProfit(self, prices: List[int]) -> int:
        for i in range(len(prices) - 1):
            # print("i", i, "p", p)
            curr = prices[i]
            succ = prices[i+1]

            if self.bought and  curr > succ:
                self.sell(curr)
            if not self.bought and curr < succ:
                self.buy(curr)

        if self.bought:
            self.sell(prices[-1])

        return self.profit

# @lc code=end

