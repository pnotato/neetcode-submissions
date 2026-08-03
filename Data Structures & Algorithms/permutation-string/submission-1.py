class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        chars = {}
        for i in s1:
            chars[i] = chars.get(i, 0) + 1
        
        l, r = 0, 0
        while (l < len(s2)):
            if s2[l] in chars:
                chars_tmp = chars.copy()
                r = l
                while chars_tmp and r < len(s2) and s2[r] in chars_tmp:
                    if chars_tmp[s2[r]] == 1:
                        del chars_tmp[s2[r]]
                    else:
                        chars_tmp[s2[r]] -= 1
                    r += 1
                if not chars_tmp:
                    return True
            l += 1
        return False








