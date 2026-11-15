class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # Found the result (success case)
            if total == target:
                res.append(cur.copy())
                return

            # Path down the tree wasn't valid (unsuccessful case)
            if i >= len(nums) or total > target:
                return
            
            # Decision 1: Include current value to list
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # Decision 2: Increment i by not including candidate
            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res
