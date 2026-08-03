class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> indices = {};
        for (int i = 0; i < nums.size(); i++) {
            indices[nums[i]] = i;
        }

        for (int j=0; j < nums.size(); j++) {
            int total = target - nums[j];
            if (indices.count(total) > 0 && j != indices[total]) {
                return std::vector<int> {j, indices[total]};
            }
        }

        return std::vector<int> {};
    }
};
