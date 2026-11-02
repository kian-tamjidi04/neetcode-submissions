class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {} # Diff -> index

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in sumMap:
                return [sumMap[diff], i]

            sumMap[nums[i]] = i

        