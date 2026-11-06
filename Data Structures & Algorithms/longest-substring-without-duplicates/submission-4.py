class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currSet = set()
        maxLen = 0
        l = 0

        for r in range(len(s)):
            # If the letter we're at has already been seen somewhere, need to remove letter at l because the substring is no longer valid

            # Even if s[l] != s[r], we care about substrings - substring invalid -> increment l until it is
            while s[r] in currSet:
                currSet.remove(s[l])
                l += 1
            currSet.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen

            