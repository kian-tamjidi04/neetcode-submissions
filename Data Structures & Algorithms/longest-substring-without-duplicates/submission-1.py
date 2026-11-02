class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        l, r = 0, 0
        maxLen = 0
        while r < len(s):
            if s[r] in unique:
                unique.remove(s[l])
                l += 1
                continue
            else:
                unique.add(s[r])
                maxLen = max(maxLen, r - l + 1)

            r += 1

        return maxLen