class Solution:
    def isPalindrome(self, s: str) -> bool:
        # this question is a pain in the ass to do in C++ so I'm leaving it like this
        # yes i know i can do it with 2 pointers but this is way funnier
        s = ''.join(char for char in s if char.isalnum()).lower()
        return s == s[::-1]