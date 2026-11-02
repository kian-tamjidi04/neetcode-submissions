class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialise a map mapping values in the array to their index
        prevMap = {}

        for i, n in enumerate(nums):
            # Obtains the difference between the target and current value in array
            diff = target - n
            
            # If the difference is in the map already, return the current index and index of difference
            if diff in prevMap:
                return [prevMap[diff], i]
            
            prevMap[n] = i