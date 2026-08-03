class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        return nums.size() != set(nums.begin(), nums.end()).size();
    }
};