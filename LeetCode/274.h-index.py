#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#
from typing import List

# @lc code=start

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        length = len(citations)
        # print("length:", length)
        citations.sort()
        # print("Citations:", citations)
        for c in range(length + 1):
            greater_n = len([i for i in citations if i >= c])
            # print(f"c:{c}, h:{h}, greater_n:{greater_n}")
            if greater_n >= c:
                h = c
        return h

# @lc code=end
