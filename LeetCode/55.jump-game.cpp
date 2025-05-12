/*
 * @lc app=leetcode id=55 lang=cpp
 *
 * [55] Jump Game
 */

// @lc code=start
class Solution {
public:
    bool canJump(std::vector<int>& nums) {
        int start_pos = 0;
        int target_pos = nums.size() - 1;
        
        int curr_pos = start_pos;

        int max_pos = curr_pos + nums[curr_pos];
        while (true){
            if (max_pos >= target_pos) {
                return true;
            }
            curr_pos++;
            if (curr_pos > max_pos) {
                return false;
            }
            if (curr_pos + nums[curr_pos] > max_pos) {
                max_pos = curr_pos + nums[curr_pos];
            } 
        }
    }
};
// @lc code=end

