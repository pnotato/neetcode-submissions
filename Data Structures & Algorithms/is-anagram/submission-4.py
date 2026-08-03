class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if len(s) == 1 and len(t) == 1:
            return s == t

        hashmap = {}
        for letter in s:
            if letter not in hashmap:
                hashmap.update({letter:0})
            else:
                hashmap[letter] += 1

        hashmap2 = {}
        for letter in t:
            if letter not in hashmap2:
                hashmap2.update({letter:0})
            else:
                hashmap2[letter] += 1

        return hashmap == hashmap2
