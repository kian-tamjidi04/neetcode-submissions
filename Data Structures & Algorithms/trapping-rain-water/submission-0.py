class Solution:
    def trap(self, height: List[int]) -> int:
        # Key formula = min(height[l], height[r]) - height[i]
        # height[l], height[r] are the max heights to the left and right of i

        if not height:
            return 0

        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        maxWater = 0

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                maxWater += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                maxWater += maxR - height[r]

        return maxWater

