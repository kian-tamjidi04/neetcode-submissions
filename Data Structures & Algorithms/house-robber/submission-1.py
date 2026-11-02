class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxOutcomes = [0]*len(nums)

        maxOutcomes[0], maxOutcomes[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            maxOutcomes[i] = max(maxOutcomes[i-1], nums[i] + maxOutcomes[i-2])

        return maxOutcomes[len(nums) - 1]