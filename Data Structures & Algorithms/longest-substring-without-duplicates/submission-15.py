class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # more efficient
        l, r = 0, 0
        maxV = 0
        seen = set()
        while (r < len(s)):
            while (s[r] in seen):
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxV = max(maxV, r-l+1)
            r += 1

        return maxV



            
            


