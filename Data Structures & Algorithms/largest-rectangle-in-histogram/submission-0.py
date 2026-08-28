class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        rbi = [size-1] * size
        lbi = [0] * size
        stack = [] # holds elements where right boundary is not determined
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                rbi[stack[-1]] = i - 1
                stack.pop()
            stack.append(i)
        
        stack = []
        for i, h in reversed(list(enumerate(heights))):
            while stack and h < heights[stack[-1]]:
                lbi[stack[-1]] = i + 1
                stack.pop()
            stack.append(i)
        
        _max = 0
        for i in range(size):
            _max = max(_max, heights[i] * (rbi[i] - lbi[i] + 1))

        return _max


        