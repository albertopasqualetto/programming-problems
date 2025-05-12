/*
 * @lc app=leetcode id=189 lang=cpp
 *
 * [189] Rotate Array
 */

// @lc code=start
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k=k%nums.size();
        vector<int> temp{};
        for(int i=nums.size()-k; i<nums.size(); i++){
            temp.push_back(nums[i]);
        }
        for(int i=nums.size()-1; i>=k; i--){
            nums[i]=nums[i-k];
        }
        for(int i=0; i<k; i++){
            nums[i]=temp[i];
        }
    }
};
// @lc code=end

