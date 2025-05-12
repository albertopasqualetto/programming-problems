#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        min_for_majority=len(nums)/2
        maj=nums[0]
        occ=0
        for n in nums:
            print(n, maj, occ)
            if occ==0:
                maj=n
            if maj==n:
                occ+=1
                if occ > min_for_majority:  # early exit
                    return maj
            else:
                occ-=1
        return maj

# @lc code=end

