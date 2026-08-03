class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> seen = {};

        // ampersand makes it a reference to not copy it
        for (auto& num : nums) {
            if (seen.count(num) > 0) {
                return true;
            }
            else {
                seen.insert(num);
            }
        }

        return false;

    }
};
