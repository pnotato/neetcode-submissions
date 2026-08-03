class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i # intialize this pointer j at i
            while s[j] != "#": # loop every character until you reach the first #.
                j += 1
            length = int(s[i:j]) # This is to include multiple digits for numbers.
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res