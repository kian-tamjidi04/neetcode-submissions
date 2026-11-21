class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        # curr = current combination
        # total = sum of elements in curr
        # i = index of value we're considering
        def dfs(i, curr, total):
            # Success base case
            if total == target:
                res.append(curr.copy()) # continue to use the curr var when considering other combos
                return

            # Failure base cases
            if i >= len(nums) or total > target:
                return

            # Include value
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])

            # Exclude value
            curr.pop()
            dfs(i+1, curr, total)

        dfs(0, [], 0)
        return res