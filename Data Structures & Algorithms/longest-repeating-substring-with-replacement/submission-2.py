class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        l = 0
        mostFreq = 0
        maxLen = 0

        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            mostFreq = max(mostFreq, window[char])

            while (r - l + 1) - mostFreq > k:
                window[s[l]] -= 1
                l += 1

            maxLen = max(maxLen, r - l + 1)

        return maxLen