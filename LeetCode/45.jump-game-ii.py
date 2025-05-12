#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        start_pos = 0
        target_pos = len(nums) - 1
        visiting_end = start_pos
        farthest = start_pos

        for i in range(target_pos):
            farthest = max(farthest, nums[i] + i)
            if farthest >= target_pos:
                jumps += 1
                break
            if i == visiting_end:
                jumps += 1
                visiting_end = farthest
        return jumps
# @lc code=end
