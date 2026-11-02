class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxLen = 0

        for i in range(len(s)):
            # Case 1: Odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    res = s[l:r+1]
                    maxLen = r - l + 1
                l -= 1
                r += 1

            # Case 2: Even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    res = s[l:r+1]
                    maxLen = r - l + 1
                l -= 1
                r += 1

        return res