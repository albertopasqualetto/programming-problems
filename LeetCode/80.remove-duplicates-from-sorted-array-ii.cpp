/*
 * @lc app=leetcode id=80 lang=cpp
 *
 * [80] Remove Duplicates from Sorted Array II
 */

// @lc code=start
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int toSubtract=0;
        bool seenMoreThanOnce=false;
        for(int i=1; i<nums.size(); i++){
            if(nums[i]==nums[i-1]){
                if(seenMoreThanOnce){
                    toSubtract++;
                } else {
                    nums[i-toSubtract]=nums[i];
                }
                seenMoreThanOnce=true;
            } else {
                seenMoreThanOnce=false;
            }
            if(!seenMoreThanOnce){
                nums[i-toSubtract]=nums[i];
            }
        }
        return nums.size()-toSubtract;
    }
};
// @lc code=end

