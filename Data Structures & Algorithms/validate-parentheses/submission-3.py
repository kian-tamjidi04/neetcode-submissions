class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {"]":"[", "}":"{", ")":"("}

        for c in s:
            if c not in pairs:
                stack.append(c)
                continue
            elif not stack or pairs[c] != stack[-1]:
                return False

            stack.pop()
        
        return not stack