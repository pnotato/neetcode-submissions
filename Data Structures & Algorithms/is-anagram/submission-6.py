class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        wordlist = {}
        for letter in s:
            if letter in wordlist:
                wordlist[letter] += 1
            else:
                wordlist[letter] = 1
        
        for letter in t:
            if wordlist.get(letter):
                wordlist[letter] -= 1
            else:
                return False

        return True