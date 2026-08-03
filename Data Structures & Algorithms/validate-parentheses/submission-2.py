class Solution:
    def isValid(self, s: str) -> bool:
        braces = {
        ')':'(',
            ']': '[',
            '}':'{'
        }
        stack = deque()
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                if len(stack) == 0 or braces[char] != stack.pop():
                    return False

        return len(stack) == 0



## Could be better