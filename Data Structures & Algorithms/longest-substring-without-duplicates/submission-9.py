class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
            
                


        # my attempt. 
        # l, r, res = 0, 0, 0
        # collected = set()
        # while r < len(s):
        #     if s[r] not in collected:
        #         collected.add(s[r])
        #         r += 1
        #     else:
        #         res = max(res, r-l)
        #         l = r
        #         collected.clear()

        # return r if l == 0 else res