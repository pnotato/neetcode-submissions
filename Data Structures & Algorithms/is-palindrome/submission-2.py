class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        a = 0
        b = len(s) - 1
        while (a < b):
            if s[a] != s[b]:
                return False
            a += 1
            b -= 1
        return True