class Solution:
    def isValid(self, s: str) -> bool:
        parenMap = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []

        for c in s:
            if c in parenMap.values():
                stack.append(c)
            else:
                if stack and stack[-1] == parenMap[c]:
                    stack.pop()
                else:
                    return False
        
        return not stack