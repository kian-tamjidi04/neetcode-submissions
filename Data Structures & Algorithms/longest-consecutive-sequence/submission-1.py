class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Used to check if n - 1 (n in nums) is in the set
        lookupSet = set(nums)

        longest = 0

        for n in nums:
            if (n - 1) not in lookupSet:
                currLen = 1
                while (n + currLen) in lookupSet:
                    currLen += 1
                longest = max(longest, currLen)
        return longest