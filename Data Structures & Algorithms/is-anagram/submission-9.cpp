class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
           return false;
        }
        std::unordered_map<char, int> seen = {};

        for (int i = 0; i < s.length(); i++) {
            if (seen.contains(s[i])) {
                seen[s[i]] += 1;
            }
            else {
                seen.insert({s[i], 1});
            }
        }

        for (int j=0; j < t.length(); j++){
            if (!seen.contains(t[j]) || seen[t[j]] == 0) {
                return false;
            }
            else {
                seen[t[j]] -= 1;
            }
        }
        return true;
    }
};
