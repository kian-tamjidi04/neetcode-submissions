class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            target = nums[i]

            # Finished when ith value is positive (values are in increasing order)
            if target > 0:
                break
            
            # Skip duplicates
            if i > 0 and target == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if -(nums[j] + nums[k]) == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif -(nums[j] + nums[k]) < target:
                    k -= 1
                else:
                    j += 1
            
        return res
