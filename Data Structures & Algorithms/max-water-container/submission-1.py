class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        # Idea: get max area between l and r indices, update pointers depending on which side has the limiting height
        maxWater = 0
        while l < r:
            currWater = (r - l) * min(heights[l], heights[r])

            maxWater = max(currWater, maxWater)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        
        return maxWater