class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in ")]}" and len(stack) == 0:
                return False
            elif char == ")" and stack.pop() != "(":
                return False
            elif char == "]" and stack.pop() != "[":
                return False
            elif char == "}" and stack.pop() != "{":
                return False
        if len(stack) > 0:
            return False
        return True