class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''.join(a for a in s.lower() if a.isalnum())
        return res == res[::-1]