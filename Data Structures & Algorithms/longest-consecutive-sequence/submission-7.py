class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        longest = 1
        numSet = set(nums)

        for n in nums:
            if n - 1 in numSet:
                continue

            currVal = n + 1
            currLen = 1

            while currVal in numSet:
                currLen += 1
                currVal += 1
            longest = max(longest, currLen)

        return longest