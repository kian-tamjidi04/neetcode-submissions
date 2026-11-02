class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracketMap = {'}':'{', ']':'[', ')':'('}

        for c in s:
            # If c is an opening bracket, push it to the stack
            if c not in bracketMap:
                stack.append(c)
                continue
            elif not stack or bracketMap[c] != stack[-1]:
                # If c is a closing bracket AND the stack is empty OR 
                # doesn't match top of the stack
                return False

            # Update the stack
            stack.pop()
        
        # Return true if the stack is empty
        return not stack