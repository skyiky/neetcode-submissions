class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        l, r = 0, len(heights)-1
        while l < r:
            diff = heights[r] - heights[l]
            result = max(result, (r-l) * (min(heights[l], heights[r])))
            if diff == 0:
                l += 1
                r -= 1
            elif diff > 0:
                l += 1
            else:
                r -= 1
        return result

        