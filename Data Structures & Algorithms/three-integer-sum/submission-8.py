class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(0, len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, len(nums) - 1

            while j < k:
                curr = nums[i] + nums[j] + nums[k]

                if curr == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif curr < 0:
                    j += 1
                else:
                    k -= 1

        return res