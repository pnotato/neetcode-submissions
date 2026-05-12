class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> indices = {};

        for (int i = 0; i < nums.size(); i++) {
            int needed = target - nums[i];
            if (indices.contains(needed)) {
                return {indices[needed], i};
            }
            else {
                indices.insert({nums[i], i});
            }
        }


    }
};
