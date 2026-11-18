class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        i = 0
        res = []

        while i < len(nums) and nums[i] <= 0:
            # Skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
            
            i += 1
        
        return res