class Solution:
    def isValid(self, s: str) -> bool:
        match = {")":"(", "}":"{", "]":"["}
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if not stack or stack[-1] != match[c]:
                    return False
                stack.pop()
        return True if not stack else False