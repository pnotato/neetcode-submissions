class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res = "";
        // recall the first string might not be the shortest. we will need to break earlier
        for (int i = 0; i < strs[0].size(); i++) {
            for (int j = 0; j < strs.size(); j++) {
                if (i == strs[j].size() || strs[j][i] != strs[0][i]) {
                    return res;
                }
            }
            res += strs[0][i];
        }
        return res;
    }
};