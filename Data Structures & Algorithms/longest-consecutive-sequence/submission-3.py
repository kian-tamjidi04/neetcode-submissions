class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longest = 0

        for n in nums:
            if n - 1 in numSet:
                continue
            
            currLength = 1
            while n + currLength in numSet:
                currLength += 1
            longest = max(longest, currLength)
        
        return longest