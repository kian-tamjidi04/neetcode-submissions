class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # Char : frequency
        maxLen = 0
        l = 0
        
        maxFrequency = 0

        for r in range(len(s)):
            # Get the frequency of r
            count[s[r]] = 1 + count.get(s[r], 0)

            # Update the most frequenct character in the substring
            maxFrequency = max(maxFrequency, count[s[r]])
            
            # Number of replacements = length of substring - most frequent character
            # Shrink window while number of replacements exceeds k
            while (r - l + 1) - maxFrequency > k:
                count[s[l]] -= 1
                l += 1
            
            # Update max length
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen
