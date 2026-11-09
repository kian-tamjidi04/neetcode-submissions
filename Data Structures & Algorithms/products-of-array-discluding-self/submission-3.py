class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 2 arrays - prefix and suffix
        # Each hold the product of items before and after the current item respectively

        pre, suff = [1] * len(nums), [1] * len(nums)

        # Populate pre
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]

        # Populate suff
        for i in range(len(nums) - 2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        
        res = []
        for i in range(len(nums)):
            res.append(pre[i] * suff[i])
        
        return res

        