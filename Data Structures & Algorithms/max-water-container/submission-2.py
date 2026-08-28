class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        l = 0
        r = len(heights) - 1
        while l < r: # two pointer converging approach, area is limited by the shortest bar of the two. Move the pointer of the smallest bar as it is the limiting height factor.
            h = min(heights[l], heights[r])
            w = r - l
            result = max(result, h * w)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return result