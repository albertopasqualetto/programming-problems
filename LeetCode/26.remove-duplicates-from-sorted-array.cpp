/*
 * @lc app=leetcode id=26 lang=cpp
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int toSubtract=0;
        for(int i=1; i<nums.size(); i++){
            if(nums[i]==nums[i-1]){
                toSubtract++;
            } else {
                nums[i-toSubtract]=nums[i];
            }
        }
        return nums.size()-toSubtract;
    }
};
// @lc code=end

