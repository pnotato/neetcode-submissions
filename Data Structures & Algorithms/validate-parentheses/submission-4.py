class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                if not stack or stack.pop() != matches[char]:
                    return False
                
        return not stack

