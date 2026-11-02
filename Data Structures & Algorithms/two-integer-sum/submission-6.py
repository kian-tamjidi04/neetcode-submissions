class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementMap = {} # value : index

        for i in range(len(nums)):
            complement = target - nums[i]
            if complementMap and complement in complementMap:
                # Return current index and index of complement
                return sorted([i, complementMap[complement]])
            
            # Store value with associated index
            complementMap[nums[i]] = i