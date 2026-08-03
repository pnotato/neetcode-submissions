class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0

        for l in range(len(s)):
            r = l
            count = 0
            seen = set()
            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                r += 1
            maxL = max(maxL, r - l)
        return maxL


        # while r < len(s):
        #     count = 0
        #     seen = set()
        #     while r < len(s) and s[r] not in seen:
        #         seen.add(s[r])
        #         r += 1
        #     maxL = max(maxL, r - l)
        #     l = r
        # return maxL
            
