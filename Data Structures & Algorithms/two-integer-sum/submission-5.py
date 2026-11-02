class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementMap = {} # complement : index

        for i in range(len(nums)):
            complement = target - nums[i]
            if complementMap and complement in complementMap:
                return sorted([i, complementMap[complement]])
            complementMap[nums[i]] = i