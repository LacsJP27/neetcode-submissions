class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(heights) - 1
        while l < r:
            minHeight = min(heights[l], heights[r])
            length = r - l
            currArea = length * minHeight
            maxArea = max(maxArea, currArea)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea
        # [1, 2, 1, 9]
