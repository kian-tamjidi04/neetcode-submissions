class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.replace(" ", "")

        for c in s:
            if c not in "abcdefghijklmnopqrstuvwxyz" and c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and c not in "0123456789":
                s = s.replace(c, "")

        k = len(s) - 1

        for i in range(len(s)):
            if s[i].lower() != s[k].lower():
                return False
            k -= 1
        
        return True