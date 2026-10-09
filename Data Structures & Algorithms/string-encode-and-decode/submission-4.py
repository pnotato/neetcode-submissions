class Solution:

    # "hello" "world"
    # -> $5|hello


    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += "$" + str(length) + "|" + s
        return res
        
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        length = 0
        while (i < len(s)):
            if s[i] == "$":
                i += 1
                length = ""
                while s[i] != "|":
                    length += s[i]
                    i += 1
                ln = int(length)
                res.append(s[i+1:i+1+ln])
                i += ln
            i += 1
        return res



